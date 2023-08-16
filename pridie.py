# py -m pip install python-nmap

import os

title = """
██████╗░██████╗░██╗██████╗░██╗███████╗
██╔══██╗██╔══██╗██║██╔══██╗██║██╔════╝
██████╔╝██████╔╝██║██║░░██║██║█████╗░░
██╔═══╝░██╔══██╗██║██║░░██║██║██╔══╝░░
██║░░░░░██║░░██║██║██████╔╝██║███████╗
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝╚══════╝
"""

print(title)

def main():
    waitingEnd = True

    while waitingEnd:
        num = input("0 - Exit\n1 - Network Scanner\nPlease enter a number: ")

        if num == "0":
            print("Good bye")
            waitingEnd = False
        elif num == "1":
            NetworkScanner()
        else:
            print("Wrong number!")
    return

def get_ip():
    return input("\nGive me the IP from the target: ")

def NetworkScanner():
    print("**** Welcome to Little Network Scanner ****")
    ip = get_ip()
    mode = input("\nMode of your scanner: \n1 - Classic (Top 10), Silent\n2 - Classic (Top 100), Silent\n3 - All ports, Silent\nEnter a number: ")
    command = ""
    if mode == "1":
        command = "nmap -T3 --top-ports=10 -sV -n -Pn --disable-arp-ping -D RND:5 " + ip
    elif mode == "2":
        command = "nmap -T3 -F -sV -n -Pn --disable-arp-ping -D RND:5 " + ip
    elif mode == "3":
        command = "nmap -T3 -p- -sV -n -Pn --disable-arp-ping -D RND:5 " + ip
    print(f"\n Command executed: {command}" + os.system(command) + "\n")

if __name__ == "__main__":
    main()