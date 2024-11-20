#!/bin/python3

import sys
import socket 
from datetime import datetime

# Defines the target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translates host input to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

print("M O O N F I R E CYBERSEC PROJECTS \n BASIC IP PORT SCANNER \n made with python")
print("-" * 33) # This is just a seperator line

print("Target Scanning: "+target)
print("Time started: " +str(datetime.now())) # Prints timestamp as a string
print("-" * 33)

try:
	for port in range(0,65535): # Default all ports. You can change to 255, 1053, etc
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET says string is a host network // STREAM means TCP, change socket to SOCK_DGRAM for UDP
		socket.setdefaulttimeout(1) # Default timeout of 1 second 
		result = s.connect_ex((target,port)) # Tells you the status of that specific network port
		if result == 0: # This means the port is open, this would be 1 if the port were closed
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
# Using 'crtl + c' or other keys to exit

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
# Checks for errors in host IP prior to running port scan

except socket.error:
	print("Could not connect to server.")
	sys.exit()
# Error code response if the host network IP is down
	





