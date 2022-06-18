import os
from colorama import Fore

azul = Fore.BLUE
verde = Fore.GREEN
rojo = Fore.RED

def backdoorc():
    os.system("clear")
    print("""                  ____             _       _
                 | __ )  __ _  ___| | ____| | ___   ___  _ __
                 |  _ \ / _` |/ __| |/ / _` |/ _ \ / _ \| '__|
                 | |_) | (_| | (__|   < (_| | (_) | (_) | |
                 |____/ \__,_|\___|_|\_\__,_|\___/ \___/|_|

                        ____                _
                       / ___|_ __ ___  __ _| |_ ___  _ __
                      | |   | '__/ _ \/ _` | __/ _ \| '__|
                      | |___| | |  __/ (_| | || (_) | |
                       \____|_|  \___|\__,_|\__\___/|_""")
    print(f"""
    {rojo}[1] -----> Windows Backdoor
    [2] -----> Android Backdor
    [3] -----> Linux Backdoor
    [4] -----> Java Backdoor
    [5] -----> MacOS Backdoor
    [6] -----> iPhone Backdoor
    
    """)

    opcc = input(f"{rojo}Select ---> ")