# Ansible Role: clos_leaf_bgp_bfd - Clos Leaf BGP Configuration
---
<add role description below>

The configuration of the four leaf switches in the PoD for BGP in the Clos network consist of common variables that apply to all leaf switches and unique variables that apply to a specific leaf switch. Therefore multiple templates must be used on the leaf switches. 

For more details, see [Configuring a Clos Network using Ansible](http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fconfiguring_a_clos_network_using_ansible.html&cp=0_3_1_0_5).


## Requirements
---
<add role requirements information below>

- Ansible version 2.2 or later ([Ansible installation documentation](http://docs.ansible.com/ansible/intro_installation.html))
- Lenovo switches running CNOS version 10.2.1.0 or later
- an SSH connection to the Lenovo switch (SSH must be enabled on the network device)


## Role Variables
---
<add role variables information below>

The values of the template variables need to be modified to fit the specific scenario in which you are deploying the solution. To change the values of the variables, you need to visits the *vars* directory of each role and edit the *main.yml* file located there. The values stored in this file will be used by Ansible when the template is executed.

The syntax of *main.yml* file for variables is the following:

```
<template variable>:<value>
```

You will need to replace the `<value>` field with the value that suits your topology. The `<template variable>` fields are taken from the template and it is recommended that you leave them unchanged.

Available variables are listed below, along with description:

Common Variables | Description
--- | ---
`username` | Specifies the username used to log into the switch
`password` | Specifies the password used to log into the switch
`hostname` | Specifies the hostname of the switch to connect to
`stpmode` | Configures the STP mode (**mst** - MSTP, **rapid-pvst** - Rapid PVST+, **disable** - STP is disabled) for all leaf switches
`stpmst` | STP MST value for all leaf switches

Switch-specific Variables | Description
--- | ---
`flag` | Conditional flag specifying which leaf switch the unique variables should be applied to
`leaf_to_spine1_interface1` | Specifies the first ethernet port (*slot number/port number*) connected to spine switch 1
`leaf_to_spine1_description1` | Configures the description of the first port connected to spine switch 1 (maximum of 80 characters)
`leaf_to_spine1_ip1` | Configures the IP address (*IPv4 or IPV6 address/prefix length*) of the first port  connected to spine switch 1
`leaf_to_spine1_interface2` | Specifies the second ethernet port (*slot number/port number*) connected to spine switch 1
`leaf_to_spine1_description2` | Configures the description of the second port connected to spine switch 1 (maximum of 80 characters)
`leaf_to_spine1_ip2` | Configures the IP address (*IPv4 or IPV6 address/prefix length*) of the second port connected to spine switch 1
`leaf_to_spine2_interface1` | Specifies the first ethernet port (*slot number/port number*) connected to spine switch 2
`leaf_to_spine2_description1` | Configures the description of the first port connected to spine switch 2 (maximum of 80 characters)
`leaf_to_spine2_ip1` | Configures the IP address (*IPv4 or IPV6 address/prefix length*) of the first port connected to spine switch 2
`leaf_to_spine2_interface2` | Specifies the second ethernet port (*slot number/port number*) connected to spine switch 2
`leaf_to_spine2_description2` | Configures the description of the second port connected to spine switch 2 (maximum of 80 characters)
`leaf_to_spine2_ip2` | Configures the IP address (*IPv4 or IPV6 address/prefix length*) of the second port connected to spine switch 2
`router_as_number` | Configures the router Autonomous System (AS) Number (*1-4294967295*)
`router_multipath_number` | Configures the router multipath number
`neighbor_ad_interval` | Configures the neighbor advertisement interval (*0-65535* seconds)
`neighbor_address1` | Specifies the neighbor IP address (*IPv4 or IPV6 address/prefix length*) of spine 1 connected to port 1
`neighbor_address2` | Specifies the neighbor IP address (*IPv4 or IPV6 address/prefix length*) of spine 1 connected to port 2
`neighbor_address3` | Specifies the neighbor IP address (*IPv4 or IPV6 address/prefix length*) of spine 2 connected to port 1
`neighbor_address4` | Specifies the spine neighbor IP address (*IPv4 or IPV6 address/prefix length*) spine 2 connected to port 2


## Dependencies
---
<add dependencies information below>

- username.iptables - Configures the firewall and blocks all ports except those needed for web server and SSH access.
- username.common - Performs common server configuration.
- /etc/ansible/hosts - You must edit the */etc/ansible/hosts* file with the device information of the Clos Leaf BGP switches. You may refer to *clos_leaf_bgp_bfd_hosts* for a sample configuration.

Ansible keeps track of all network elements that it manages through a hosts file. Before the execution of a playbook, the hosts file must be set up.

Open the */etc/ansible/hosts* file with root privileges. Most of the file is commented out by using **#**. You can also comment out the entries you will be adding by using **#**. You need to copy the content of the hosts file for the role into the */etc/ansible/hosts* file. The sample hosts file for the role is located in the main directory.

```
[clos_leaf_bgp_bfd]
10.240.175.211   username=<username> password=<password> deviceType=g8272_cnos
10.240.175.212   username=<username> password=<password> deviceType=g8272_cnos
10.240.175.213   username=<username> password=<password> deviceType=g8272_cnos
10.240.175.214   username=<username> password=<password> deviceType=g8272_cnos
```
**Note:** You need to change the IP addresses to fit your specific topology. You also need to change the `<username>` and `<password>` to the appropriate values used to log into the specific Lenovo network devices.


## Example Playbook
---
<add playbook samples below>

To execute an Ansible playbook, use the following command:

```
ansible-playbook clos_leaf_bgp_bfd.yml -vvv
```

`-vvv` is an optional verbos command that helps identify what is happening during playbook execution. The playbook for each role of the Clos network configuration solution is located in the main directory of the solution.

```
- hosts: clos_leaf_bgp_bfd
  roles:
    - clos_leaf_bgp_bfd
```


## License
---
<add license information below>
Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the [GNU General Public License](http://www.gnu.org/licenses/) for more details.