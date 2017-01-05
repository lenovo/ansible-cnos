# Ansible Role: CNOS Switch VLAG configurations - Sample

This role is an example on usage of module cnos_vlag.py in the context of CNOS configurations. This module can be used to execute any vlag configuration commands. Apart from many mandatory arguments there are a series of overloaded arguments which will help you to achieve all configuration tasks. Though we have covered many possible configuration cases in this example, still, please refer to the module documentation and samples to understand and utilize this module to its maximum. The value for the variables specified in the tasks can be provided through the vars/main.yml. You can always look at the Results folder to know the status of your command run operation.

## Requirements

To execute any vlag configurations on a CNOS switch.

## Role Variables

Available variables are listed below, along with description:

These are the mandatory inventory variables. 
1. username : User name for the switch
2. password: Password for the switch
3. enablePassword : Enable password for the switch. This is an optional parameter.
4. hostname: Host name for this switch
5. deviceType : The type of device you are back up. At the moment we support Mars and Jupiter(G8272_cnos, G8296_cnos)

These are the variables that need to be provided at the vars/main.yml
6. vlagArg1 - This is an overloaded vlag first argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
 			  choices: [enable,auto-recovery,config-consistency,isl,mac-address-table, peer-gateway, priority, 
 			  startup-delay, tierid,vrrp,instance,hlthchk]
7. vlagArg2 - This is an overloaded vlag second argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
              choices: [Interval in seconds,disable or strict,Port Aggregation Number,VLAG priority,
              Delay time in seconds,VLAG tier-id value, VLAG instance number, keepalive-attempts, keepalive-interval,
              retry-interval,peer-ip]
8. vlagArg3 - This is an overloaded vlag third argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
              choices: [enable or port-aggregation,Number of keepalive attempts,Interval in seconds,Interval in 
              seconds,VLAG health check peer IP4 address]
9. vlagArg4 - This is an overloaded vlag fourth argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
              choices: [Port Aggregation Number,default or management]

## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated switches for VLAG configurations. You may refer to cnos_vlag_sample for a sample configuration. Its pasted below  as well for your convenience.
  [cnos_vlag_sample]
  10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos
  10.241.107.40   username=<username> password=<password> deviceType=g8272_cnos 
    
  You should change all the Ip Addresses involved appropriately
 - cnos_vlag.py - this module has to come in the library folder of the role.
 - cnos_utility.py - this module has to come in the PYTHONPATH environment variable set in the Ansible system 


## Example Playbook

 - name: Module to  do VLAG configurations
   hosts: cnos_vlag_sample
   gather_facts: no
   connection: local

   roles:
    - cnos_vlag_sample

## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
