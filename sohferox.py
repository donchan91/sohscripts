#!/usr/bin/python3

import sys, os

ip = sys.argv[1]
port = sys.argv[2]

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <IP> <port>")
    sys.exit()

if ip.count(".") != 3:
    print ("Invalid IP. Exiting.....")
    print(f"Usage: {sys.argv[0]} <IP> <port>")
    sys.exit()

def ferox(ip,port):
    #Debug line to check for command line input
    filename = f"{ip}_{port}_feroxbuster_medium.txt"
    protocol = ["http://", "https://"]
    #print (f"Test filename variable: {filename}")
    if "443" in port:
        os.system(f"feroxbuster -u {protocol[1]}{ip}:{port} -k -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 10 -o {filename} ")
    else:
        os.system(f"feroxbuster -u {protocol[0]}{ip}:{port} -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 10 -o {filename} ")

ferox(ip,port)