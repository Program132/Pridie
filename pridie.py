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
    speed = input("\n Speed of your scan: (1,2,3,4 or 5)")
    if speed != "1" and speed != "2" and speed != "3" and speed != "4" and speed != "5":
        print("Error: The speed of the scan must be between 1 and 5!")
        return
    command = ""
    if mode == "1":
        command = "nmap -T" + speed + " --top-ports=10 -sV -n -Pn --disable-arp-ping -D RND:5 " + ip
    elif mode == "2":
        command = "nmap -T" + speed + " -F -sV -n -Pn --disable-arp-ping -D RND:5 " + ip
    elif mode == "3":
        command = "nmap -T" + speed + " -p- -sV -n -Pn --disable-arp-ping -D RND:5 " + ip
    print("\n")
    print(f"Command executed: {command}")
    print("\n")
    print(os.system(command))
    print("\n")

if __name__ == "__main__":
    main()