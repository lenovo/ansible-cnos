# Ansible Role: CNOS Switch template execution - Sample

This role is an example on usage of module cnos_template.py in the context of CNOS configurations. This module can be used to execute any CLI template for the device of your choice. You have to be in the right context for the template to be succeeded. The module will take CLIs specified in template file, line by line and execute it. The value for the variables specified in the template can be provided through the vars/main.yml. This module does not provide any validations in the module and the execution  results from the device will be parsed for error conditions and will be present to the user. You can always look at the Results folder to know the status of your command run operation.

## Requirements

To provide a way to execute templates through a module. This can be used in case you want to execute a CLI template on devices specified under an inventory tag.

## Role Variables

Available variables are listed below, along with description:

These are the mandatory inventory variables. 
1. username : User name for the switch
2. password: Password for the switch
3. enablePassword : Enable password for the switch. This is an optional parameter.
4. hostname: Host name for this switch
5. deviceType : The type of device you are back up. At the moment we support Mars and Jupiter(G8272_cnos, G8296_cnos)

These are the variables that need to be provided at the vars/main.yml
6. commandfile - This is the path CNOS command file which need to be applied. This usually comes from the commands
             folder. Generally this file is the output of the variables applied on a template file


## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated switches for CLI template Configurations. You may refer to cnos_template_sample for a sample configuration. Its pasted below  as well for your convenience.
  [cnos_template_sample]
  10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos
  10.241.107.40   username=<username> password=<password> deviceType=g8272_cnos 
    
  You should change all the Ip Addresses involved appropriately
 - cnos_template.py - this module has to come in the library folder of the role.
 - cnos_utility.py - this module has to come in the PYTHONPATH environment variable set in the Ansible system 


## Example Playbook

 - name: Module to  do some template configurations
   hosts: cnos_template_sample
   gather_facts: no
   connection: local

   roles:
    - cnos_template_sample

## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
