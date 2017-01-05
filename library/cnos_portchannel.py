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
module: cnos_portchannel
short_description: Performs all configurations on switches pertaining to Port Aggregation.
description: 
    - Manages network device configurations over SSH. This module allows implementors to work with the 
    Port Channel (Port Aggregation) configurations. The operators here are overloaded to take care of all 
    configurations pertaining to portchannel . Apart from the regular device connection related attributes 
    there are 5 PortChannel Arguments which are overloaded to achieve all configurations. They are interfaceArg1, 
    interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5 respectively. Port Channel configurations are taken care 
    at two contexts in a regular CLI. We have to go into interface > port-aggregation to configure the 
    interface port channel parameters. This can be done for a range as well as individual port-aggregations 
    as well. The second context of port channel configurations are in the general configuration pertaining to 
    load balancing. first set of configuration comes in context "(config-if)#" or "(config-if-range)#" while 
    the other comes in "(config)#".Please see the example section to understand more how to use this 
    overloaded functions. Results of the backup operation can be viewed in results folder.
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
            - The value of password is used to enter the congig mode.The default value is empty string. The value has to come from inventory file ideally,
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
    interfaceRange:
        description:
            - This specifies the interface range in which the port aggregation is envisaged
        required: Yes
        default: null
        choices: []
    
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

Please find below the table with option how the overloaded variables are used in the context of Port Channel. 
There are 2 places where portchannel configurations are happening. First one is inside context of interface and 
other one in general configuration  mode. The second mode will always start with portCh1 argument as "portaggregation".

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
    1. cnos_portchannel.py
    2. cnos_utility.py 
'''
EXAMPLES = '''
The task/main.yml will look like this
---
- name: Test Port Channel - aggregation-group
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data1}}"
 
- name: Test Port Channel - aggregation-group - Interface Range
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data24}}"

- name: Test Port Channel - bridge-port
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt  interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data2}}"

- name: Test Port Channel - bridgeport mode
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data3}}"

- name: Test Port Channel  - Description
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_portchannel_data4}}"

- name: Test Port Channel - Duplex
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_portchannel_data5}}"

- name: Test Port Channel - flowcontrol
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data6}}"

- name: Test Port Channel - lacp
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data7}}"

- name: Test Port Channel  - lldp
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data8}}"

- name: Test Port Channel - load-interval
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}' interfaceArg4='{{item.interfaceArg4}}'
  with_items: "{{test_portchannel_data9}}"

#- name: Test Port Channel - mac
#  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
#  with_items: "{{test_portchannel_data10}}"

- name: Test Port Channel - microburst-detection
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_portchannel_data11}}"

- name: Test Port Channel  - mtu
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_portchannel_data12}}"

- name: Test Port Channel - service-policy
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data13}}"

- name: Test Port Channel - speed
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_portchannel_data14}}"

- name: Test Port Channel - storm
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data15}}"

#- name: Test Port Channel - vlan
#  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
#  with_items: "{{test_portchannel_data16}}"

- name: Test Port Channel - vrrp
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}'
  with_items: "{{test_portchannel_data17}}"

- name: Test Port Channel - spanning tree1
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data18}}"

- name: Test Port Channel - spanning tree 2
  cnos_portchannel: host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}' interfaceArg4='{{item.interfaceArg4}}' interfaceArg5='{{item.interfaceArg5}}'
  with_items: "{{test_portchannel_data19}}"

- name: Test Port Channel - ip1
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}' interfaceArg4='{{item.interfaceArg4}}'
  with_items: "{{test_portchannel_data20}}"

- name: Test Port Channel - ip2
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}'
  with_items: "{{test_portchannel_data21}}"

- name: Test Port Channel - bfd
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}' interfaceArg4='{{item.interfaceArg4}}' interfaceArg5='{{item.interfaceArg5}}'
  with_items: "{{test_portchannel_data22}}"

- name: Test Port Channel - bfd
  cnos_portchannel:  host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_portchannel_{{ inventory_hostname }}_output.txt interfaceRange='{{item.interfaceRange}}' interfaceArg1='{{item.interfaceArg1}}' interfaceArg2='{{item.interfaceArg2}}' interfaceArg3='{{item.interfaceArg3}}' interfaceArg4='{{item.interfaceArg4}}' interfaceArg5='{{item.interfaceArg5}}' interfaceArg6='{{item.interfaceArg6}}'
  with_items: "{{test_portchannel_data23}}"

In the vars/main.yml will look like this
---
test_portchannel_data1:
  - {interfaceRange: 33, interfaceArg1: "aggregation-group", interfaceArg2: 33, interfaceArg3: "on"}
test_portchannel_data2:
  - {interfaceRange: 33, interfaceArg1: "bridge-port", interfaceArg2: "access", interfaceArg3: 33}
test_portchannel_data3:
  - {interfaceRange: 33, interfaceArg1: "bridge-port", interfaceArg2: "mode", interfaceArg3: "access"}
test_portchannel_data4:
  - {interfaceRange: 33, interfaceArg1: "description", interfaceArg2: "Hentammoo "}
test_portchannel_data5:
  - {interfaceRange: 33, interfaceArg1: "duplex", interfaceArg2: "auto"}
test_portchannel_data6:
  - {interfaceRange: 33, interfaceArg1: "flowcontrol", interfaceArg2: "send", interfaceArg3: "off"}
test_portchannel_data7:
  - {interfaceRange: 33, interfaceArg1: "lacp", interfaceArg2: "port-priority", interfaceArg3: 33}
test_portchannel_data8:
  - {interfaceRange: 33, interfaceArg1: "lldp", interfaceArg2: "tlv-select", interfaceArg3: "max-frame-size"}
test_portchannel_data9:
  - {interfaceRange: 33, interfaceArg1: "load-interval", interfaceArg2: "counter", interfaceArg3: 2,interfaceArg4: 33 }
test_portchannel_data10:
  - {interfaceRange: 33, interfaceArg1: "mac", interfaceArg2: "copp-system-acl-vlag-hc"}
test_portchannel_data11:
  - {interfaceRange: 33, interfaceArg1: "microburst-detection", interfaceArg2: 25}
test_portchannel_data12:
  - {interfaceRange: 33, interfaceArg1: "mtu", interfaceArg2: 66}
test_portchannel_data13:
  - {interfaceRange: 33, interfaceArg1: "service-policy", interfaceArg2: "input", interfaceArg3: "Anil"}
test_portchannel_data14:
  - {interfaceRange: 33, interfaceArg1: "speed", interfaceArg2: "auto"}
test_portchannel_data15:
  - {interfaceRange: 33, interfaceArg1: "storm-control", interfaceArg2: "broadcast", interfaceArg3: 12.5 }
test_portchannel_data16:
  - {interfaceRange: 33, interfaceArg1: "vlan", interfaceArg2: "disable"}
test_portchannel_data17:
  - {interfaceRange: 33, interfaceArg1: "vrrp", interfaceArg2: 33}
test_portchannel_data18:
  - {interfaceRange: 33, interfaceArg1: "spanning-tree", interfaceArg2: "bpduguard", interfaceArg3: "enable"}
test_portchannel_data19:
  - {interfaceRange: 33, interfaceArg1: "spanning-tree", interfaceArg2: "mst", interfaceArg3: "33-35", interfaceArg4: "cost", interfaceArg5: 33}
test_portchannel_data20:
  - {interfaceRange: 33, interfaceArg1: "ip", interfaceArg2: "access-group", interfaceArg3: "anil", interfaceArg4: "in"}
test_portchannel_data21:
  - {interfaceRange: 33, interfaceArg1: "ip", interfaceArg2: "port", interfaceArg3: "anil" }
test_portchannel_data22:
  - {interfaceRange: 33, interfaceArg1: "bfd", interfaceArg2: "interval", interfaceArg3: 55, interfaceArg4: 55, interfaceArg5: 33}
test_portchannel_data23:
  - {interfaceRange: 33, interfaceArg1: "bfd", interfaceArg2: "ipv4", interfaceArg3: "authentication", interfaceArg4: "meticulous-keyed-md5", interfaceArg5: "key-chain", interfaceArg6: "mychain"}
test_portchannel_data24:
- {interfaceRange: "1/1-2", interfaceArg1: "aggregation-group", interfaceArg2: 33, interfaceArg3: "on"}

In the inventory file u specify like this
[cnos_portchannel_sample]
10.241.107.39  username=<username> password=<password> deviceType=g8272_cnos
10.241.107.40  username=<username> password=<password> deviceType=g8272_cnos

'''

RETURN = '''

On successful execution, the method returns and empty string with a message "Port Channel configurations 
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
    interfaceRange= module.params['interfaceRange']
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
    if(interfaceArg1 == "port-aggregation"):
        output = output + cnos_utility.portChannelConfig(remote_conn, deviceType, "(config)#", 2, interfaceArg1, 
                                                           interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5, interfaceArg6, interfaceArg7)
    else :
        output = output + cnos_utility.interfaceConfig(remote_conn, deviceType, "(config)#", 2, "port-aggregation", interfaceRange, 
                                                     interfaceArg1, interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5,interfaceArg6, interfaceArg7)
    
    #Save it into the file
    file = open(outputfile, "a")
    file.write(output)
    file.close()
    
    # Logic to check when changes occur or not
    errorMsg = cnos_utility.checkOutputForError(output)
    if(errorMsg == None):
        module.exit_json(changed=True, msg="Port Aggregation configuration is done")
    else:
        module.fail_json(msg=errorMsg)
    

if __name__ == '__main__':
        main()
                                   
