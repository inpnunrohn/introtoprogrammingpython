# -----------------------------------#
# Title: Home Inventory Collection Script
# Dev: ROHINI N
# Date: May 17,2023
# Changelog: (Who, When, What)
# ROHINI N,05/17/2023,Created Script
# -----------------------------------#
#DATA
#objfile = Represent file
#strData = Data from file
#dicRow = element of dic data
#lstTable = Dic act as table in row
#strMenu = Menu of user action
#strChoice = User choice

#.............processing.....................#
# Declare variables and constants
objFileName = "HomeInventory1.txt"  # File name
lstTable = []  # List to store tasks and priorities

# Load data from file into lstTable
with open(objFileName, "r") as file:
    for line in file:
        task, priority = line.strip().split(",")
        lstTable.append({"Task": task, "Priority": priority})

# Menu-driven program
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = input("Which option would you like to perform? [1 to 4] - ")
    print()

    if strChoice == '1':
        if not lstTable:
            print("No tasks found.")
        else:
            print("******* The current items ToDo are: *******")
            for row in lstTable:
                print(row["Task"] + " (" + row["Priority"] + ")")
            print("*******************************************")

    elif strChoice == '2':
        strTask = input("What is the task? - ").strip()
        strPriority = input("What is the priority? [high|low] - ").strip()
        lstTable.append({"Task": strTask, "Priority": strPriority})
        print("Task added successfully.")

    elif strChoice == '3':
        strKeyToRemove = input("Which TASK would you like removed? - ")
        removed = False
        for row in lstTable:
            if row["Task"] == strKeyToRemove:
                lstTable.remove(row)
                removed = True
                break
        if removed:
            print("The task was removed.")
        else:
            print("Task not found.")

    elif strChoice == '4':
        if not lstTable:
            print("No tasks to save.")
        else:
            with open(objFileName, "w") as file:
                for row in lstTable:
                    file.write(row["Task"] + "," + row["Priority"] + "\n")
            print("Data saved to file.")

    elif strChoice == '5':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")

    print()  # Add an extra line for looks
