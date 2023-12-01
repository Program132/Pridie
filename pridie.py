# pip3 install python-nmap
# pip3 install pymetasploit3

import os
import platform

title = """
██████╗░██████╗░██╗██████╗░██╗███████╗
██╔══██╗██╔══██╗██║██╔══██╗██║██╔════╝
██████╔╝██████╔╝██║██║░░██║██║█████╗░░
██╔═══╝░██╔══██╗██║██║░░██║██║██╔══╝░░
██║░░░░░██║░░██║██║██████╔╝██║███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝╚══════╝
"""

print(title)

def verificationToolsAndLibs():
    aMenu = False
    while not aMenu:
        accessMenu = str(input("Do you want to install libs to use Pridie? (y/n)"))
        if accessMenu == "y":
            print("Installing libs...")
            os.system("py -m pip install python-nmap")
            os.system("py -m pip install pymetasploit3")
            break
        elif accessMenu == "n":
            break
        else:
            print("Wrong action try again!")

    aMenu = False
    while not aMenu:
        accessMenu = str(input("Do you want to install tools to use Pridie? (y/n)"))
        if accessMenu == "y":
            print("Installing tools...")
            if platform.system() == "Linux":
                os.system("sudo apt install nmap")
                os.system("sudo apt install metasploit")
            elif platform.system() == "Windows":
                print("NMAP: https://nmap.org/download.html#windows")
            break
        elif accessMenu == "n":
            break
        else:
            print("Wrong action try again!")

def main():
    verificationToolsAndLibs()

    over = False

    import nmap

    sc = nmap.PortScanner()

    while not over:
        inputs = str(input("""
Select an interaction :
- 1 : Run Classic Information gathering
- 2 : Run NMAP Enumeration
- 3 : Run Metasploit
- 4 : Quit

Number: """))

        if inputs == "1":
            print("Running classic information gathering")
        elif inputs == "2":
            TargetIP = str(input("Enter the target IP : "))
            TargetPort = str(input("Enter the port(s) : "))
            Speed = str(input("Speed of the scan (1-5) : "))

            if Speed != "1" and Speed != "2" and Speed != "3" and Speed != "4" and Speed != "5":
                print("You did not give a valid speed, the default will be 3.")
                Speed = 3

            print(f"Running scan on {TargetIP} {TargetPort}")
            sc.scan(TargetIP, TargetPort, arguments=f"-T{Speed}")
            result = sc[TargetIP]['tcp']
            print("Opened ports : ")
            for i in result.keys():
                print(f"- {i}, {result[i]['name']}")
        elif inputs == "3":
            print("Running Metasploit")
        elif inputs == "4":
            over = True

if __name__ == "__main__":
    main()