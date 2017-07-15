#!/usr/bin/python3
import telnetlib

HOST='localhost'
tn = telnetlib.Telnet(HOST, '7000')
while True:
	tn.interact()
	#print(tn.read_until(b'\n'))

