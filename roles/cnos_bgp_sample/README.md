# Ansible Role: CNOS Switch BGP Configuration Sample

This role is an example on usage of module cnos_bgp.py in the context of CNOS configurations. This module can be used to execute bgp configuration commands. But we are still to realize neighbor configurations inside bgp. Apart from many mandatory arguments there are a series of overloaded arguments which will help you to achieve all configuration tasks. Though we have covered many possible BGP configuration cases in this example, still, please refer to the module documentation and samples to understand and utilize this module to its maximum. The value for the variables specified in the tasks can be provided through the vars/main.yml. You can always look at the Results folder to know the status of your command run operation.

## Requirements

To execute any bgp configurations on a CNOS switch.

## Role Variables

Available variables are listed below, along with description:

These are the mandatory inventory variables. 
1. username : User name for the switch
2. password: Password for the switch
3. enablePassword : Enable password for the switch. This is an optional parameter.
4. hostname: Host name for this switch
5. deviceType : The type of device you are back up. At the moment we support Mars and Jupiter(G8272_cnos, G8296_cnos)
6. asNum - AS number

These are the variables that need to be provided at the vars/main.yml
7. bgpArg1 - This is an overloaded bgp first argument. Please refer to the module documentation 
		     for detailed description on usage. Value of these argument depends on the configuration context 
			 and choices are given below.
 			 choices: [address-family, bestpath, bgp, cluster-id, confederation, enforce-first-as,
 			 fast-external-failover, graceful-restart,  graceful-restart-helper, log-neighbor-changes,
 			 maxas-limit, neighbor,router-id,shutdown, synchronization,timers,vrf]
9. bgpArg2 - This is an overloaded bgp second argument. Please refer to the module documentation 
			 for detailed description on usage. Value of these argument depends on the configuration context 
			 and choices are given below.
             choices: [always-compare-med, compare-confed-aspath, compare-routerid, dont-compare-originator-id,
             tie-break-on-age, as-path,med,identifier,peers]
10. bgpArg3 - This is an overloaded bgp third argument. Please refer to the module documentation
              for detailed description on usage. Value of these argument depends on the configuration context 
              and choices are given below.
              choices: [ignore or multipath-relax, confed or missing-as-worst or non-deterministic or
              remove-recv-med or remove-send-med]
11. bgpArg4 - This is an overloaded bgp fourth argument. Please refer to the module documentation 
			  for detailed description on usage. Value of these argument depends on the configuration context
			  and choices are given below.
              choices: [TBD]
12. bgpArg5 - This is an overloaded bgp fifth argument. Please refer to the module documentation
			  for detailed description on usage. Value of these argument depends on the configuration context 
			  and choices are given below.
              choices: [TBD]
12. bgpArg6 - This is an overloaded bgp sixth argument. Please refer to the module documentation 
			  for detailed description on usage. Value of these argument depends on the configuration context
			  and choices are given below.
              choices: [TBD]
13. bgpArg7 - This is an overloaded bgp seventh argument. Please refer to the module documentation 
			  for detailed description on usage. Value of these argument depends on the configuration context
			  and choices are given below.
              choices: [TBD]
13. bgpArg8 - This is an overloaded bgp eighth argument. Please refer to the module documentation 
			  for detailed description on usage. Value of these argument depends on the configuration context
			  and choices are given below.
              choices: [TBD]


## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated switches for BGP Configurations. You may refer to cnos_bgp_sample for a sample configuration. Its pasted below as well for your convenience.
  [cnos_bgp_sample]
  10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos
  10.241.107.40   username=<username> password=<password> deviceType=g8272_cnos
  
  You should change all the Ip Addresses involved appropriately
  
 - cnos_bgp.py - this module has to come in the library folder of the role.
 - cnos_utility.py - this module has to come in the PYTHONPATH environment variable set in the Ansible system


## Example Playbook

- name: Module to do BGP configuration
   hosts: cnos_bgp_sample
   gather_facts: no
   connection: local

   roles:
    - cnos_bgp_sample

## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
