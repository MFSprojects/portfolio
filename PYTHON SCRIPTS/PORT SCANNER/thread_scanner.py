#!/bin/python3

import sys
import socket
from datetime import datetime
import threading

# Defines the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translates host input to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

print("M O O N F I R E CYBERSEC PROJECTS \n BASIC IP PORT SCANNER \n made with python")
print("-" * 33)  # This is just a separator line

print("Target Scanning: " + target)
print("Time started: " + str(datetime.now()))  # Prints timestamp as a string
print("-" * 33)

# Function to scan a single port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP connection
        socket.setdefaulttimeout(1)  # Timeout of 1 second
        result = s.connect_ex((target, port))  # Check the status of the port
        if result == 0:  # Port is open
            print(f"Port {port} is open")
        s.close()
    except:
        pass

# Threaded port scanning function
def threaded_scan(start_port, end_port):
    for port in range(start_port, end_port):
        scan_port(target, port)

# Main threading logic
try:
    threads = []
    total_ports = 65535
    num_threads = 100  # Adjust this to control the number of threads
    ports_per_thread = total_ports // num_threads

    for i in range(num_threads):
        start_port = i * ports_per_thread
        end_port = (i + 1) * ports_per_thread if i < num_threads - 1 else total_ports
        thread = threading.Thread(target=threaded_scan, args=(start_port, end_port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
