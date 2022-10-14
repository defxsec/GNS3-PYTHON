#!/usr/bin/env python3

import getpass
import telnetlib

HOST = "192.168.1.11"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")

tn.write(b"configure terminal\n")

for n in range(2, 10):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
