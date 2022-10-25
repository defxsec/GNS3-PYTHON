#!/usr/bin/env python3

from netmiko import ConnectHandler

CiscoIOSvL2_SW1 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.144',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

CiscoIOSvL2_SW2 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.145',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

CiscoIOSvL2_SW3 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.239.146',
    'username': 'defxsec',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    # 'secret': 'secret',     # optional, defaults to ''
}

all_devices = [CiscoIOSvL2_SW1, CiscoIOSvL2_SW2, CiscoIOSvL2_SW3]

for sw in all_devices:
    net_connect = ConnectHandler(**sw)
    print("Conexión exitosa", net_connect.host)
    for n in range(2, 10):
        print("Creando VLAN " + str(n))
        config_commands = ['vlan ' + str(n),
                           'name Python_VLAN_' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
