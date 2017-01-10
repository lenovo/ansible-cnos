#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Lenovo, Inc.

# This module is distributed WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#
# See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
#
# Module to send BGP commands to Lenovo Switches 
# Lenovo Networking
#
#---- Documentation Start ----------------------------------------------------#
DOCUMENTATION = '''
---
version_added: "1.7"
module: cnos_bgp
short_description: Performs all configurations on switches pertaining to BGP.
description: 
    - Manages network device configurations over SSH. This module allows implementors to work with the BGP 
     configurations. The operators here are overloaded to take care of all configurations pertaining to BGP. 
     In the level one, u will be able to configure BGP with AS Number, the subsequent attributes will go into 
     various configuration operation under the conext of BGP. The module is invoked using method using asNumber 
     as one of its argument. Once the level is passed through, rest of the attributes will take care of the 
     further configurations. Please go through the Overloaded variable section to understand more on how to use 
     the overloaded variables. Please see the example section to understand more how this overloading functions. 
     Results of the bgp configuration operation can be viewed in results folder.
options:
    #Options are as given below
    outputfile:
        description:
            - This specifies the file path to which the output of each command excecution is persisted. 
             Response from the device saved here. Usually the location is the results folder. 
             But your user can choose which ever path he has write permission. 
        required: true
        default: null
        choices: []
    host:
        description:
            - This is the variable which used to look into /etc/ansible/hosts file so that device IP addresses 
             on which this template has to be applied is identified. Usually we specify the ansible keyword {{ inventory_hostname }}
             which we specify in the playbook which is an abstraction to the group of 
             network elements that need to be configured.
        required: true
        default: null
        choices: []
    username:
        description:
            - Configures the username to use to authenticate the connection to the remote device. The value of 
             username is used to authenticate the SSH session. The value has to come from inventory file ideally,
             you can even enter it as variable.
        required: true
        default: 
        choices: []
    password:
        description:
            - Configures the password to use to authenticate the connection to the remote device. 
             The value of password is used to authenticate the SSH session.The value has to come from inventory file ideally,
             you can even enter it as variable.
        required: true
        default: 
        choices: []
    enablePassword:
        description:
            - Inputs the enable password, in case its enables in the device. This get ignored if the device is not demanding an enable password. 
             The value of password is used to enter the congig mode.The default value is empty string. The value has to come from inventory file ideally,
             you can even enter it as variable.
        required: false
        default: 
        choices: []
    deviceType:
        description:
            - This specifies the type of device against which the image is downloaded. The value has to come from inventory file ideally,
             you can even enter it as variable.
        required: Yes
        default: null
        choices: []
    asNum:
        description:
            - AS number 
        required: Yes
        default: null
        choices: []
    bgpArg1:
        description:
            - This is an overloaded bgp first argument. Usage of these overloaded variables are described in the table below.
             Value of these argument depends on the configuration context.
        required: Yes
        default: null
        choices: [address-family,bestpath,bgp,cluster-id,confederation,enforce-first-as,fast-external-failover,
        graceful-restart,graceful-restart-helper,log-neighbor-changes,maxas-limit,neighbor,router-id,shutdown,
        synchronization,timers,vrf]
    bgpArg2:
        description:
            - This is an overloaded bgp second argument. Usage of these overloaded variables are described in the table below.
             Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [ipv4 or ipv6, always-compare-med,compare-confed-aspath,compare-routerid,dont-compare-originator-id,tie-break-on-age,
        as-path,med,identifier,peers]
    bgpArg3:
        description:
            - This is an overloaded bgp third argument. Usage of these overloaded variables are described in the table below.
             Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [aggregate-address,client-to-client,dampening,distance,maximum-paths,network,nexthop,redistribute,save,synchronization,
        ignore or multipath-relax, confed or missing-as-worst or non-deterministic or remove-recv-med or remove-send-med]
    bgpArg4:
        description:
            - This is an overloaded bgp fourth argument. Usage of these overloaded variables are described in the table below.
             Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [Aggregate prefix, Reachability Half-life time,route-map, Distance for routes external,ebgp or ibgp, 
        IP prefix <network>,IP prefix <network>/<length>, synchronization, Delay value, direct, ospf, static, memory]
    bgpArg5:
        description:
            - This is an overloaded bgp fifth argument. Usage of these overloaded variables are described in the table below.
             Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [as-set, summary-only, Value to start reusing a route, Distance for routes internal, Supported multipath numbers,
        backdoor, map, route-map ]
    bgpArg6:
        description:
            - This is an overloaded bgp sixth argument. Usage of these overloaded variables are described in the table below.
             Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [summary-only,as-set, route-map name, Value to start suppressing a route, Distance for local routes,  Network mask, 
        Pointer to route-map entries]
    bgpArg7:
        description:
            - This is an overloaded bgp seventh argument. Usage of these overloaded variables are described in the table below.
             Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [ Maximum duration to suppress a stable route(minutes), backdoor,route-map, Name of the route map ]
    bgpArg8:
        description:
            - This is an overloaded bgp eigth argument. Usage of these overloaded variables are described in the table below.
             Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [ Un-reachability Half-life time for the penalty(minutes), backdoor]
    
---    
notes: |
     Please find below the table with option how the overloaded variables are used in the context of BGP.
     Every bgp command starts with an asNum which has to be unique. If the context is different then issue 
     a no command before attempting on these.

---
Overloaded Options: 
    bgpArg1: [address-family, address-family, address-family, address-family,address-family,address-family, address-family, address-family, address-family, address-family, address-family, address-family, address-family, address-family, address-family, address-family, address-family, address-family, bestpath,bestpath, bestpath, bestpath,bestpath,bestpath,bestpath,bgp,cluster-id,log-neighbor-changes,maxas-limit,neighbor,neighbor,router-id,shutdown,synchronization, timers,vrf]
    bgpArg2: [​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, ​ipv4 or ipv6, always-compare-med,compare-confed-aspath,compare-routerid,dont-compare-originator-id, tie-break-on-age,as-path,med,Number of times local-as to be prepended,peers, Route-Reflector Cluster-id as 32 bit quantity or Route-Reflector Cluster-id in IP address format, identifier,~,~,Delay value (seconds),~,~,Number of ASes in the AS-PATH attribute,Neighbor address,Neighbor prefix, Manually configured router identifier,~,~,Keepalive interval (seconds)]
    bgpArg3: [​aggregate-address, ​​aggregate-address, client-to-client, dampening,dampening, ​distance,maximum-paths, ​network, network, network, network, network, network, network, nexthop, redistribute, save, synchronization,~,~,~,~,~,ignore or multipath-relax,confed or missing-as-worst or non-deterministic or remove-recv-med or remove-send-med,~,~,Set routing domain confederation AS,AS number,~,~,~,~,~,AS Number,AS Number,~,~,~,~,~,~]
    bgpArg4: [Aggregate prefix, Aggregate prefix,~, route-map,Reachability Half-life time for the penalty(minutes),​Distance for routes external,​ebgp or ibgp,​synchronization,​IP prefix <network>,​IP prefix <network>, ​IP prefix <network>, ​IP prefix <network>, ​IP prefix <network>/<length>, ​IP prefix <network>/<length>, ​Delay value in milliseconds, direct or ospf or static, ​memory,~,~,~,~,~,~,ignore or multipath-relax,confed or missing-as-worst or non-deterministic or remove-recv-med or remove-send-med,~,~,Set routing domain confederation AS,AS number,~,~,~,~,~,AS Number,AS Number,~,~,~,~,~,~]
    bgpArg5: [​as-set, ​​​summary-only,~,​Route-map name,​Value to start reusing a route, ​Distance for routes internal,Suported multipath numbers,~, backdoor, mask, mask, route-map, ​route-map, backdoor, ​Delay value in milliseconds, ​route-map,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~]
    bgpArg6: [​​​​summary-only,as-set,~,~,​Value to start suppressing a route, Distance for local routes,~,~,~,~,Network Mask, Name of the route map,Name of the route map,~, Delay value in milliseconds, ​Pointer to route-map entries,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~]
    bgpArg7: [~​​,~,~,~,Maximum duration to suppress a stable route(minutes),~,~,~,~,~,route-map, backdoor,backdoor,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,]
    bgpArg8: [​​,~,~,~,​Un-reachability Half-life time for the penalty(minutes),~,~,~,~,~,backdoor,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,~,]
    Remarks: [​From Arg5 onwards its optional,​From Arg5 onwards its optional,​No further Arguments,​From Arg4 onwards its optional,From Arg4 onwards its optional,~,~,~,~,~,~,~,​From Arg5 its optional,​From Arg5 its optional,​From Arg5 its optional,~,~,From Arg5 its optional,​From Arg4 onwards its optional,​No further arguments,~,~,~,~,~,~,~,~,~,~,~,~,No Further Arguments,No Further Arguments,No Further Arguments,No Further Arguments,No Further Arguments,As Number is optional,As Number is optional,~,No arguments required,No arguments required,~,No arguments required.]
---
   |
   - For help in developing on modules, should you be so inclined, please read 
    Community Information & Contributing, Helping Testing PRs and Developing Modules.
    Module Dependency :
    1. cnos_bgp.py
    2. cnos_utility.py 
'''
EXAMPLES = '''
#The task/main.yml will look like this
---
- name: Test BGP - bestpath - always-compare-med
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data2}}"

- name: Test BGP - bestpath-compare-confed-aspat
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt  asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data3}}"

- name: Test BGP - bgp
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data4}}"

- name: Test BGP  - cluster-id
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data5}}"

- name: Test BGP - confederation-identifier
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}' bgpArg3='{{item.bgpArg3}}'
  with_items: "{{test_bgp_data6}}"

- name: Test BGP - enforce-first-as
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}'
  with_items: "{{test_bgp_data7}}"

- name: Test BGP - fast-external-failover
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}'
  with_items: "{{test_bgp_data8}}"

- name: Test BGP  - graceful-restart
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data9}}"

- name: Test BGP - graceful-restart-helper
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}'
  with_items: "{{test_bgp_data10}}"

- name: Test BGP - maxas-limit
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data11}}"

- name: Test BGP - instance
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data12}}"

- name: Test BGP  - neighbor
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}' bgpArg3='{{item.bgpArg3}}'
  with_items: "{{test_bgp_data13}}"

- name: Test BGP - router-id
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data14}}"

- name: Test BGP - synchronization
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}'
  with_items: "{{test_bgp_data15}}"

- name: Test BGP - timers
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}' bgpArg2='{{item.bgpArg2}}'
  with_items: "{{test_bgp_data16}}"

- name: Test BGP - vrf
  cnos_bgp:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_bgp_{{ inventory_hostname }}_output.txt asNum='{{item.asNum}}' bgpArg1='{{item.bgpArg1}}'
  with_items: "{{test_bgp_data17}}"

#In the vars/main.yml will look like this

  test_bgp_data1:
  - {asNum: 33, bgpArg1: "address-family", bgpArg2: "ipv4"}
  test_bgp_data2:
  - {asNum: 33, bgpArg1: "bestpath", bgpArg2: "always-compare-med"}
  test_bgp_data3:
  - {asNum: 33, bgpArg1: "bestpath", bgpArg2: "compare-confed-aspath"}
  test_bgp_data4:
  - {asNum: 33, bgpArg1: "bgp", bgpArg2: 33}
  test_bgp_data5:
  - {asNum: 33, bgpArg1: "cluster-id", bgpArg2: "1.2.3.4"}
  test_bgp_data6:
  - {asNum: 33, bgpArg1: "confederation", bgpArg2: "identifier", bgpArg3: "1.2.3.4"}
  test_bgp_data7:
  - {asNum: 33, bgpArg1: "enforce-first-as"}
  test_bgp_data8:
  - {asNum: 33, bgpArg1: "fast-external-failover"}
  test_bgp_data9:
  - {asNum: 33, bgpArg1: "graceful-restart", bgpArg2: 333}
  test_bgp_data10:
  - {asNum: 33, bgpArg1: "graceful-restart-helper"}
  test_bgp_data11:
  - {asNum: 33, bgpArg1: "maxas-limit", bgpArg2: 333}
  test_bgp_data12:
  - {asNum: 33, bgpArg1: "instance", bgpArg2: "33"}
  test_bgp_data13:
  - {asNum: 33, bgpArg1: "neighbor", bgpArg2: "1.2.3.4", bgpArg3: 13}
  test_bgp_data14:
  - {asNum: 33, bgpArg1: "router-id", bgpArg2: "1.2.3.4"}
  test_bgp_data15:
  - {asNum: 33, bgpArg1: "synchronization"}
  test_bgp_data16:
  - {asNum: 33, bgpArg1: "timers", bgpArg2: 333}
  test_bgp_data17:
  - {asNum: 33, bgpArg1: "vrf"}
#In the inventory file u specify like this
  inventory sample: |
    [cnos_bgp_sample]
    10.241.107.39  username=<username> password=<password> deviceType=g8272_cnos 
    10.241.107.40  username=<username> password=<password> deviceType=g8272_cnos 

'''

RETURN = '''
return value: |
  On successful execution, the method returns and empty string with a message "BGP configurations accomplished" 
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
    # Define parameters for bgp creation entry
    #
    module = AnsibleModule(
        argument_spec=dict(
            outputfile=dict(required=True),
            host=dict(required=True),
            username=dict(required=True),
            password=dict(required=True),
            enablePassword=dict(required=False),
            deviceType=dict(required=True),
            bgpArg1=dict(required=True),
            bgpArg2=dict(required=False),
            bgpArg3=dict(required=False),
            bgpArg4=dict(required=False),
            bgpArg5=dict(required=False),
            bgpArg6=dict(required=False),
            bgpArg7=dict(required=False),
            bgpArg8=dict(required=False),
            asNum=dict(required=True),),
        supports_check_mode=False)

    username = module.params['username']
    password = module.params['password']
    enablePassword = module.params['enablePassword']
    bgpArg1= module.params['bgpArg1']
    bgpArg2 = module.params['bgpArg2']
    bgpArg3= module.params['bgpArg3']
    bgpArg4= module.params['bgpArg4']
    bgpArg5 = module.params['bgpArg5']
    bgpArg6= module.params['bgpArg6']
    bgpArg7 = module.params['bgpArg7']
    bgpArg8= module.params['bgpArg8']
    asNum = module.params['asNum']
    outputfile =  module.params['outputfile']
    hostIP = module.params['host']
    deviceType = module.params['deviceType']
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
    output = output + cnos_utility.routerConfig(remote_conn, deviceType, "(config)#", 2, "bgp", asNum, 
                                                bgpArg1, bgpArg2, bgpArg3,bgpArg4, bgpArg5, bgpArg6,bgpArg7, bgpArg8  )
    
    #Save it into the file
    file = open(outputfile, "a")
    file.write(output)
    file.close()
    
    # Logic to check when changes occur or not
    errorMsg = cnos_utility.checkOutputForError(output)
    if(errorMsg == None):
        module.exit_json(changed=True, msg="BGP configurations accomplished")
    else:
        module.fail_json(msg=errorMsg)
    

if __name__ == '__main__':
        main()
                                   
