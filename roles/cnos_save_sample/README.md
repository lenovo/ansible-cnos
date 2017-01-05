# Ansible Role: CNOS Switch Save running-config to startup-config - Sample

This role is an example on usage of module cnos_save.py in the context of CNOS configurations. The typical use of this module come in saving of the running configuration to start-up configuration. This will make sure that the present running configuration will be intact even if u restart the device. You can always look at the Results folder to know the status of your save operation.

## Requirements

To copy the running configuration to startup configuration of a CNOS switch.

## Role Variables

Available variables are listed below, along with description:

These are the mandatory inventory variables. 
1. username : User name for the switch
2. password: Password for the switch
3. enablePassword : Enable password for the switch. This is not a mandatory parameter.
4. hostname: Host name for this switch
5. deviceType : The type of device you are back up. At the moment we support Mars and Jupiter(G8272_cnos, G8296_cnos)


## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated switches for saving running-config to start up configurations. You may refer to cnos_save_sample for a sample configuration. Its pasted below  as well for your convenience.
  [cnos_save_sample]
  10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos
  10.241.107.40   username=<username> password=<password> deviceType=g8272_cnos 
    
  You should change all the Ip Addresses involved appropriately
  
 - cnos_save.py - this module has to come in the library folder of the role.
 - cnos_utility.py - this module has to come in the PYTHONPATH environment variable set in the Ansible system 

## Example Playbook

 - name: Module to  do save configurations
   hosts: cnos_save_sample
   gather_facts: no
   connection: local

   roles:
    - cnos_save_sample

## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
