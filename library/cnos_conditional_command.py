#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Lenovo, Inc.

# This module is distributed WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#
# See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
#
# Module to send Conditional CLI commands to Lenovo Switches
# Lenovo Networking
#
#---- Documentation Start ----------------------------------------------------#
DOCUMENTATION = '''
---
version_added: "1.7"
module: cnos_conditional_command
short_description: Run a single CNOS Command on Devices based on conditions specified at inventory.
description: 
   - Manages network device configurations over SSH. This module allows implementors to work with the device 
   running-config. It provides a way to push a CNOS command onto a network device by evaluting the current 
   running-config and only pushing configuration commands that are not already configured. The command is 
   passed as an argument to the method. This method functions as same as runcommand. Only execption is when 
   u specify and inventory variable "condition =<flag string>", the command is executed for that network 
   element who has the same flag string passed on to the task as variable . But when there is a case where 
   you want to skip the command for one or few devices in that group, it is preferable to use this method. 
   By default it will be value for condition is True.
   
options:
# Options are as given below
    clicommand:
        description:
            - Specify the CLI command as an attribute to this method. Pass on the command in double quotes. 
            - The variables can also be placed directly on to CLIs or can come from the vars folder.
        required: true
        default: null
        choices: []
    outputfile:
        description:
            - This specifies the file path to which the output of each command excection is persisted. 
            - Response from the device saved here. Usually the location is the results folder. 
            - But your user can choose which ever path he has write permission. 
        required: true
        default: null
        choices: []
    condition:
        description:
            - If you specify condition = False in the inventory file against any device, the command 
            execution is skipped for that device.
        required: true
        default: null
        choices: []
    flag:
        description:
            - If a task has to get executed, you have to set the flag same as that its specified in the 
            inventory for the particular device.
        required: true
        default: null
        choices: []
    host:
        description:
            - This is the variable which used to look into /etc/ansible/hosts file so that device IP addresses 
            - on which this template has to be applied is identified. Usually we specify the ansible keyword 
            - {{ inventory_hostname }} which we specify in the playbook which is an abstraction to the group of 
            - network elements that need to be configured.
        required: true
        default: null
        choices: []
    username:
        description:
            - Configures the username to use to authenticate the connection to the remote device. The value of 
            - username is used to authenticate the SSH session. The value has to come from inventory file ideally,
            - you can even enter it as variable.
        required: true
        default: 
        choices: []
    password:
        description:
            - Configures the password to use to authenticate the connection to the remote device. 
            - The value of password is used to authenticate the SSH session.The value has to come from inventory file ideally,
            - you can even enter it as variable.
        required: true
        default: 
        choices: []
    enablePassword:
        description:
            - Inputs the enable password, in case its enables in the device. This get ignored if the device is not demanding an enable password. 
            - The value of password is used to enter the config mode.The default value is empty string. The value has to come from inventory file ideally,
            - you can even enter it as variable.
        required: false
        default: 
        choices: []
    deviceType:
        description:
            - This specifies the type of device against which the image is downloaded. The value has to come from inventory file ideally,
            - you can even enter it as variable.
        required: Yes
        default: null
        choices: []
        
notes:
    - For help in developing on modules, should you be so inclined, please read 
     Community Information & Contributing, Helping Testing PRs and Developing Modules.
     Module Dependency :
    1. cnos_conditional_command.py
    2. cnos_utility.py 
'''
EXAMPLES = '''
# In the tasks/main.yml you specify like this

- name: Applying CLI template on VLAG Tier1 Leaf Switch1
  cnos_conditional_command: host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  
  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} 
  condition={{ hostvars[inventory_hostname]['condition']}} flag='{{item.flag}}' command="spanning-tree mode enable"  
  enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_conditional_command_{{ inventory_hostname }}_output.txt
  with_items: "{{vlag_1tier_leaf_data}}"

In the vars/main.yml specify

vlag_1tier_leaf_data:
  - {flag: leaf_switch2, enablePassword: "anil"}

In the inventory file u specify like this
[vlag_1tier_leaf]
10.240.178.74  username=<username> password=<password> deviceType=g8272_cnos condition=leaf_switch1
10.240.178.75  username=<username> password=<password> deviceType=g8272_cnos condition=leaf_switch2

'''

RETURN = '''

On successful execution, the method returns and empty string with a message "Command Applied" in json format. 
But upon any failure, the output will be the error display string.

'''
#---- Documentation Ends ----------------------------------------------------#
#---- Logic Start ------------------------------------------------------------#
import sys
import paramiko
import time
import argparse
import socket
import array
import json
import time
import re
try:
    import cnos_utility
    HAS_LIB=True
except:
    HAS_LIB=False

#
# load Ansible module
#
from ansible.module_utils.basic import *
from collections import defaultdict

#
def  main():
    #
    # Define parameters for commandline entry
    #
    module = AnsibleModule(
        argument_spec=dict(
            clicommand=dict(required=True),
            outputfile=dict(required=True),
	        condition=dict(required=True),
            flag=dict(required=True),
            host=dict(required=True),
            deviceType=dict(required=True),
            username=dict(required=True),
            password=dict(required=True),
            enablePassword=dict(required=False),),
         supports_check_mode=False)

    username = module.params['username']
    password = module.params['password']
    enablePassword = module.params['enablePassword']
    condition= module.params['condition']
    flag= module.params['flag']
    cliCommand= module.params['clicommand']
    outputfile =  module.params['outputfile']
    deviceType = module.params['deviceType']
    hostIP = module.params['host']
    output = ""
    
    if (condition != flag):
        module.exit_json(changed=True, msg="Command Skipped for this value")
        return " " 
    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection with the switch
    remote_conn_pre.connect(hostIP, username=username, password=password)
    time.sleep(2)
    
    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    time.sleep(2)
    
    # Enable and enter configure terminal then send command
    #
    # Enable and enter configure terminal then send command
    output = output + cnos_utility.waitForDeviceResponse("\n",">", 2, remote_conn)
    output = output + cnos_utility.enterEnableModeForDevice(enablePassword, 3, remote_conn)
    
    #Make terminal length = 0
    output = output + cnos_utility.waitForDeviceResponse("terminal length 0\n","#", 2, remote_conn)
    
    #Go to config mode
    output = output + cnos_utility.waitForDeviceResponse("configure d\n","(config)#", 2, remote_conn)
    
    #Send the CLi command
    output = output + cnos_utility.waitForDeviceResponse(cliCommand +"\n","(config)#", 2, remote_conn)
    
    #Save it into the file
    file = open(outputfile, "a")
    file.write(output)
    file.close()
    
    # Logic to check when changes occur or not
    errorMsg = cnos_utility.checkOutputForError(output)
    if(errorMsg == None):
        module.exit_json(changed=True, msg="CLI Command executed and results saved in file ")
    else:
        module.fail_json(msg=errorMsg)
    

if __name__ == '__main__':
        main()
                                   
