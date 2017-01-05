# Ansible Role: VLAG Tier2 Spine Configuration

This is a template driven configuration playbook for VLAG Tier 2 Spine configuration.
This involves four Mars switches and are connected to each other in a North south orientation.
Here configurations are similiar in the North side and South side of Spine configuration except
except the peer ip configuration details. Therefore there will be two set of data/vars for each pair
of switches. This data switching is achieved using a flag specified in /etc/ansible/host file as
condition. It has value north and south depending on the topology location for each switches.
Peer ip has to be specified for each spine switches in the /etc/anisble/hosts file with tag id peerip
This will enable the template to populate it in the run time before execution.
The configuration commands and its results can be verified in the commands and results folder.

## Requirements

To configure the VLAG Tier 2 Spine configuration using a single template seamlessly using Ansible.

## Role Variables
Available variables are listed below, along with description:


1. username : User name for the switch
2. password: Password for the switch
3. slot_chassis_number1: Specify Slot/chassis number 1
4. portchannel_interface_number1:Specify a port-channel number 1
5. portchannel_mode1 : Specify channeling mode
6. slot_chassis_number2: Specify Slot/Chassis Number 2
7. portchannel_interface_number2:Specify a port-channel number 2
8. slot_chassis_number3: Specify Slot/Chassis Number 3
9. portchannel_interface_number3: Specify a port-channel number 3
10. slot_chassis_number4: Specify Slot/Chassis Number 4
11. portchannel_interface_number4: Specify a port-channel number 4
12. switchport_mode1: Enter the port mode
13. slot_chassis_number5: Specify Slot/Chassis Number 5
14. stp_mode1: Spanning Tree operating mode
15. vlag_tier_id1: VLAG tier-id value
16. vlag_instance_number1: Port-channel interface identifier 1
17. vlag_instance_number2: Port-channel interface identifier 2
18. vlag_instance_number3: Port-channel interface identifier 3

## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated
  as north spine and south spine switches. You may refer to vlag_2tier_spine_hosts for a sample configuration. Its pasted below
  as well for your convineance.

  [vlag_2tier_spine]
  10.240.178.76   username=<username> password=<password> deviceType=g8272_cnos condition=north peerip=10.240.178.77
  10.240.178.77   username=<username> password=<password> deviceType=g8272_cnos condition=north peerip=10.240.178.76
  10.240.178.78   username=<username> password=<password> deviceType=g8272_cnos condition=south peerip=10.240.178.79
  10.240.178.79   username=<username> password=<password> deviceType=g8272_cnos condition=south peerip=10.240.178.78
  
  You should change all the Ip Addresses involved appropriately

## Example Playbook

    - hosts: vlag_2tier_spine
      roles:
        - vlag_2tier_spine
## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
