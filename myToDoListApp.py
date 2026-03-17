from colorama import Fore, Style, init
import os

#initialize colorama
init(autoreset = True)

tasks = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    print(Fore.CYAN + "="*30)
    print(Fore.YELLOW + "      My TO-Do List     ")
    print(Fore.CYAN + "="*30)
    print(Fore.GREEN + "1. Add Task")
    print(Fore.GREEN + "2. View Tasks")
    print(Fore.GREEN + "3. Remove Tasks")
    print(Fore.GREEN + "4. Exit")
    
    choice = input(Fore.MAGENTA + "Enter your choice(1-4):")
    if choice == "1":
        task = input("Enter a task:")
        tasks.append(task)
        print(Fore.GREEN + f"Task `{task}` added successfully!")
        #input(Fore.CYAN + "Press Enter to continue...")
        
    elif choice == "2":
        print(Fore.YELLOW + "\nYour Tasks:")
        if tasks:
            for idx, t in enumerate(tasks, start = 1):
                print(Fore.BLUE + f"{idx}.{t}")
        else:
            print(Fore.RED + "No tasks found!")
        #input(Fore.CYAN + "Press Enter to continue...")
    
    elif choice =="3":
        if tasks:
            remove_task = int(input("Enter task number to remove:"))
            if 0 < remove_task <= len(tasks):
                removed = tasks.pop(remove_task - 1)
                print(Fore.GREEN + f"Task `{removed}` removed successfully!")
            else:
                print(Fore.RED + "Invalid task number")
        #input(Fore.CYAN + "Press Enter to continue...")
        
    elif choice == "4":
        print(Fore.RED + "Existing To-Do List. Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice! Please enter 1-4")
        #input(Fore.CYAN + "Press Enter to continue...")