#!/bin/python3

#syntax: 
#       python3 scanner.py <ip address>
#scan through a port range


import sys
import socket
from datetime import datetime

#Define Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPV4
else:  #if no ip addrtess found the user will get this
    print("Invalid Amount Of Arguement") 
    print("\n")
    print("syntax: python3 scanner.py <ip address>")

#Add Banner
print("-" * 50) #50 dashes(-)
print("Scanning Target: "+target) #Print Target 
print("Time Started: "+str(datetime.now())) #prints date & Time of the scan

try:
    for port in range(1, 1024): #Specify the port range
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# AF_INET = IPV4 + SOCK_STREAM = port ;: s = connection over IPV4 
        socket.setdefaulttimeout(1) #connection will timeout after 1 second 
        result = s.connect_ex((target, port)) #returns an error indicator, if there is an error the result will be 1 else  if successful then the result will be 0
#        print("Checking port {}.".format(port)) #print the ports that are being checked
        if result == 0: #prints the rusult based on result variable
            print("Port {} is open".format(port))
#        else:  #prints the rusult based on result variable
#            print("Port {} is close".format(port))
        s.close()

except KeyboardInterrupt: #Exit program if there is any keyboard interuptions
    print("\nExiting Program.")
    sys.exit

except socket.gaierror: #Exit program if there is no hostname
    print("\nHostname Could Not Be Resolved.")
    sys.exit

except socket.error:  #Exit program if the connection to the server is failing
    print("\nCould Not Connect To The Server")
    sys.exit

#Print Finishing Time
print("Time finished: "+str(datetime.now()))
