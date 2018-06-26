
# Sample Playbooks and Roles for support of Lenovo's CNOS and ENOS based networking devices in Ansible

## Overview

* Modules provide the basis for supporting basic switch management functions.
* Module Playbooks and Roles are samples showing how to use each of the Modules and must be tailored by the user to their environment.
* Playbooks and Roles are samples for showing how to use each modules. The values of variables used are typical to the lab test enviroment.  These must be tailored by the user to their environment.

### Requirements

* Ansible 2.6 installed.  [Ansible Installation Instructions](http://docs.ansible.com/ansible/intro_installation.html)
* Lenovo CNOS network device version 10.2.1.0 or later
* Lenovo switches running ENOS version 8.4.1.0 or later
* SSH enabled on the device

### How to Run it?

* Ansible 2.6 has to be installed first.
* Clone the ansible-cnos github to an appropriate location.(https://github.com/lenovo/ansible-cnos.git)
* Copy the necessary playbooks and roles to <anisble-install-directory>/test/integration
* The roles has to be in the "roles" folder not in the "targets" folder.
* The host file (/etc/ansible/hosts) has to be updated typically as given in sample host files.
* Edit the hosts file based on IP address/ Username / Password of their environment
* Exceute the playbooks from <anisble-install-directory>/test/integration using command 
  anisble-playbook <Your Sample Playbook.yml> -vvvv
  

## Documentation

Lenovo documentation can be found here:
[Lenovo Ansible Documentation](http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fansible_for_lenovo_networking.html&cp=0_3_1_0)

## License

* GPLv3
* Copyright (C) 2017 Lenovo, Inc.


