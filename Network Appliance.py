# Libraries needed for network activities
import os
import socket


# function for option 1 (pinging)
def option_1():
    print("the Ping option")
    hostname = input("pls enter the address you wish to ping>>")  # lets the user specify what IP to ping
    response = os.system("ping -n 1 " + hostname)  # the ping command
    # conditions for ping response
    if response == 0:
        print(hostname, "is up!")
        print("_" * 60)
    else:
        print(hostname, "is down!")
        print("_" * 60)
    print("Ping executed successfully, returning to the main menu...")


# function for option 2 (port scanning)
def option_2():
    print("The port scanner")
    # the socket library command that lets us connect to ports online
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # assigning the command a shorter alias for quick use
    print("welcome, Please wait while port is being scanned")
    # inputting data for port scan to run
    host = input("enter the IP address>>")
    i = int(input("please enter the port NUMBER you'd like to start scanning from>>"))
    j = int(input("Please enter the port NUMBER you'd like the scan to stop at>>"))
    print("Thank you for your Selection,\nPlease wait while port(s) is/are being scanned")
    print("_" * 60)
    # conditions for running port scan
    for port in range(i, (j + 1)):  # +1 is added to provide a complete range of ports to be scanned
        if s.connect_ex((host, port)):
            print("Port", port, "is closed")
        else:
            print("Port", port, "is open")
        print("_" * 60)
    print("port scanning complete returning to main menu...")


def option_3():
    print("Traceroute stub")


def option_4():
    # start of the sub-menu for the help option
    print("welcome to the help menu")

    # function that defines ping help
    def ping():
        print("^" * 70)
        print("the Ping option lets you ping any IP address or web address of your choosing \n"
              "all you need to do type in the address you would like to ping, hit enter, and the command will be "
              "executed\nif"
              "the host is up, you get the message, \n[the host is up] and if the host is down, you get the message ["
              "the host is down]")
        print("_" * 70)

    # function that defines the port scanner help
    def port_scanner():
        print("^" * 70)
        print(
            "the Port scanner tool lets you run port scan on a range of open ports. when initiated, you need to enter "
            "\nthe"
            "IP address or web address of the host, whose ports you would like to scan \nafter this, enter a range of "
            "ports"
            "you would like to scan. \nFrom the port you want to begin with to the port you want to end at and hit "
            "enter. \nthe"
            "output for the port scan will be what ports are open from that IP address")
        print("_" * 70)

    # function that defines the traceroute help
    def traceroute():
        print("^" * 70)
        print("The traceroute tool lets you input an IP address or a web address and the program returns \nthe"
              "number of hops its takes to get to the address")
        print("_" * 70)

    # function that returns to the previous menu
    def terminate():
        print("*" * 70)

    # function that handles wrong entries
    def wrong_entry():
        print("Sorry invalid entry Pls try again")
        print("_" * 70)

    # function that defines the help menu parameters
    def menu2():
        print("*" * 70)
        print("please select one of the following:")
        print("Type 1 for Help on the ping option")
        print("Type 2 for help on the port scanner option")
        print("Type 3 for help on the traceroute option")
        print("Type 4 if you want to return to the previous menu")
        choice = input(" enter your choice here >>")
        return choice

    menu_choice2 = menu2()

    while True:
        if menu_choice2 == "1":
            ping()
        elif menu_choice2 == "2":
            port_scanner()
        elif menu_choice2 == "3":
            traceroute()
        elif menu_choice2 == "4":
            terminate()
            break
        else:
            wrong_entry()
        menu_choice2 = menu2()


def option_5():
    print("Thank you for running the program\n", "_" * 70)


def invalid_entry():
    print("invalid entry \nLoading the menu again...\n",
          "*" * 70)


def menu():
    print("*" * 70)
    print("please select one of the following:")
    print("Type P for Option 1")
    print("Type E for Option 2")
    print("Type L for Option 3")
    print("Type U for option 4")
    print("Type M To Quit the program")
    choice = input("Please enter your Choice here>>")
    return choice


menu_choice = menu()

while True:
    if menu_choice == "P" or menu_choice == "p":
        option_1()
    elif menu_choice == "E" or menu_choice == "e":
        option_2()
    elif menu_choice == "L" or menu_choice == "l":
        option_3()
    elif menu_choice == "U" or menu_choice == "u":
        option_4()
    elif menu_choice == "M" or menu_choice == "m":
        option_5()
        break
    else:
        invalid_entry()
    menu_choice = menu()

# quotations for "^" "-" "*" string commands used to separate code execution segments
