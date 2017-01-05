# Ansible Role: CNOS Switch Port Aggregation configurations - Sample

This role is an example on usage of module cnos_portchannel.py in the context of CNOS configurations. This module can be used to execute any portchannel configuration commands. Apart from many mandatory arguments there are a series of overloaded arguments which will help you to achieve all configuration tasks. Though we have covered many possible configuration cases in this example, still, please refer to the module documentation and samples to understand and utilize this module to its maximum. The value for the variables specified in the tasks can be provided through the vars/main.yml. You can always look at the Results folder to know the status of your command run operation.

## Requirements

To execute any interface-port-aggregation configurations on a CNOS switch.

## Role Variables

Available variables are listed below, along with description:

These are the mandatory inventory variables. 
1. username : User name for the switch
2. password: Password for the switch
3. enablePassword : Enable password for the switch. This is an optional parameter.
4. hostname: Host name for this switch
5. deviceType : The type of device you are back up. At the moment we support Mars and Jupiter(G8272_cnos, G8296_cnos)
6. interfaceRange - This specifies the interface range in which the port aggregation is envisaged

These are the variables that need to be provided at the vars/main.yml
7. interfaceArg1 - This is an overloaded port-channel first argument. Please refer to the module documentation 
				   for detailed description on usage. Value of these argument depends on the configuration context 
				   and choices are given below.
 			       choices: [aggregation-group, bfd, bridgeport, description, duplex, flowcontrol, ip, ipv6, 
 			       lacp, lldp, load-interval, mac, mac-address, mac-learn, microburst-detection, mtu, service,
 			       service-policy, shutdown, snmp, spanning-tree, speed, storm-control, vlan, vrrp, port-aggregation]
8. interfaceArg2 - This is an overloaded port-channel second argument. Please refer to the module documentation 
				   for detailed description on usage. Value of these argument depends on the configuration context 
				   and choices are given below.
              	   choices: [aggregation-group number, access or mode or trunk, description, auto or full or half,
        		   recieve or send, port-priority, suspend-individual, timeout,receive or transmit or 
        		   trap-notification, tlv-select, Load interval delay in seconds, counter, Name for the MAC Access
        		   List, mac-address in HHHH.HHHH.HHHH format, THRESHOLD  Value in unit of buffer cell, <64-9216>  
        		   MTU in bytes:<64-9216> for L2 packet,<576-9216> for L3 IPv4 packet, <1280-9216> for L3 IPv6 packet,
        		   enter the instance id, input or output, copp-system-policy, type, 1000  or  10000  or   40000 or
        		   auto, broadcast or multicast or unicast, disable or enable or egress-only, Virtual router 
        		   identifier, destination-ip or destination-mac or destination-port or source-dest-ip or
        		   source-dest-mac or source-dest-port or source-interface or source-ip or source-mac or source-port]
9. interfaceArg3 - This is an overloaded port-channel third argument. Please refer to the module documentation
                   for detailed description on usage. Value of these argument depends on the configuration context 
                   and choices are given below.
              	   choices: [active or on or passive, on or off, LACP port priority, long or short, 
              	   link-aggregation or mac-phy-status or management-address or max-frame-size or port-description 
              	   or port-protocol-vlan or port-vlan or power-mdi or protocol-identity or system-capabilities or
              	   system-description or system-name or vid-management or vlan-name, counter for load interval, 
              	   policy input name, all or Copp class name to attach, qos, queing, Enter the allowed traffic level,
              	   ipv6]
10. interfaceArg4 - This is an overloaded port channel fourth argument. Please refer to the module documentation 
					for detailed description on usage. Value of these argument depends on the configuration context
					and choices are given below.
                    choices: [key-chain, key-id, keyed-md5 or keyed-sha1 or meticulous-keyed-md5 or 
                    meticulous-keyed-sha1 or simple, Interval value in milliseconds, Destination IP (Both IPV4 
                    and IPV6),in or out, MAC address, Time-out value in seconds, 
                    class-id, request, Specify the IPv4 address, OSPF area ID as a decimal value, OSPF area ID in 
                    IP address format, anycast or secondary, ethernet, vlan, MAC (hardware) address in 
                    HHHH.HHHH.HHHH format, Load interval delay in seconds, Specify policy input name, 
                    input or output, cost, port-priority, BFD minimum receive interval,source-interface]
11. interfaceArg5 - This is an overloaded port channel fifth argument. Please refer to the module documentation
					for detailed description on usage. Value of these argument depends on the configuration context 
					and choices are given below.
              		choices: [name of key-chain,  key-Id Value, key-chain , key-id, BFD minimum receive interval, 
              		Value of Hello Multiplier, admin-down or multihop or non-persistent, Vendor class-identifier name, 
              		bootfile-name or host-name or log-server or ntp-server or tftp-server-name, Slot/chassis number, 
              		Vlan interface, Specify policy input name, Port path cost or auto, Port priority increments of 32]
12. interfaceArg6 - This is an overloaded port channel sixth argument. Please refer to the module documentation 
					for detailed description on usage. Value of these argument depends on the configuration context
					and choices are given below.
              		choices: [Authentication key string, name of key-chain, key-Id Value, Value of Hello Multiplier,
              		admin-down or non-persistent]
13. interfaceArg7 - This is an overloaded port channel seventh argument. Please refer to the module documentation 
					for detailed description on usage. Value of these argument depends on the configuration context
					and choices are given below.
              		choices: [Authentication key string, admin-down]

## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated switches for Port Aggregation configurations. You may refer to cnos_portchannel_sample for a sample configuration. Its pasted below  as well for your convenience.
  [cnos_portchannel_sample]
  10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos
  10.241.107.40   username=<username> password=<password> deviceType=g8272_cnos 
    
  You should change all the Ip Addresses involved appropriately
- cnos_portchannel.py - this module has to come in the library folder of the role.
- cnos_utility.py - this module has to come in the PYTHONPATH environment variable set in the Ansible system 

## Example Playbook

 - name: Module to  do Port Channel configurations
   hosts: cnos_portchannel_sample
   gather_facts: no
   connection: local

   roles:
    - cnos_portchannel_sample

## License
 
Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
