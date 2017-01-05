# Ansible Role: CNOS Switch Image Download - Sample

This role is an example on usage of module cnos_image.py in the context of CNOS configurations. The typical use of this module come in downloading image on to the device. In this context, users have the choice of various protocols in uploading the configurations to the servers. Users can use TFTP, FTP , SFTP or SCP in the back up process. You can always look at the Results folder to know the status of your backup operation.

## Requirements

To download image on to a CNOS switch from an SFTP/SCP/FTP/TFTP server.

## Role Variables

Available variables are listed below, along with description:

These are the mandatory inventory variables. 
1. username : User name for the switch
2. password: Password for the switch
3. enablePassword : Enable password for the switch. This is not a mandatory parameter.
4. hostname: Host name for this switch
5. deviceType : The type of device you are back up. At the moment we support Mars and Jupiter(G8272_cnos, G8296_cnos)
6. imgpath - This specifies the absolute path of the image file located in the server. In case you are using 
            the relative path as the variable value, you need to specify the root folder for the user of the 
            server which u have specified. 

These are the variables that need to be provided at the vars/main.yml
7. imgType - Image type which you indent to download. The choices for you are 
            - all   Both Uboot and OS
            - boot  Uboot only
            - onie  ONIE image
            - os    OS only 
                The values expected are 1. running-config and startup-config
8. protocol - The protocol which your server would like to interract with device. This include SFTP/SCP/FTP/TFTP
9. serverip - IP address of the SFTP/SCP/FTP/TFTP serve of your choice
10. serverusername - The username, preferably username with Read Write permission on  SFTP/SCP/FTP/TFTP server. This is optional for TFTP
11. serverpassword - The password of the user specified above. This is optional for TFTP

## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration
- /etc/ansible/hosts - You must be editing the /etc/ansible/hosts file with the device information which are designated switches for Image Download. You may refer to cnos_conditional_template_sample for a sample configuration. Its pasted below  as well for your convenience.
[cnos_image_sample]
10.241.107.39   username=<username> password=<password> deviceType=g8272_cnos
10.241.107.40   username=<username> password=<password> deviceType=g8272_cnos
    
You should change all the Ip Addresses involved appropriately
- cnos_image.py - this module has to come in the library folder of the role.
- cnos_utility.py - this module has to come in the PYTHONPATH environment variable set in the Ansible system 

## Example Playbook

  - name: Module to  do image download
   hosts: cnos_image_sample
   gather_facts: no
   connection: local

   roles:
    - cnos_image_sample

## License

Copyright (C) 2017 Lenovo, Inc.

This Ansible Role is distributed WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
