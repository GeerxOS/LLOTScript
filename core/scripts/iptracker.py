import os
from time import sleep

def iptracker():
    os.system("clear")
    print("""                 ___ ____     _____               _
                |_ _|  _ \   |_   _| __ __ _  ___| | _____ _ __
                 | || |_) |____| || '__/ _` |/ __| |/ / _ \ '__|
                 | ||  __/_____| || | | (_| | (__|   <  __/ |
                |___|_|        |_||_|  \__,_|\___|_|\_\___|_|""")
    ip = input("IP +-> ")
    print("Wait...")
    sleep(2)
    os.system(f"curl -s http://ip-api.com/{ip}")
    print("")
    input("Done!")
    