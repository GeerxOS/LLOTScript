import os
from time import sleep
from colorama import Fore
from scripts.iptracker import iptracker
from scripts.backdoorc import backdoorc

# Variables colores y mas

user = os.getlogin()
negro = Fore.BLACK
azul = Fore.BLUE
azul2 = Fore.LIGHTBLUE_EX
cian = Fore.CYAN
verde = Fore.GREEN
verde2 = Fore.LIGHTGREEN_EX
magen = Fore.MAGENTA
rojo = Fore.RED
reset = Fore.RESET
blanco = Fore.WHITE
amarillo = Fore.YELLOW

def main():
    os.system("clear")
    print(f"""

{verde2} ▄▀▀▀▀▄    ▄▀▀▀▀▄    ▄▀▀▀▀▄   ▄▀▀▀█▀▀▄      ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▀▄    ▄▀▀▄▀▀▀▄  ▄▀▀▀█▀▀▄ 
{rojo}█    █    █    █    █      █ █    █  ▐     █ █   ▐ █ █    ▌ █   █   █ █   █  █  █   █   █ █    █  ▐ 
{rojo}▐    █    ▐    █    █      █ ▐   █            ▀▄   ▐ █      ▐  █▀▀█▀  ▐   █  ▐  ▐  █▀▀▀▀  ▐   █     
{rojo}    █         █     ▀▄    ▄▀    █          ▀▄   █    █       ▄▀    █      █        █         █      
{rojo}  ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄▄▄▀ ▀▀▀▀    ▄▀            █▀▀▀    ▄▀▄▄▄▄▀ █     █    ▄▀▀▀▀▀▄   ▄▀        ▄▀       
{rojo}  █         █                █              ▐      █     ▐  ▐     ▐   █       █ █         █         
{verde2}  ▐         ▐                ▐                     ▐                  ▐       ▐ ▐         ▐         
                                {amarillo}Welcome {user}!
{reset} 
{verde2}
    [1] Backdoor Creator
    [2] IP-Tracker
    [3] IDSO
    [4] IP-Logger
    [5] Number Info
    [6] Port-Scanner

[00] Exit


""")
    opc = input(f"{magen}Select -> ")

    if opc == "1":
        backdoorc()
        main()

    if opc == "2":
        iptracker()
        main()

    if opc == "3":
        ip_3 = input(f"{verde}Target IP --> ")
        os.system(f"python3 scripts/idso.py {ip_3}")
        input("Enter to back")
        main()

    if opc == "4":
        input("ERROR.")
        main()

    if opc == "5":
        os.system("python3 scripts/ninfo.py")
        input("Enter to back")
        main()

    if opc == "6":
        ip_2 = input(f"{verde}Target IP --> ")
        os.system(f"python3 scripts/portscanner.py {ip_2}")
        input("Enter to back")
        main()

    if opc == "00":
        print(f"{rojo}Exiting....")
        time.sleep(1)
        exit()

    else:
        print(f"{azul}[{rojo}-{azul}] {opc} Is not a command!")
        main()
        time.sleep(2)
        
if __name__ == '__main__':
    main()