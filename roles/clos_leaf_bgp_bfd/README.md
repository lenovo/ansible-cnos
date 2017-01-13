# Ansible Role: CLOS Leaf BGP Configuration

Thee configuration is common to all the leaf switches for BGP in the CLOS configuration.
Hence only one template applies to both with same values as specified below.

## Requirements

To configure a the CLOS Leaf BGP Switches configuration using a single template seamlessly using Ansible.

## Role Variables

Available variables are listed below, along with description:

1. username : User name for the switch
2. password: Password for the switch
3. hostname: Host name for this switch
4. stpmpode: STP Mode value
5. vlanid1: VLAN Id 1
6. stpmst : STP MST value
7. slot_chassis_number1: Specify Slot/Chassis Number 1
8. interface_description1 : Interface Description 1
9. interface_ip_addr1: Interface Ip Address 1
10. slot_chassis_number2 : Specify Slot/Chassis Number 2
11. interface_ip_addr2:Interface Ip Address 2
12. interface_description2 : Interface Description 2
13. slot_chassis_number3: Specify Slot/Chassis Number 3
14. interface_ip_addr3:Interface Ip Address 3
15. slot_chassis_number4: Specify Slot/Chassis Number 4
16. interface_ip_addr4:Interface Ip Address 4
17. slot_chassis_number5: Specify Slot/Chassis Number 5
18. interface_description3 : Interface Description 3
19. interface_ip_addr5:Interface Ip Address 5
20. interface_ip_addr6:Interface Ip Address 6
21. router_as_number1: Router AS Number
22. router_multipath_number1: Router Multipath Number
23. neighbor_address1: Neighbor address 1
24. neighbor_as_number1: Neighbor AS Number 1
25. neighbor_ad_interval1: Neighbour advertisement interval
26. neighbor_address2: Neighbor address 2
27. neighbor_as_number2: Neighbor AS Number 2
28. neighbor_address3: Neighbor address 3
29. neighbor_address4: Neighbor address 4
30. neighbor_address5: Neighbor address 5
31. ip_dest_prefix1: IP Destination Prefix 1
32. mgmt_int_number: Management Interface Number
33. ip_gateway_addr: IP Gateway Address.

## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated
  as CLOS Leaf BGP switches. You may refer to clos_leaf_bgp_hosts for a sample configuration. Its pasted below
  as well for your convineance.
  [clos_leaf_bgp_bfd]
  10.240.175.211   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.212   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.213   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.214   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.231   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.232   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.233   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.234   username=<username> password=<password> deviceType=g8272_cnos
  
  You should change all the Ip Addresses involved appropriately


## Example Playbook

    - hosts: clos_leaf_bgp_bfd
      roles:
        - clos_leaf_bgp_bfd

## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
