#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Lenovo, Inc.

# This module is distributed WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#
# See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
#
# Module to send VLAG commands to Lenovo Switches
# Lenovo Networking
#
#---- Documentation Start ----------------------------------------------------#
DOCUMENTATION = '''
---
version_added: "1.7"
module: cnos_vlag
short_description: Performs all configurations on switches pertaining to VLAG.
description: 
    - Manages network device configurations over SSH. This module allows implementors to work with the VLAG 
    configurations. The operators here are overloaded to take care of all configurations pertaining to vlag. 
    Apart from the regular device connection related attributes there are 4 VLAG Argument which are overloaded
    to achieve all configurations. They are vlagArg1, vlagArg2, vlagArg3, vlagArg4 respectively. 
    Please see the example section to understand more how to use this overloading functions. 
    Results of the backup operation can be viewed in results folder.
options:
# Options are as given below
    
    outputfile:
        description:
            - This specifies the file path to which the output of each command execution is persisted. 
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
    deviceType:
        description:
            - This specifies the type of device against which the image is downloaded. 
        required: Yes
        default: null
        choices: []
    vlagArg1:
        description:
            - This is an overloaded vlag first argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: Yes
        default: null
        choices: [enable, auto-recovery,config-consistency,isl,mac-address-table,peer-gateway,priority,startup-delay,tier-id,vrrp,instance,hlthchk]
    vlagArg2:
        description:
            - This is an overloaded vlag second argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [Interval in seconds,disable or strict,Port Aggregation Number,VLAG priority,Delay time in seconds,VLAG tier-id value,
        VLAG instance number,keepalive-attempts,keepalive-interval,retry-interval,peer-ip]
    vlagArg3:
        description:
            - This is an overloaded vlag third argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [enable or port-aggregation,Number of keepalive attempts,Interval in seconds,Interval in seconds,VLAG health check peer IP4 address]
    vlagArg4:
        description:
            - This is an overloaded vlag fourth argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [Port Aggregation Number,default or management]

notes:

Please find below the table with option how the overloaded variables are used in the context of VLAG.

    vlagArg1:[enable, auto-recovery,config-consistency,isl,mac-address-table,peer-gateway,priority,startup-delay,tier-id,vrrp,instance,hlthchk,hlthchk,hlthchk,hlthchk]
    vlagArg2:[, Interval in seconds,disable or strict,Port Aggregation Number,,,VLAG priority,Delay time in seconds,VLAG tier-id value,,VLAG instance number,
        keepalive-attempts,keepalive-interval,retry-interval,peer-ip]
    vlagArg3:[,,,,,,,,,,enable or port-aggregation,Number of keepalive attempts,Interval in seconds,Interval in seconds,VLAG health check peer IP4 address]
    vlagArg4:[,,,,,,,,,,Port Aggregation Number,,,,default or management]
    Remarks:[No arguments required,,Disable VLAG consistency checking or Strict mode,isl,No arguments required,No arguments required,,,,
        No arguments required,vlagArg4 applies only if vlagArg3 is port-aggregation,,,,]

    - For help in developing on modules, should you be so inclined, please read
    Community Information & Contributing, Helping Testing PRs and Developing Modules.
    Module Dependency :
    1. cnos_vlag.py
    2. cnos_utility.py

'''
EXAMPLES = '''
The task/main.yml will look like this

---

- name: Test Vlag  - enable
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}'
  with_items: "{{test_vlag_data1}}"

- name: Test Vlag - autorecovery
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}'
  with_items: "{{test_vlag_data2}}"

- name: Test Vlag - config-consistency
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}'
  with_items: "{{test_vlag_data3}}"

- name: Test Vlag - isl
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}'
  with_items: "{{test_vlag_data4}}"

- name: Test Vlag  - mac-address-table
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}'
  with_items: "{{test_vlag_data5}}"

- name: Test Vlag - peer-gateway
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}'
  with_items: "{{test_vlag_data6}}"

- name: Test Vlag - priority
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}'
  with_items: "{{test_vlag_data7}}"

- name: Test Vlag - startup-delay
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}'
  with_items: "{{test_vlag_data8}}"

- name: Test Vlag  - tier-id
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}'
  with_items: "{{test_vlag_data9}}"

- name: Test Vlag - vrrp
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}'
  with_items: "{{test_vlag_data10}}"

- name: Test Vlag - instance
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}' vlagArg3='{{item.vlagArg3}}'
  with_items: "{{test_vlag_data11}}"

- name: Test Vlag - instance2
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}'
  with_items: "{{test_vlag_data12}}"

- name: Test Vlag  - keepalive-attempts
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}' vlagArg3='{{item.vlagArg3}}'
  with_items: "{{test_vlag_data13}}"

- name: Test Vlag - keepalive-interval
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}' vlagArg3='{{item.vlagArg3}}'
  with_items: "{{test_vlag_data14}}"

- name: Test Vlag - retry-interval
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}' vlagArg3='{{item.vlagArg3}}'
  with_items: "{{test_vlag_data15}}"

- name: Test Vlag - peer ip
  cnos_vlag:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_vlag_{{ inventory_hostname }}_output.txt vlagArg1='{{item.vlagArg1}}' vlagArg2='{{item.vlagArg2}}' vlagArg3='{{item.vlagArg3}}'
  with_items: "{{test_vlag_data16}}"


In the vars/main.yml will look like this

---
test_vlag_data1:
  - {vlagArg1: "enable"}
test_vlag_data2:
  - {vlagArg1: "auto-recovery", vlagArg2: 266}
test_vlag_data3:
  - {vlagArg1: "config-consistency", vlagArg2: "strict"}
test_vlag_data4:
  - {vlagArg1: "isl", vlagArg2: 23}
test_vlag_data5:
  - {vlagArg1: "mac-address-table"}
test_vlag_data6:
  - {vlagArg1: "peer-gateway"}
test_vlag_data7:
  - {vlagArg1: "priority", vlagArg2: 1313}
test_vlag_data8:
  - {vlagArg1: "startup-delay", vlagArg2: 323}
test_vlag_data9:
  - {vlagArg1: "tier-id", vlagArg2: 313}
test_vlag_data10:
  - {vlagArg1: "vrrp"}
test_vlag_data11:
  - {vlagArg1: "instance", vlagArg2: 33, vlagArg3: 333}
test_vlag_data12:
  - {vlagArg1: "instance", vlagArg2: "33"}
test_vlag_data13:
  - {vlagArg1: "hlthchk", vlagArg2: "keepalive-attempts", vlagArg3: 13}
test_vlag_data14:
  - {vlagArg1: "hlthchk", vlagArg2: "keepalive-interval", vlagArg3: 131}
test_vlag_data15:
  - {vlagArg1: "hlthchk", vlagArg2: "retry-interval", vlagArg3: 133}
test_vlag_data16:
  - {vlagArg1: "hlthchk", vlagArg2: "peer-ip", vlagArg3: "1.2.3.4"}

In the inventory file u specify like this
[cnos_vlag_sample]
10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos

'''

RETURN = '''

On successful execution, the method returns and empty string with a message "VLAG configurations accomplished" 
in json format. But upon any failure, the output will be the error display string. You may have to rectify the 
error and try again.

'''
#---- Documentation Ends ----------------------------------------------------#
#---- Logic Start ------------------------------------------------------------###
#

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
    # Define parameters for vlag creation entry
    #
    module = AnsibleModule(
        argument_spec=dict(
            outputfile=dict(required=True),
            host=dict(required=True),
            username=dict(required=True),
            password=dict(required=True),
            enablePassword=dict(required=False),
            deviceType=dict(required=True),
            vlagArg1=dict(required=True),
            vlagArg2=dict(required=False),
            vlagArg3=dict(required=False),
            vlagArg4=dict(required=False),),
        supports_check_mode=False)

    username = module.params['username']
    password = module.params['password']
    enablePassword = module.params['enablePassword']
    outputfile =  module.params['outputfile']
    hostIP = module.params['host']
    deviceType = module.params['deviceType']
    vlagArg1= module.params['vlagArg1']
    vlagArg2 = module.params['vlagArg2']
    vlagArg3= module.params['vlagArg3']
    vlagArg4 = module.params['vlagArg4']
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
        
    #Go to config mode
    output = output + cnos_utility.waitForDeviceResponse("configure d\n","(config)#", 2, remote_conn)
    
    #Send the CLi command
    output = output + cnos_utility.vlagConfig(remote_conn, deviceType, "(config)#", 2, vlagArg1, vlagArg2, vlagArg3, vlagArg4)
    
    #Save it into the file
    file = open(outputfile, "w")
    file.write(output)
    file.close()
    
    # need to add logic to check when changes occur or not
    errorMsg = cnos_utility.checkOutputForError(output)
    if(errorMsg == None):
        module.exit_json(changed=True, msg="vlag configurations accomplished")
    else:
        module.fail_json(msg=errorMsg)
    

if __name__ == '__main__':
        main()
                                   
