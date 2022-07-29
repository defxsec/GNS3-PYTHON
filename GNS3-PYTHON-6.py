#!/usr/bin/env python3

from ast import For
import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

for n in range(111, 116):
    HOST = "192.168.1." + str(n)

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
    #Añadimos este fragmento de codigo para no tener problema
    tn.write(b"wr\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))