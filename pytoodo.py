import os
import platform
import sys

# Functions
def display_line_art(title_bar_msg: str) -> str:    
    # 1: >>--------------->
    # 2: :.:.:.:.:.:.:.:.:.:.:
    # 3: @-->--->--->--->--->
    # 4: ------------------
    
    # set style[1-4]:
    style = 4
    
    # len of header
    number = len(str(title_bar_msg))
    
    if style == 1:
        string = f">>" + "-"*number + ">"    
    elif style == 2:
        string = f":."*number + ":"
    elif style == 3:
        string = f"@--" + ">---"*number + ">"
    elif style == 4:
        string = f"-"*number
    else:
        string = []
    return title_bar_msg + "\n" + string

def display_tasks():
    if not os.path.exists("tasks.txt") or os.stat("tasks.txt").st_size == 0:
        print("You have no tasks for today! Try adding some tasks below.")
        return

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")

def add_task():
    dislay_main_menu()
    task = input("\nEnter your task:\n> ")
    with open("tasks.txt", "a") as file:
        file.write(f"{task}\n")
    print("Task added successfully!")

def delete_task():
    dislay_main_menu()
    task_index = False
    while task_index is False:
        try:
            task_index = int(input("\nEnter the number of the task you want to delete: "))
        except Exception:
            dislay_main_menu()
            continue
        
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    tasks = [task for task in tasks if task.strip()]
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number. Try again.")
        return
    with open("tasks.txt", "w") as file:
        for i, task in enumerate(tasks, 1):
            if i != task_index:
                file.write(f"{task}")
    print("Task deleted successfully!")
   
def display_choices():
        print("\nChoices: ")
        print("[1] - Show all tasks")
        print("[2] - Add task")
        print("[3] - Delete task")
        print("[q] - Quit")

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def count_newlines(file_path):
    if not os.path.exists("tasks.txt") or os.stat("tasks.txt").st_size == 0:
        return 0
    with open(file_path, 'r') as f:
        contents = f.read()
        return contents.count('\n')

def display_header():
    file_name = "tasks.txt"
    lines = count_newlines(file_name)
    print(display_line_art(f"pytoodo / your tasks ({lines})"))

def dislay_main_menu():
        clear_screen()
        display_header()    
        display_tasks()
        
# Main program
def main():
    while True:
        dislay_main_menu()
        
        # Get user choice
        display_choices()
        choice = input("Enter your choice [1-3, q(uit)]\n> ")
        
        # Process user input
        # [1] - Show all tasks
        if choice == "1":
            dislay_main_menu()
        # [2] - Add task
        elif choice == "2":
            add_task()
        # [3] - Delete task
        elif choice == "3":
            delete_task()
        # [q] - Quit
        elif choice.upper() == "Q":
            clear_screen()
            sys.exit()
        else:
            display_header()
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
