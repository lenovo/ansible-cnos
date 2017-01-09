#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Lenovo, Inc.

# This module is distributed WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#
# See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
#
# Module to display running config of Switches
# Lenovo Networking
#
#---- Documentation Start ----------------------------------------------------#
DOCUMENTATION = '''
---
version_added: "1.7"
module: cnos_showrun
short_description: Exceutes a show running config operation.
description: 
    - Manages network device configurations over SSH. This module allows implementors to work with the device 
    running-config. Its just a utility method to show the running configuration of a device. It will output 
    the results to results folder. This is a just a wrapper over cnos_command where the command 
    "display running-config" is executed for the user.

options:
# Options are as given below
    
    outputfile:
        description:
            - This specifies the file path to which the output of each command excection is persisted. 
             Response from the device saved here. Usually the location is the results folder. 
             But your user can choose which ever path he has write permission. 
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
            - The value of password is used to enter the congig mode.The default value is empty string. The value has to come from inventory file ideally,
            - you can even enter it as variable.
        required: false
        default: 
        choices: []
    
Notes:
    - For help in developing on modules, should you be so inclined, please read 
    Community Information & Contributing, Helping Testing PRs and Developing Modules.
    Module Dependency :
    1. cnos_showrun.py
    2. cnos_utility.py 

'''

EXAMPLES = '''
- name: Run show running-config
  cnos_showrun: host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} enablePassword='{{item.enablePassword}}' outputfile=/home/test/ansible/cnos/Random_Command_Output.txt
  with_items: test_showrun_data1

Inside vars/main.yml
---
test_showrun_data1:
  - {enablePassword: "anil"}
  
In the inventory file u specify like this

[cnos_backup_sample]
10.241.107.39  username=<username> password=<password> deviceType=g8272_cnos 
10.241.107.40  username=<username> password=<password> deviceType=g8272_cnos   


'''

RETURN = '''

On successful execution, the method returns and empty string with a message "Command Applied" 
in json format. But upon any failure, the output will be the error display string.

'''
#---- Documentation Ends ----------------------------------------------------#
#---- Logic Start ------------------------------------------------------------###

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
            outputfile=dict(required=True),
            host=dict(required=True),
            username=dict(required=True),
            password=dict(required=True),
            enablePassword=dict(required=False),),
        supports_check_mode=False)
    
    username = module.params['username']
    password = module.params['password']
    enablePassword = module.params['enablePassword']
    cliCommand= "display running-config"
    outputfile =  module.params['outputfile']
    hostIP = module.params['host']
    output = ""
    
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
    output = output + cnos_utility.waitForDeviceResponse("\n",">", 2, remote_conn)
    
    output = output + cnos_utility.enterEnableModeForDevice(enablePassword, 3, remote_conn)
            
    #Make terminal length = 0
    output = output + cnos_utility.waitForDeviceResponse("terminal length 0\n","#", 2, remote_conn)
            
    #Send the CLi command
    output = output + cnos_utility.waitForDeviceResponse(cliCommand +"\n","#", 2, remote_conn)
        
    #Save it into the file
    file = open(outputfile, "a")
    file.write(output)
    file.close()
        
    errorMsg = cnos_utility.checkOutputForError(output)
    if(errorMsg == None):
        module.exit_json(changed=True, msg="Running Configuration saved in file ")
    else:
        module.fail_json(msg=errorMsg)
        
if __name__ == '__main__':
    main()
                                       
