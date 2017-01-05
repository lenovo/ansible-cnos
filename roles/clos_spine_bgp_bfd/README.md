
# Ansible Role: CLOS Spine BGP Configuration

These configuration is common to all the Spine switches for BGP in the CLOS configuration.
Hence only one template applies to both with same values as specified below.

# Requirements

To configure a the CLOS Spine BGP Switches configuration using a single template seamlessly using Ansible.

## Role Variables

       
Available variables are listed below, along with description:

1. username : User name for the switch
2. password: Password for the switch
3. hostname: Host name for this switch
4. stpmpode: STP Mode value
5. vlanid1: VLAN Id 1
6. stpmst : STP MST value
7. slot_chassis_number1: Specify Slot/Chassis Number 1
8. process_id1: Process Id 1
9. area_id1: Area Id 1
10. interface_ip_addr1: Interface Ip Address 1
11. slot_chassis_number2 : Specify Slot/Chassis Number 2
12. interface_ip_addr2:Interface Ip Address 2
13. interface_description2 : Interface Description 2
14. slot_chassis_number3: Specify Slot/Chassis Number 3
15. interface_ip_addr3:Interface Ip Address 3
16. slot_chassis_number4: Specify Slot/Chassis Number 4
17. interface_ip_addr4:Interface Ip Address 4
18. slot_chassis_number5: Specify Slot/Chassis Number 5
19. slot_chassis_number6: Specify Slot/Chassis Number 6
20. interface_description3 : Interface Description 3
21. interface_ip_addr5:Interface Ip Address 5
22. interface_ip_addr6:Interface Ip Address 6
23. slot_chassis_number7: Specify Slot/Chassis Number 7
24. slot_chassis_number8: Specify Slot/Chassis Number 8
25. interface_ip_addr7: Interface Ip Address 7
26. slot_chassis_number9: Specify Slot/Chassis Number 9
27. interface_ip_addr8: Interface Ip Address 8
28. slot_chassis_number10: Specify Slot/Chassis Number 10
29. interface_ip_addr9: Interface Ip Address 9
30. slot_chassis_number11: Specify Slot/Chassis Number 11
31. interface_ip_addr10: Interface Ip Address 10
32. interface_ip_addr11: Interface Ip Address 11
33. router_id: Router Id
34. router_as_number1: Router AS Number 1
35. router_multipath_number1: Router Multipath Number 1
36. neighbor_address1: Neighbor address 1
37. neighbor_as_number1: Neighbor AS Number 1
38. neighbor_ad_interval1: Neighbour advertisement interval
39. neighbor_address2: Neighbor address 2
40. neighbor_as_number2: Neighbor AS Number 2
41. neighbor_address3: Neighbor address 3
42. neighbor_address4: Neighbor address 4
43. neighbor_address5: Neighbor address 5
44. neighbor_address6: Neighbor address 6
45. neighbor_address7: Neighbor address 7
46. neighbor_as_number4: Neighbor AS Number 4
47. neighbor_address8: Neighbor address 8
48. neighbor_address9: Neighbor address 9
49. neighbor_as_number5: Neighbor AS Number 5
50. neighbor_address10: Neighbor address 10
51. ip_dest_prefix1: IP Destination Prefix 1
52. mgmt_int_number: Management Interface Number
53. ip_gateway_addr: IP Gateway Address.

## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated
  as CLOS Spine BGP switches. You may refer to clos_spine_bgp_bfd_hosts for a sample configuration. Its pasted below
  as well for your convineance.
  [clos_spine_bgp_bfd]
  10.240.175.111   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.112   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.131   username=<username> password=<password> deviceType=g8272_cnos
  10.240.175.132   username=<username> password=<password> deviceType=g8272_cnos


## Example Playbook

    - hosts: clos_spine_bgp_bfd
      roles:
        - clos_spine_bgp_bfd

## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
