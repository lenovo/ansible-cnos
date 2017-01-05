# Ansible Role: VLAG Tier1 Leaf Configuration

This is a template driven configuration playbook for VLAG Tier 1 Leaf configuration.
This involves two Mars switches and are connected to each other at South side.
The templates used in this configurations are similiar but the value getting configured are very much different.
So there will be two set of values for the templates and each switch will get populated with its own values
This will enable the template to populate it in the run time before execution.
The module file with execute or skip the tasks given in the playbook depending on the flag given against each ip address.
The configuration commands and its results can be verified in the commands and results folder.

## Requirements

To configure a the VLAG Tier 1 Leaf configuration using a single template seamlessly using Ansible.

## Role Variables

Available variables are listed below, along with description:

1. username : User name for the switch
2. password: Password for the switch
3. stp_mode1: Spanning Tree operating mode
4. port_range:Specify a port-ranges 1
5. portchannel_interface_number1: Specify a port-channel number 1
6. portchannel_mode1: Specify Port Channel Mode
7. slot_chassis_number1: Specify Slot/Chassis Number 1
8. switchport_mode1: Enter the port mode


## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated
  as leaf1 and leaf2 switches. You may refer to vlag_1tier_leaf_hosts for a sample configuration. Its pasted below
  as well for your convineance.
  
  [vlag_1tier_leaf]
  10.240.178.74   username=<username> password=<password> deviceType=g8272_cnos condition=leaf_switch1
  10.240.178.75   username=<username> password=<password> deviceType=g8272_cnos condition=leaf_switch2
  
 You should change all the Ip Addresses involved appropriately

## Example Playbook

    - hosts: vlag_1tier_leaf
      roles:
        - vlag_1tier_leaf
## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
