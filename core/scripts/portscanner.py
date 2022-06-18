import sys
import socket
from colorama import Fore
from datetime import datetime

verde = Fore.LIGHTGREEN_EX

print(f""" 
{verde}
          ____            _     ____                                  
         |  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
         | |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
         |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
         |_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|""")

# Definiendo el objetivo
if len(sys.argv) == 2:
     
    # traducir el host a ipv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
 

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)
  
try:
     
    # escaneando puertos
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
       # errores
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
         
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()