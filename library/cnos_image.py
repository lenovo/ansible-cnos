#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Lenovo, Inc.

# This module is distributed WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#
# See the GNU General Public License for more details <http://www.gnu.org/licenses/>.
#
# Module to download new image to Lenovo Switches
# Lenovo Networking
#
#---- Documentation Start ----------------------------------------------------#
DOCUMENTATION = '''
---
version_added: "1.7"
module: cnos_image
short_description: Performs Image Download on switches using SFTP/SCP/FTP/TFTP.
description: 
    - Manages network device configurations over SSH.
    This module allows implementors to work with the device images.
    It provides a way to download images onto a network device from an SFTP/SCP/FTP/TFTP server.
    You have to first create a folder which has the reach of the SFTP/SCP/FTP/TFTP Server.
    Then specify the full path from where you need to download the image.
    Authentication details pertaining to SFTP/SCP/FTP server also have to be provided.
    Here is this method, its made default to make the newly downloaded image as the active one after restart.
    Results of the download can be viewed in results folder.
options:
# Options are as given below
    
    outputfile:
        description:
            - This specifies the file path to which the output of each command excecution is persisted. 
             Response from the device saved here. Usually the location is the results folder. 
             But your user can choose which ever path he has write permission. 
        required: true
        default: null
        choices: []
    host:
        description:
            - This is the variable which used to look into /etc/ansible/hosts file so that device IP addresses 
            - on which this template has to be applied is identified. Usually we specify the ansible keyword 
            - {{ inventory_hostname }} which we specify in the playbook which is an abstraction to the group of 
            - network elements that need to be configured.
        required: true
        default: null
        choices: []
    username:
        description:
            - Configures the username to use to authenticate the connection to the remote device. The value of 
            - username is used to authenticate the SSH session. The value has to come from inventory file ideally,
            - you can even enter it as variable.
        required: true
        default: 
        choices: []
    password:
        description:
            - Configures the password to use to authenticate the connection to the remote device. 
            - The value of password is used to authenticate the SSH session.The value has to come from inventory file ideally,
            - you can even enter it as variable.
        required: true
        default: 
        choices: []
    enablePassword:
        description:
            - Inputs the enable password, in case its enables in the device. This get ignored if the device is not demanding an enable password. 
            - The value of password is used to enter the config mode.The default value is empty string. The value has to come from inventory file ideally,
            - you can even enter it as variable.
        required: false
        default: 
        choices: []
    deviceType:
        description:
            - This specifies the type of device against which the image is downloaded. 
        required: Yes
        default: null
        choices: []
    protocol:
        description:
            - This refers to the protocol in which your device will interact with the server you are 
            connecting to download image onto the device. The choices for you are SFTP, SCP, FTP or TFTP. 
            Any other protocols apart from the above will result in error. There is no default specified for 
            this argument 
        required: Yes
        default: null
        choices: [SFTP, SCP, FTP, TFTP]
    serverip:
        description:
            - IP Address of the SFTP/SCP/FTP/TFTP server you are using for the download of image to device 
        required: Yes
        default: null
        choices: []
    imgpath:
        description:
            - This specifies the absolute path of the image file located in the server. In case u are using 
            the relative path as the variable value, you need to specify the root folder for the user of the 
            server which u have specified.
        required: Yes
        default: null
        choices: []
    imgtype:
        description:
            - Image type which you indent to download
            - all   Both Uboot and OS
            - boot  Uboot only
            - onie  ONIE image
            - os    OS only
        required: Yes
        default: null
        choices: []
    serverusername:
        description:
            - Username for the server pertaining to respective protocol of your choice
        required: True
        default: null
        choices: []
    serverpassword:
        description:
            - Password for the server pertaining to respective protocol of your choice
        required: false
        default: null
        choices: []
    
notes:
    - For help in developing on modules, should you be so inclined, please read 
    Community Information & Contributing, Helping Testing PRs and Developing Modules.
    Module Dependency :
    1. cnos_image.py
    2. cnos_utility.py 
'''
EXAMPLES = '''
The task/main.yml will look like this

---

- name: Test Image transfer
  cnos_image: host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_image_{{ inventory_hostname }}_output.txt protocol='{{item.protocol}}' serverip='{{item.serverip}}' imgpath='{{item.imgpath}}' imgtype='{{item.imgtype}}' serverusername='{{item.serverusername}}' serverpassword='{{item.serverpassword}}'
  with_items: "{{test_image_data1}}"

- name: Test Image tftp
  cnos_image: host={{ inventory_hostname }} username={{ hostvars[inventory_hostname]['username']}}  password={{ hostvars[inventory_hostname]['password']}} deviceType={{ hostvars[inventory_hostname]['deviceType']}} outputfile=./results/cnos_image_{{ inventory_hostname }}_output.txt protocol='{{item.protocol}}' serverip='{{item.serverip}}' imgpath='{{item.imgpath}}' imgtype='{{item.imgtype}}' serverusername='{{item.serverusername}}' serverpassword='{{item.serverpassword}}'
  with_items: "{{test_image_data2}}"

In the vars/main.yml will look like this

---
test_image_data1:
  - {protocol: "sftp", serverip: "10.241.106.118", imgpath: "/root/cnos_images/G8272-10.1.0.112.img", imgtype: "os", serverusername: "root", serverpassword: "root123"}

test_image_data2:
  - {protocol: "tftp", serverip: "10.241.106.118", imgpath: "/anil/G8272-10.2.0.34.img", imgtype: "os", serverusername: "root", serverpassword: "root123"}

In the inventory file u specify like this
[cnos_image_sample]
10.241.107.39  username=<username> password=<password> deviceType=g8272_cnos
10.241.107.40  username=<username> password=<password> deviceType=g8272_cnos
'''

RETURN = '''

On successful execution, the method returns and empty string with a message "Image file tranferred to device" 
in json format. But upon any failure, the output will be the error display string. You may have to rectify the 
error and try again..

'''
#---- Documentation Ends ----------------------------------------------------#
#---- Logic Start ------------------------------------------------------------###
#
import sys
import paramiko
import time
import argparse
import socket
import array
import json
import time
import re
try:
    import cnos_utility
    HAS_LIB=True
except:
    HAS_LIB=False

#
# load Ansible module
#
from ansible.module_utils.basic import *
from collections import defaultdict

#
def  main():
    #
    # Define parameters for commandline entry
    #
    module = AnsibleModule(
        argument_spec=dict(
            outputfile=dict(required=True),
            host=dict(required=True),
            username=dict(required=True),
            password=dict(required=True),
            enablePassword=dict(required=False),
            deviceType=dict(required=True),
            protocol=dict(required=True),
            serverip=dict(required=True),
            imgpath=dict(required=True),
            imgtype=dict(required=True),
            serverusername=dict(required=False),
            serverpassword=dict(required=False),),
        supports_check_mode=False)

    username = module.params['username']
    password = module.params['password']
    enablePassword = module.params['enablePassword']
    outputfile = module.params['outputfile']
    host = module.params['host']
    deviceType = module.params['deviceType']
    protocol = module.params['protocol'].lower()
    imgserverip = module.params['serverip']
    imgpath = module.params['imgpath']
    imgtype = module.params['imgtype']
    imgserveruser = module.params['serverusername']
    imgserverpwd = module.params['serverpassword'] 
    output = ""
    timeout = 120
    tftptimeout = 600

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection with the switch
    remote_conn_pre.connect(host, username=username, password=password)
    time.sleep(2)
    
    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    time.sleep(2)
    
    #
    # Enable and enter configure terminal then send command
    output = output + cnos_utility.waitForDeviceResponse("\n", ">", 2, remote_conn)
    
    output = output + cnos_utility.enterEnableModeForDevice(enablePassword, 3, remote_conn)
    
    # Make terminal length = 0
    output = output + cnos_utility.waitForDeviceResponse("terminal length 0\n", "#", 2, remote_conn)
	
    transfer_status = ""
    # Invoke method for image transfer from server	
    if(protocol == "tftp" or protocol == "ftp"):
        transfer_status = cnos_utility.doImageTransfer(protocol, tftptimeout, imgserverip, imgpath, imgtype, imgserveruser, imgserverpwd, remote_conn)
    elif(protocol == "sftp" or protocol == "scp"):
        transfer_status = cnos_utility.doSecureImageTransfer(protocol, timeout, imgserverip, imgpath, imgtype, imgserveruser, imgserverpwd, remote_conn)
    else:
        transfer_status = "Invalid Protocol option"
    
	
    output = output + "\n Image Transfer status \n" + transfer_status 

	# Save it into the file
    file = open(outputfile, "a")
    file.write(output)
    file.close()
    
    # Logic to check when changes occur or not
    errorMsg = cnos_utility.checkOutputForError(output)
    if(errorMsg == None):
        module.exit_json(changed=True, msg="Image file tranferred to device")
    else:
        module.fail_json(msg=errorMsg)
    

if __name__ == '__main__':
        main()
