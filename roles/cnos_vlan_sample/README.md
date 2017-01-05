# Ansible Role: CNOS Switch VLAN configurations - Sample

This role is an example on usage of module cnos_vlan.py in the context of CNOS configurations. This module can be used to execute any vlan configuration commands. Apart from many mandatory arguments there are a series of overloaded arguments which will help you to achieve all configuration tasks. Though we have covered many possible configuration cases in this example, still, please refer to the module documentation and samples to understand and utilize this module to its maximum. The value for the variables specified in the tasks can be provided through the vars/main.yml. You can always look at the Results folder to know the status of your command run operation.

## Requirements

To execute any vlan configurations on a CNOS switch.

## Role Variables

Available variables are listed below, along with description:

These are the mandatory inventory variables. 
1. username : User name for the switch
2. password: Password for the switch
3. enablePassword : Enable password for the switch. This is an optional parameter.
4. hostname: Host name for this switch
5. deviceType : The type of device you are back up. At the moment we support Mars and Jupiter(G8272_cnos, G8296_cnos)

These are the variables that need to be provided at the vars/main.yml
6. vlanArg1 - This is an overloaded vlan first argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
 			  choices: [access-map, dot1q, filter, <1-3999> VLAN ID 1-3999 or range]
7. vlanArg2 - This is an overloaded vlan second argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
              choices: [VLAN Access Map name,egress-only,name, flood,state, ip]
8. vlanArg3 - This is an overloaded vlan third argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
              choices: [action, match, statistics, enter VLAN id or range of vlan, ascii name for the VLAN, 
              ipv4 or ipv6, active or suspend, fast-leave, last-member-query-interval, mrouter, querier, 
              querier-timeout, query-interval, query-max-response-time, report-suppression, robustness-variable,
              startup-query-count, startup-query-interval, static-group]
9. vlanArg4 - This is an overloaded vlan fourth argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
              choices: [drop or forward or redirect, ip or mac,Interval in seconds,ethernet, port-aggregation, 
              Querier IP address, Querier Timeout in seconds, Query Interval in seconds, 
              Query Max Response Time in seconds,  Robustness Variable value, Number of queries sent at startup, 
              Query Interval at startup]
10. vlanArg5 - This is an overloaded vlan fifth argument. Please refer to the module documentation for detailed 
              description on usage. Value of these argument depends on the configuration context and choices are 
              given below.
              choices: [access-list name, Slot/chassis number, Port Aggregation Number]

## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated switches for VLAN configurations. You may refer to cnos_vlan_sample for a sample configuration. Its pasted below  as well for your convenience.
  [cnos_vlan_sample]
  10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos
  10.241.107.40   username=<username> password=<password> deviceType=g8272_cnos 
    
  You should change all the Ip Addresses involved appropriately
  
 - cnos_vlan.py - this module has to come in the library folder of the role.
 - cnos_utility.py - this module has to come in the PYTHONPATH environment variable set in the Ansible system 


## Example Playbook

 - name: Module to do VLAN configurations
   hosts: cnos_vlan_sample
   gather_facts: no
   connection: local

   roles:
    - cnos_vlan_sample

## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
