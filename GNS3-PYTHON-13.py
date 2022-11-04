#!/usr/bin/env python3

from netmiko import ConnectHandler

Cisco_R1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.238',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

with open('DHCP.txt') as f:
    lines = f.read().splitlines()
print(lines)

net_connect = ConnectHandler(**Cisco_R1)
print("Conexión exitosa", net_connect.host)
output = net_connect.send_config_set(lines)
print(output)
