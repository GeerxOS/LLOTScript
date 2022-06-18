import requests
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")

print("""          
          _   _                 _                 ___        __       
         | \ | |_   _ _ __ ___ | |__   ___ _ __  |_ _|_ __  / _| ___  
         |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|  | || '_ \| |_ / _ \ 
         | |\  | |_| | | | | | | |_) |  __/ |     | || | | |  _| (_) |
         |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    |___|_| |_|_|  \___/
         """)

api_key = '48d04397c36551c48eced6a4304b66f6'

number = int(input(GREEN+"Number -->  "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))