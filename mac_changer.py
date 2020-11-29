# Example
# python ./mac_changer.py -i eth0 -m 00:11:22:33:44:55:66

#!/usr/bin/env python

import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address (xx:xx:xx...)")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_args()
change_mac(options.interface, options.new_mac)
