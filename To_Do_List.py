#!/usr/bin/python3

import sys
import os
import time

# Empty list waiting for saved tasks to do.
to_do_list = []

# Infinite loop, which returns the "chosing menu".
loop = 0


# Formats of text color assigned to system informations.
class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"


# Format of text bold (named as second class to differentiate).
class font:
    BOLD = "\033[1m"
    END = "\033[0m"


# Definitions section.
def ornament1():
    """Decoration for text (with new line)"""
    print("\n{}".format("-" * 80))


def ornament2():
    """Decoration for text (without new line)"""
    print("{}".format("-" * 80))


def list_reminder():
    """Print user's list of tasks to do"""
    print("\nYOUR LIST TO DO:\n")
    for index, item in enumerate(to_do_list, start=1):
        print("{}. {}".format(index, item))

# File Management System, to saving progress.
if os.path.exists("List to do.txt"):  # Checks if the file is already existing at the script's directory.
    with open("List to do.txt", "r") as in_file:  # If it so -- read from inside the saved user's list "to do".
        to_do_list = in_file.read().splitlines()
else:
    with open("List to do.txt", 'a+') as out_file:  # If not -- create immediately the new file with an empty list.
        print("File ""\"""List to do.txt""\""" is created at the Python's script directory!")

# Name of the script.
print("\n\n\t\t\t\tLIST TO DO:")

### MAIN LOOP of THE SCRIPT ###
while loop == 0:
    print("\nPlease, specify a command (LIST, ADD, MARK, UNMARK, DELETE, HELP, EXIT): ", end="")  # Allowed script options.
    command_console = input()

    # HELP option (just informative).
    if command_console.lower() == ("help"):  # Case letter insensitive (whenever of input).
        ornament1()
        print("LIST:")
        print("  Shows the complete list of your saved tasks.")
        print("\nADD:")
        print("  Puts any of your task onto the special ""\"""TO DO""\""" list.")
        print("  New tasks will be displayed as ""\"""undone""\""" until mark.")
        print("\nMARK:")
        print("  Checks a single task from your list as ""\"""complete""\""".")
        print("\nUNMARK:")
        print("  Unchecks a single task from your list as ""\"""undone""\""".")
        print("  Very helpfull if you mark something by a mistake.")
        print("\nDELETE:")
        print("  Removes a single task from your list (you can also")
        print("  wish to archive all of your finished tasks at once).")
        print("\nEXIT:")
        print("  Save your list on the file and quit the program.")
        ornament2()

    # LIST option (print the function named "list_reminder").
    elif command_console.lower() == ("list"):
        if len(to_do_list) < 1:
            ornament1()
            print(color.YELLOW + "Your list is empty!" + color.END)
            ornament2()
        else:
            list_reminder()

    # ADD option (creating new task to do).
    elif command_console.lower() == ("add"):
        item_to_do = input("\nAdd an item: ")
        to_do_list.append("[ ] " + item_to_do)
        ornament1()
        print(color.GREEN + "{} was added!".format(item_to_do) + color.END)  # Print the name of added item.
        ornament2()

    # MARK option (selecting undone task as complete).
    elif command_console.lower() == ("mark"):
        if len(to_do_list) < 1:
            ornament1()
            print(color.YELLOW + "Your list is empty!" + color.END)
            ornament2()
        if len(to_do_list) >= 1:  # List must have, at least, one item to modifying it.
            list_reminder()
            try:
                done = int(input("\nWhich one do you want to MARK as completed? Choose a number: "))
                if "[ ]" in to_do_list[done - 1]:  # When "[x]" item was marked, there is no system output.
                    to_do_list[done - 1] = to_do_list[done - 1].replace("[ ]", "[x]", 1)
                    ornament1()
                    print(color.GREEN + "Task completed!" + color.END)
                    ornament2()
            except:
                ornament1()
                print (color.RED + "Invalid sign or number are above the list! Try again." + color.END)   # User's input error.
                ornament2()

    # UNMARK option (selecting done task as incomplete).
    elif command_console.lower() == ("unmark"):
        if len(to_do_list) < 1:
            ornament1()
            print(color.YELLOW + "Your list is empty!" + color.END)
            ornament2()
        if len(to_do_list) >= 1:  # List must have, at least, one item to modifying it.
            list_reminder()
            try:
                undone = int(input("\nWhich one do you want to UNMARK as uncomplete? Choose a number: "))
                if "[x]" in to_do_list[undone - 1]:  # When "[ ]" item was unmarked, there is no system output.
                    to_do_list[undone - 1] = to_do_list[undone - 1].replace("[x]", "[ ]", 1)
                    ornament1()
                    print(color.GREEN + "Task changed!" + color.END)
                    ornament2()
            except:
                ornament1()
                print (color.RED + "Invalid sign or number are above the list! Try again." + color.END)   # User's input error.
                ornament2()

    # DELETE option (working on two different ways).
    elif command_console.lower() == ("delete") or command_console.lower() == ("del"):
        decision = input("\nWould you like to REMOVE specific item (""\"""R""\""") or ARCHIVE all done tasks (""\"""A""\""")? ")

        # REMOVING single item from the list.
        if decision.lower() == ("r") or decision.lower() == ("remove"):
            try:
                list_reminder()
                decision = int(input("\nWhich one do you want to REMOVE? Choose a number: "))
                if decision > 0:
                    ornament1()
                    # Fancy alert, that warns user from deleting the item from the list.
                    confirm = input(color.RED + "WARNING! This operation cannot be withdrawn. Are you sure?" + font.BOLD + " (""\"""Y""\""" " + font.END + color.RED + "/" + font.BOLD + " ""\"""N""\""")" + font.END + color.RED + ": " + color.END)
                    ornament2()
                    if confirm.lower() == ("y") or confirm.lower() == ("yes"):  # Ask again about user's decision. 
                        del to_do_list[decision - 1]
                        ornament1()
                        print(color.GREEN + "Done! Task removed!" + color.END)
                        ornament2()
                        loop = 0
                    # Escape mode (back to the main menu).
                    elif confirm.lower() == ("n") or confirm.lower() == ("no"):
                        loop = 0
                else:
                    ornament1()
                    print (color.RED + "Invalid sign or number are above the list! Try again." + color.END)    # User's input error.
                    ornament2()
            except:
                ornament1()
                print (color.RED + "Invalid sign or number are above the list! Try again." + color.END)    # User's input error.
                ornament2()

        # ARCHIVE many items from the list (previously marked as completed).
        elif decision.lower() == ("a") or decision.lower() == ("archive"):
            list_reminder()
            ornament1()
            # Fancy alert, that warns user from deleting all the following tasks from the list.
            confirm = input(color.RED + "WARNING! This operation cannot be withdrawn. Are you sure?" + font.BOLD + " (""\"""Y""\""" " + font.END + color.RED + "/" + font.BOLD + " ""\"""N""\""")" + font.END + color.RED + ": " + color.END)
            ornament2()
            if confirm.lower() == ("y") or confirm.lower() == ("yes"):  # Ask again about user's decision.
                if to_do_list:
                    for done_item in range(len(to_do_list)):
                        for position in range(len(to_do_list)):
                            if to_do_list[position][0:3] == "[x]":
                                del to_do_list[position]
                                break
                ornament1()
                print(color.GREEN + "All complete tasks was removed." + color.END)
                ornament2()
            # Escape mode (back to the main menu).
            elif confirm.lower() == ("n") or confirm.lower() == ("no"):
                loop = 0
        else:
            ornament1()
            print (color.RED + "Your command is invalid!" + color.END)  # Wrong letter or command inside DELETE mode.
            ornament2()

    # EXIT option (consist of saving changes to the file named "List to do.txt" and, after that, shut down the script).
    elif command_console.lower() == ("exit"):
        with open("List to do.txt", "w") as out_file:
            for item_to_do in to_do_list:
                out_file.write(str(item_to_do) + "\n")
            ornament1()
            print("Your list is saved as ""\"""List to do.txt""\"""")
            time.sleep(0.5)
            ornament2()
            print("Good bye!")
            ornament2()
            break

    else:
        ornament1()
        print (color.RED + "Your command is invalid!" + color.END)  # Wrong command inside MAIN mode.
ornament2()
