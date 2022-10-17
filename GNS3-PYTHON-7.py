#!/usr/bin/env python3

import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open("HOSTs.txt")

for ip in f:
    print("Configurando Switch" + ip)

    tn = telnetlib.Telnet(ip.strip())

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"ls\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show running-config\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all()
    saveoutput = open("Switch" + ip.strip(), "wb")
    saveoutput.write(readoutput)
    saveoutput.close()
