#!/usr/bin/env python

import subprocess

interface = input("Enter interface : ") # change input to raw_input for python2
new_mac = input("Enter new mac : ") # change input to raw_input for python2

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
