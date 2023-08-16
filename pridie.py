# py -m pip install python-nmap

import nmap

title = """
██████╗░██████╗░██╗██████╗░██╗███████╗
██╔══██╗██╔══██╗██║██╔══██╗██║██╔════╝
██████╔╝██████╔╝██║██║░░██║██║█████╗░░
██╔═══╝░██╔══██╗██║██║░░██║██║██╔══╝░░
██║░░░░░██║░░██║██║██████╔╝██║███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝╚══════╝
"""

print(title)

nm = nmap.PortScanner()

def main():
    waitingEnd = True

    while waitingEnd:
        num = input("0 - Exit\n1 - Little Network Scanner\n2 - Large Network Scanner\n3 - Silent Little Network Scanner\n4 - Silent Large Network Scanner\n Please enter a number: ")

        if num == 0 or num == "0":
            print("Good bye")
            waitingEnd = False
        elif num == 1 or num == "1":
            nmap_little()
        else:
            print("Wrong number!")
    return

def get_ip():
    ip = str(input("\nGive me the IP from the target: "))
    return ip
def nmap_little():
    print("**** Welcome to Little Network Scanner ****")
    ip = get_ip()
    nm.scan(ip, '1-443')
    print(nm.scaninfo())
    print(nm[ip]['tcp'].keys())

main()