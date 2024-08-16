import os
import platform
import socket
import shutil
import pyfiglet
from colorama import Fore, Style, init

print("by z0up29 x Dragosicu")

init(autoreset=True)

def print_logo():
    """Displays the main logo using pyfiglet."""
    ascii_logo = pyfiglet.figlet_format("PC Tools", font="starwars")
    print(Fore.MAGENTA + ascii_logo)

def check_internet_connection():
    """Checks the internet connection."""
    try:
        socket.create_connection(("www.google.com", 80))
        print(Fore.GREEN + "You are connected to the internet")
    except OSError:
        print(Fore.RED + "You are not connected to the internet")

def check_disk_space():
    """Checks the available disk space."""
    total, used, free = shutil.disk_usage("/")
    print(Fore.CYAN + f"Total Disk Space: {total // (2**30)} GiB")
    print(Fore.YELLOW + f"Used Space: {used // (2**30)} GiB")
    print(Fore.GREEN + f"Free Space: {free // (2**30)} GiB")

def system_info():
    """Displays basic system information."""
    print(Fore.CYAN + "System Information:")
    print(Fore.GREEN + f"Operating System: {platform.system()}")
    print(Fore.GREEN + f"OS Version: {platform.version()}")
    print(Fore.GREEN + f"Architecture: {platform.architecture()[0]}")
    print(Fore.GREEN + f"Processor: {platform.processor()}")

def show_menu():
    """Displays the menu and handles user selection."""
    while True:
        print("\nMenu:")
        print(f"1. {Fore.MAGENTA}Check Internet Connection")
        print(f"2. {Fore.MAGENTA}Check Disk Space")
        print(f"3. {Fore.MAGENTA}System Information")
        print(f"4. {Fore.MAGENTA}Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            check_internet_connection()
        elif choice == "2":
            check_disk_space()
        elif choice == "3":
            system_info()
        elif choice == "4":
            print(Fore.MAGENTA + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")

def main():
    """Main function to run the tool."""
    print_logo()
    show_menu()
    print_footer()

if __name__ == "__main__":
    main()
