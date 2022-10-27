#!/usr/bin/env python3

from netmiko import ConnectHandler

CiscoIOSvL2_SW1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.238',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

CiscoIOSvL2_SW2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.239',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

CiscoIOSvL2_SW3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.240',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

CiscoIOSvL2_SW4 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.241',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

CiscoIOSvL2_SW5 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.242',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

with open('IOSvL2_config.txt') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [CiscoIOSvL2_SW5, CiscoIOSvL2_SW4,
               CiscoIOSvL2_SW3, CiscoIOSvL2_SW2, CiscoIOSvL2_SW1]

for sw in all_devices:
    net_connect = ConnectHandler(**sw)
    print("Conexión exitosa", net_connect.host)
    output = net_connect.send_config_set(lines)
    print(output)
