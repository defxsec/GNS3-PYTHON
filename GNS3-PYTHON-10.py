#!/usr/bin/env python3

from netmiko import ConnectHandler

CiscoIOSvL2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.143',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

net_connect = ConnectHandler(**CiscoIOSvL2)

output = net_connect.send_command('show ip interface brief')
print(output)

config_commands = ['interface loopback 0',
                   'ip address 1.1.1.1 255.255.255.255',
                   'interface loopback 1',
                   'ip address 2.2.2.2 255.255.255.255']

output = net_connect.send_config_set(config_commands)
print(output)

for n in range(2, 15):
    print("Creando VLAN " + str(n))
    config_commands = ['vlan ' + str(n),
                       'name Python_VLAN_' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
