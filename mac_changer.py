#!/usr/bin/env python

import subprocess

interface = raw_input("Enter interface : ")
new_mac = raw_input("Enter new mac : ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
