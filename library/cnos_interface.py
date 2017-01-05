#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Lenovo, Inc.

# This module is distributed WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#
# See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
#
# Module to send Port channel commands to Lenovo Switches
# Lenovo Networking
#
#---- Documentation Start ----------------------------------------------------#
DOCUMENTATION = '''
---
version_added: "1.7"
module: cnos_interface
short_description: Performs all configurations on switches pertaining to Interfaces.
description: 
    - Manages network device configurations over SSH. This module allows implementors to work with the 
    Interface configurations. The operators here are overloaded to take care of all 
    configurations pertaining to Interfaces. Apart from the regular device connection related attributes 
    there are 6 Interface Arguments which are overloaded to achieve all configurations. They are interfaceArg1, 
    interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5, interfaceArg6 respectively. Interface configurations are taken care 
    at six contexts in a regular CLI. They are
    1. Interface Name - Configurations
    2. Ethernet Interface - Configurations
    3. Loopback Interface Configurations
    4. Management Interface Configurations
    5. Port Aggregation - Configurations
    6. VLAN Configurations
    Please see the example section to understand more how to use this overloaded functions. Results of the backup operation can be viewed in results folder.
options:
# Options are as given below
    
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
            - The value of password is used to enter the congig mode.The default value is empty string. 
        required: false
        default: 
        choices: []
    deviceType:
        description:
            - This specifies the type of device against which the image is downloaded. 
        required: Yes
        default: null
        choices: []
    interfaceRange:
        description:
            - This specifies the interface range in which the port aggregation is envisaged
        required: Yes
        default: null
        choices: []
    interfaceOption:
        description:
            - This specifies the attribute you specify subsequent to interface command
        required: Yes
        default: null
        choices: [None, ethernet, loopback, mgmt, port-aggregation, vlan]
    interfaceArg1:
        description:
            - This is an overloaded portCh first argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: Yes
        default: null
        choices: [aggregation-group, bfd, bridgeport, description, duplex, flowcontrol, ip, ipv6, lacp, lldp,
        load-interval, mac, mac-address, mac-learn, microburst-detection, mtu, service, service-policy,
        shutdown, snmp, spanning-tree, speed, storm-control, vlan, vrrp, port-aggregation]
    interfaceArg2:
        description:
            - This is an overloaded portCh second argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [aggregation-group number, access or mode or trunk, description, auto or full or half,
        recieve or send, port-priority, suspend-individual, timeout,     receive or transmit or trap-notification,
        tlv-select, Load interval delay in seconds, counter, Name for the MAC Access List, mac-address in HHHH.HHHH.HHHH format,
        THRESHOLD  Value in unit of buffer cell, <64-9216>  MTU in bytes:<64-9216> for L2 packet,<576-9216> for 
        L3 IPv4 packet, <1280-9216> for L3 IPv6 packet, enter the instance id, input or output, copp-system-policy,
        type, 1000  or  10000  or   40000 or   auto, broadcast or multicast or unicast, disable or enable or egress-only,
        Virtual router identifier, destination-ip or destination-mac or destination-port or source-dest-ip or 
        source-dest-mac or source-dest-port or source-interface or source-ip or source-mac or source-port]
    interfaceArg3:
        description:
            - This is an overloaded portCh third argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [active or on or passive, on or off, LACP port priority, long or short, link-aggregation or 
        mac-phy-status or management-address or max-frame-size or port-description or port-protocol-vlan or 
        port-vlan or power-mdi or protocol-identity or system-capabilities or system-description or system-name
        or vid-management or vlan-name, counter for load interval, policy input name, all or Copp class name to attach,
        qos, queing, Enter the allowed traffic level, ipv6]
    interfaceArg4:
        description:
            - This is an overloaded portCh fourth argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [key-chain, key-id, keyed-md5 or keyed-sha1 or meticulous-keyed-md5 or meticulous-keyed-sha1 or simple, Interval value in milliseconds, 
         Destination IP (Both IPV4 and IPV6),in or out, MAC address, Time-out value in seconds, class-id, request, Specify the IPv4 address,
         OSPF area ID as a decimal value, OSPF area ID in IP address format, anycast or secondary, ethernet, vlan, MAC (hardware) address in HHHH.HHHH.HHHH format,
         Load interval delay in seconds, Specify policy input name, input or output, cost, port-priority, BFD minimum receive interval,source-interface]
         
    interfaceArg5:
        description:
            - This is an overloaded portCh fifth argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [name of key-chain,  key-Id Value, key-chain , key-id, BFD minimum receive interval, Value of Hello Multiplier, 
        admin-down or multihop or non-persistent, Vendor class-identifier name, bootfile-name or host-name or log-server or ntp-server or tftp-server-name,
        Slot/chassis number, Vlan interface, Specify policy input name, Port path cost or auto, Port priority increments of 32]
    interfaceArg6:
        description:
            - This is an overloaded portCh fifth argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [Authentication key string, name of key-chain, key-Id Value, Value of Hello Multiplier, admin-down or non-persistent]
    interfaceArg7:
        description:
            - This is an overloaded portCh fifth argument. Usage of these overloaded variables are described in the table below.
            Value of these argument depends on the configuration context.
        required: No
        default: null
        choices: [Authentication key string, admin-down]
       
notes:

Please find below the table with option how the overloaded variables are used in the context of Interfaces. 


    interfaceArg1: [aggregation-group,bfd,bfd,bfd,bfd,bfd,bfd,bfd,bfd,bfd,bridge-port,description,duplex,flowcontrol,ip,ip,ip,ip,ip,ip,ip,ip,ip,ip,ip,ip,ip,ip,
    ipv6,ipv6,ipv6,ipv6,ipv6,ipv6,ipv6,lacp,lacp,lacp,lldp,lldp,load-interval,load-interval,mac,mac-address,mac-learn,microburst-detection,mtu,service,service-policy,
    service-policy,service-policy,service-policy,shutdown,snmp,spanning-tree,spanning-tree,spanning-tree,spanning-tree,spanning-tree,spanning-tree,
    spanning-tree,spanning-tree,spanning-tree,spanning-tree,spanning-tree,speed,storm-control,vlan,vrrp,port-aggregation]

    interfaceArg2:[Specify a aggregation-group number,authentication,authentication,echo,ipv4 or ipv6,ipv4 or ipv6,ipv4 or ipv6,ipv4 or ipv6,interval,neighbor,
    access or mode or trunk, Interface description of maximum 80 characters,auto or full or half,recieve or send,access-group,address,arp,arp,dhcp,dhcp,dhcp,
    ospf,port,port-unreachable,redirects,router,router,unreachables,address,address,dhcp,dhcp,link-local,nd,neighbor,port-priority,suspend-individual,timeout,
    receive or transmit or trap-notification,tlv-select,Load interval delay in seconds,counter,Name for the MAC Access List,mac-address in HHHH.HHHH.HHHH format,,
    THRESHOLD  Value in unit of buffer cell, <64-9216>  MTU in bytes:<64-9216> for L2 packet,<576-9216> for L3 IPv4 packet, <1280-9216> for L3 IPv6 packet,
    enter the instance id that should be mapped for the evc,input or output,copp-system-policy,type,type ,,,bpdufilter or bpduguard,cost,enable or disable,
    guard,link-type,mst,mst,port,port-priority,vlan,vlan, 1000  or  10000  or   40000 or   auto, broadcast or multicast or unicast,disable or enable or egress-only,
    Virtual router identifier,destination-ip or destination-mac or destination-port or source-dest-ip or source-dest-mac or source-dest-port or source-interface or source-ip or
    source-mac or source-port]

    interfaceArg3:[active or on or passive,keyed-md5 or keyed-sha1 or meticulous-keyed-md5 or meticulous-keyed-sha1 or simple,keyed-md5 or keyed-sha1 or meticulous-keyed-md5 or meticulous-keyed-sha1 or simple,
    ,authentication,authentication,echo,interval,Interval value in milliseconds,Source IP (Both IPV4 and IPV6),,,,on or off,List name,, IP address of the ARP entry ,
    timeout,client,client,relay,,List name,,,area or multi-area,area or multi-area,,dhcp,IPv6 address,Specify the IPv6 address for relay,Specify the IPv6 address for relay,
    IPv6 address format: aaaa:bbbb:cccc:dddd:eeee:ffff:gggg:hhhh, ,Neighbor's IPv6 address,LACP port priority,,long or short,,link-aggregation or mac-phy-status or 
    management-address or max-frame-size or port-description or port-protocol-vlan or port-vlan or power-mdi or protocol-identity or system-capabilities or 
    system-description or system-name or vid-management or vlan-name,,Specify counter for this load interval,,,,,,,Specify policy input name,all or Copp class name to attach,
    qos,queing,,,enable or disable,Port path cost or auto,    loop or root,auto or point-to-point or shared,MST instance range,MST instance range,,Port priority in increments of 32,
    vlan range,vlan range,,Enter the allowed traffic level, decimal optional,,ipv6,source-interface]

    interfaceArg4:[,key-chain,key-id,,keyed-md5 or keyed-sha1 or meticulous-keyed-md5 or meticulous-keyed-sha1 or simple,
    keyed-md5 or keyed-sha1 or meticulous-keyed-md5 or meticulous-keyed-sha1 or simple,,Interval value in milliseconds,BFD minimum receive interval,
    Destination IP (Both IPV4 and IPV6),,,,,in or out,,MAC address,Time-out value in seconds,class-id,request,Specify the IPv4 address,,
    in or out,,,OSPF area ID as a decimal value,OSPF area ID as a decimal value,,,anycast or secondary,ethernet,vlan,,,MAC (hardware) address in HHHH.HHHH.HHHH format,
    ,,,,,Load interval delay in seconds,,,,,,,,,Specify policy input name,input or output,,,,,,,,cost,port-priority,,,port-priority,cost,,,,,,]

    interfaceArg5:[,name of key-chain, key-Id Value,,key-chain,key-id,,BFD minimum receive interval,Value of Hello Multiplier,admin-down or multihop or non-persistent,
    ,,,,,,,,Vendor class-identifier name,bootfile-name or host-name or log-server or ntp-server or tftp-server-name,,,,,,,,,,,Slot/chassis number,Vlan interface,
    ,,,,,,,,,,,,,,,,,,,Specify policy input name,,,,,,,,Port path cost or auto,Port priority increments of 32,,,Port priority increments of 32,Port path cost or auto,
    ,,,,,]

    interfaceArg6:[,,Authentication key string,,name of key-chain,key-Id Value,,Value of Hello Multiplier,,admin-down or non-persistent,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,]

    interfaceArg7:[,,,,,Authentication key string,,,,admin-down,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,]

    Remarks:[,,,No further arguments,From interfaceArg3 onwards its optional,,,,,From interfaceArg5 onwards its optional,,,,,,This feature is not implemented yet,
    ,,,,,This feature is not implemented yet,,No further argumentsNo further arguments,No further arguments,No further arguments,No further arguments,
    No further arguments,interfaceArg4 is optional,From interfaceArg4 is optional,,,This feature is not implemented yet,,,No arguments for this command further,
    No arguments for this command further,No arguments for this command further,No arguments for this command further,,,No arguments for this command further,
    ,No arguments for this command further,,,,,,,,No arguments for this command further,No arguments for this command further,,,,,,,,,,,,
    1000 1Gb/s 10000  10Gb/s 40000  40Gb/s auto Auto negotiate speed, ,,interfaceArg3 is optional,Context changes here.
    interfaceArg003 is optional for many arguments. Check switch documentation before u apply.]

    - For help in developing on modules, should you be so inclined, please read 
    Community Information & Contributing, Helping Testing PRs and Developing Modules.
    Module Dependency :
    1. cnos_interface.py
    2. cnos_utility.py 
'''
EXAMPLES = '''
The task/main.yml will look like this
- name: Test Interface Ethernet - aggregation-group
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_interface_ethernet_data1}}"

- name: Test Interface Ethernet - bridge-port
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt  interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' ortChArg3='{{item.interfaceArg3}}'
  with_items: "{{test_interface_ethernet_data2}}"

- name: Test Interface Ethernet - bridgeport mode
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_interface_ethernet_data3}}"

- name: Test Interface Ethernet  - Description
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_interface_ethernet_data4}}"

- name: Test Interface Ethernet - Duplex
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_interface_ethernet_data5}}"

- name: Test Interface Ethernet - flowcontrol
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_interface_ethernet_data6}}"

- name: Test Interface Ethernet - lacp
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_interface_ethernet_data7}}"

- name: Test Interface Ethernet  - lldp
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_interface_ethernet_data8}}"

- name: Test Interface Ethernet - load-interval
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}' interfaceArg4='{{item.interfaceArg4}}'
  with_items: "{{test_interface_ethernet_data9}}"

- name: Test Interface Ethernet - mac
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_interface_ethernet_data10}}"

- name: Test Interface Ethernet - microburst-detection
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_interface_ethernet_data11}}"

- name: Test Interface Ethernet  - mtu
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_interface_ethernet_data12}}"

- name: Test Interface Ethernet - service-policy
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_interface_ethernet_data13}}"

- name: Test Interface Ethernet - speed
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_interface_ethernet_data14}}"

- name: Test Interface Ethernet - storm
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_interface_ethernet_data15}}"

- name: Test Interface Ethernet - vlan
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_interface_ethernet_data16}}"

- name: Test Interface Ethernet - vrrp
  cnos_interface:  host={{ inventory_hostname }} enablePassword='{{item.enablePassword}}' outputfile=./results/cnos_interface_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_interface_ethernet_data17}}"

In the vars/main.yml will look like this
---

# This contain sample values
---
test_interface_ethernet_data1:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "aggregation-group", interfaceArg2: 33, interfaceArg3: "active"}
test_interface_ethernet_data2:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "bridge-port", interfaceArg2: "access", interfaceArg3: 33}
test_interface_ethernet_data3:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "bridge-port", interfaceArg2: "mode", interfaceArg3: "access"}
test_interface_ethernet_data4:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "description", interfaceArg2: "Hentammoo "}
test_interface_ethernet_data5:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "duplex", interfaceArg2: "auto"}
test_interface_ethernet_data6:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "flowcontrol", interfaceArg2: "send", interfaceArg3: "off"}
test_interface_ethernet_data7:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "lacp", interfaceArg2: "port-priority", interfaceArg3: 33}
test_interface_ethernet_data8:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "lldp", interfaceArg2: "tlv-select", interfaceArg3: "max-frame-size"}
test_interface_ethernet_data9:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "load-interval", interfaceArg2: "counter", interfaceArg3: 2,interfaceArg4: 33 }
test_interface_ethernet_data10:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "mac", interfaceArg2: "Anil"}
test_interface_ethernet_data11:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "microburst-detection", interfaceArg2: 25}
test_interface_ethernet_data12:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "mtu", interfaceArg2: 66}
test_interface_ethernet_data13:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "service-policy", interfaceArg2: "input", interfaceArg3: "Anil"}
test_interface_ethernet_data14:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "speed", interfaceArg2: "auto"}
test_interface_ethernet_data15:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "storm-control", interfaceArg2: "broadcast", interfaceArg3: 12 }
test_interface_ethernet_data16:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "vlan", interfaceArg2: "disable"}
test_interface_ethernet_data17:
  - {username: <username>, password: <password>, enablePassword: "anil", deviceType: g8272_cnos, interfaceRange: 33, interfaceArg1: "vrrp", interfaceArg2: 33}

In the inventory file u specify like this
[cnos_interface_sample]
10.241.107.39  username=<username> password=<password> deviceType=g8272_cnos enablePassword: anil 
10.241.107.40  username=<username> password=<password> deviceType=g8272_cnos 


'''

RETURN = '''

On successful execution, the method returns and empty string with a message "Interface configurations 
accomplished" in json format. But upon any failure, the output will be the error display string. 
You may have to rectify the error and try again.

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
    # Define parameters for portChannel creation entry
    #
    module = AnsibleModule(
        argument_spec=dict(
            outputfile=dict(required=True),
            host=dict(required=True),
            username=dict(required=True),
            password=dict(required=True),
            enablePassword=dict(required=False),
            deviceType=dict(required=True),
            interfaceRange=dict(required=False),
            interfaceOption=dict(required=False),
            interfaceArg1=dict(required=True),
            interfaceArg2=dict(required=False),
            interfaceArg3=dict(required=False),
            interfaceArg4=dict(required=False),
            interfaceArg5=dict(required=False),
            interfaceArg6=dict(required=False),
            interfaceArg7=dict(required=False),),
        supports_check_mode=False)

    username = module.params['username']
    password = module.params['password']
    enablePassword = module.params['enablePassword']
    interfaceRange = module.params['interfaceRange']
    interfaceOption = module.params['interfaceOption']
    interfaceArg1= module.params['interfaceArg1']
    interfaceArg2 = module.params['interfaceArg2']
    interfaceArg3= module.params['interfaceArg3']
    interfaceArg4 = module.params['interfaceArg4']
    interfaceArg5 = module.params['interfaceArg5']
    interfaceArg6 = module.params['interfaceArg6']
    interfaceArg7 = module.params['interfaceArg7']
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
    if(interfaceOption == None or interfaceOption == ""):
        output = output + cnos_utility.interfaceConfig(remote_conn, deviceType, "(config)#", 2, None, interfaceRange, 
                                                     interfaceArg1, interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5,interfaceArg6, interfaceArg7)
    elif(interfaceOption == "ethernet"):
        output = output + cnos_utility.interfaceConfig(remote_conn, deviceType, "(config)#", 2, "ethernet", interfaceRange, 
                                                     interfaceArg1, interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5,interfaceArg6, interfaceArg7)
    elif(interfaceOption == "loopback"):
        output = output + cnos_utility.interfaceConfig(remote_conn, deviceType, "(config)#", 2, "loopback", interfaceRange, 
                                                     interfaceArg1, interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5,interfaceArg6, interfaceArg7)
    elif(interfaceOption == "mgmt"):
        output = output + cnos_utility.interfaceConfig(remote_conn, deviceType, "(config)#", 2, "mgmt", interfaceRange, 
                                                     interfaceArg1, interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5,interfaceArg6, interfaceArg7)
    elif(interfaceOption == "port-aggregation"):
        output = output + cnos_utility.interfaceConfig(remote_conn, deviceType, "(config)#", 2, "port-aggregation", interfaceRange, 
                                                     interfaceArg1, interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5,interfaceArg6, interfaceArg7)
    elif(interfaceOption == "vlan"):
        output = output + cnos_utility.interfaceConfig(remote_conn, deviceType, "(config)#", 2, "vlan", interfaceRange, 
                                                     interfaceArg1, interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5,interfaceArg6, interfaceArg7)
    else:
        output = "Invalid interface option \n"
    #Save it into the file
    file = open(outputfile, "a")
    file.write(output)
    file.close()
    
    # Logic to check when changes occur or not
    errorMsg = cnos_utility.checkOutputForError(output)
    if(errorMsg == None):
        module.exit_json(changed=True, msg="Interface Configuration is done")
    else:
        module.fail_json(msg=errorMsg)
    

if __name__ == '__main__':
        main()
                                   
