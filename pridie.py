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

nm = nmap.PortScanner()

def main():
    waitingEnd = True

    while waitingEnd:
        num = input("0 - Exit\n1 - Network Scanner\n2\n Please enter a number: ")

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
    mode = input("\Mode of your scanner: \n1 - Classic and Fast\n2 - Classic and Fast\n3 - Classic and Fast+Silent")
    command = ""
    if mode == "1":
        command = "nmap -T5 --top-ports=10 -sV " + ip
    elif mode == "2":
        command = "nmap -T3 --top-ports=10 -sV -n -Pn --disable-arp-ping -D RND:5 " + ip
    elif mode == "3":
        command = "nmap -T5 --top-ports=10 -sV -n -Pn --disable-arp-ping -D RND:5 " + ip
    print(os.system(command))
    

if __name__ == "__main__":
    main()