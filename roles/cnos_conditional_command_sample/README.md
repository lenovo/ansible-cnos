# Ansible Role: CNOS Switch command execution with inventory conditions - Sample

This role is an example on usage of module cnos_conditional_command.py in the context of CNOS configurations. This module can be used to execute any CLI command of the device of your choice. But here u have a facility to provide a condition on inventory whether this command should be executed on this device or not. You have to provide the same flag u employ in variables here from inventor for the command execution to happen or it will be skipped. Its your responsibility to be in the right context for the command to be succeeded. You can either directly give the command with the hardcoded value for it or you can specify the same through the vars/main.yml. This module does not provide any validations in the module and the execution  results from the device will be parsed for error conditions and will be present to the user. You can always look at the Results folder to know the status of your command run operation.

## Requirements

To provide a way to execute CLIs through a module based on conditions. This can be used in case you want to execute a CLI selectively on devices specified under a inventory tag.

## Role Variables

Available variables are listed below, along with description:

These are the mandatory inventory variables. 
1. username : User name for the switch
2. password: Password for the switch
3. enablePassword : Enable password for the switch. This is not a mandatory parameter.
4. hostname: Host name for this switch
5. deviceType : The type of device you are back up. At the moment we support Mars and Jupiter(G8272_cnos, G8296_cnos)
6. condition : The value of the condition should match with the value of flag for the successful command execution.
   Else it will be skipped.

These are the variables that need to be provided at the vars/main.yml
7. flag - The value of the flag should match with the conditional variable from inventory for execution 
8. clicommand - The CLI command that need to be executed on the device.



## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated switches for CLI command Configurations. You may refer to cnos_conditional_command_sample for a sample configuration. Its pasted below  as well for your convenience.
  
 [cnos_conditional_command_sample]
 10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos condition=pass
 10.241.107.40   username=<username> password=<password> deviceType=g8272_cnos 
    
  You should change all the Ip Addresses involved appropriately

 - cnos_conditional_command.py - this module has to come in the library folder of the role.
 - cnos_utility.py - this module has to come in the PYTHONPATH environment variable set in the Ansible system 

## Example Playbook

 - name: Module to  do some configurations
   hosts: cnos_conditional_command_sample
   gather_facts: no
   connection: local

   roles:
    - cnos_conditional_command_sample

## License
 
Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
