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


def nikto(ip, port):
    filename = f"{ip}_{port}_nikto.txt"
    protocol = ["http://", "https://"]
    #print (f"Test filename variable: {filename}")
    if "443" in port:
        os.system(f"nikto -h {protocol[1]}{ip}:{port} -C all -k --useragent=evalian -o {filename}")
    else:
        os.system(f"nikto -h {protocol[0]}{ip}:{port} -C all --useragent=evalian -o {filename}")

nikto(ip,port)