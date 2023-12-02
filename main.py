import os
import platform
import NmapFunctions  # custom file for nmap
import DirsearchFunctions  # custom file for dirseach (or gobuster)
import Utils  # utilities

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
            os.system("py -m pip install impacket")
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
                os.system("sudo apt install metasploit-framework")
                os.system("sudo apt install hydra")
            elif platform.system() == "Windows":
                print("NMAP: https://nmap.org/download.html#windows")
                print("Hydra (THC Hydra): https://github.com/vanhauser-thc/thc-hydra")
                print("Metasploit Framework: https://www.metasploit.com/download")
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
        print("\n")

        inputs = str(input("""
Select an interaction :
- 1 : Run Passive Information Gathering
- 2 : Run Enumeration
- 3 : Run Metasploit
- 4 : Quit

Number: """))

        if inputs == "1":
            print("Running classic information gathering")
        elif inputs == "2":
            enumOver = False

            while not enumOver:
                print("\n")

                enum_input = str(input("""
                Select an interaction :
                - 1 : Basic nmap scan
                - 2 : Directories scan (WEBSITE)
                - 3 : Quit

                Number: """))

                if enum_input == "1":
                    NmapFunctions.basicNmapScan(sc)
                elif enum_input == "3":
                    possibleFilePath = str(input("Give the path to the dict: "))

                    if Utils.is_valid_file_path(possibleFilePath):
                        DirsearchFunctions.main(possibleFilePath)
                    else:
                        print("The path is not valid.")
                elif enum_input == "3":
                    enumOver = True
                else:
                    print("Wrong action!")
        elif inputs == "3":
            print("Running Metasploit")
        elif inputs == "4":
            over = True
        else:
            print("Wrong action!")


if __name__ == "__main__":
    main()
