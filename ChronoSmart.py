#Import json for files, and import datetime to get dates in actual life.
import json
import time
from datetime import datetime
try:
    #Open all files needed.
    with open('monday.json', 'r') as file:
        mon = json.load(file)
    with open('monday.json', 'w') as file:
        json.dump(mon, file, indent=3)
    with open('tuesday.json', 'r') as file:
        tue = json.load(file)
    with open('tuesday.json', 'w') as file:
        json.dump(tue, file, indent=3)
    with open('wednesday.json', 'r') as file:
        wed = json.load(file)
    with open('wednesday.json', 'w') as file:
        json.dump(wed, file, indent=3)
    with open('thursday.json', 'r') as file:
        thu = json.load(file)
    with open('thursday.json', 'w') as file:
        json.dump(thu, file, indent=3)
    with open('friday.json', 'r') as file:
        fri = json.load(file)
    with open('friday.json', 'w') as file:
        json.dump(fri, file, indent=3)
    filename = "tasks.json"
    with open(filename, 'r') as file:
        reqs = json.load(file)
    with open(filename, 'w') as file:
        json.dump(reqs, file, indent=3)

    #1. Define function to print individual schedules according to user's preference on which schedule is needed.
    def show_sched():
        while True:
            user_input = int(input("\nWhat schedule would you like to see?\n 1. Monday\n 2. Tuesday \n 3. Wednesday \n 4. Thursday \n 5. Friday \n 0. Menu\nEnter(1,2,3,4,5,0): "))
            if user_input in list[1,2,3,4,5]:
                print("Schedule:")
                print("Time -------> Period --------> Teacher")
                if user_input == 1:
                    monday_schedule = []
                    for classes in mon:
                        monday_schedule.append((classes["time"], classes["period"], classes["teacher"]))
                    for clas, period, teacher in monday_schedule:
                        print(f"{clas} : {period} : {teacher}")

                elif user_input == 2:
                    tuesday_schedule = []
                    for classes in tue:
                        tuesday_schedule.append((classes["time"], classes["period"], classes["teacher"]))
                    for clas, period, teacher in tuesday_schedule:
                        print(f"{clas} : {period} : {teacher}")

                elif user_input == 3:
                    wednesday_schedule = []
                    for classes in wed:
                        wednesday_schedule.append((classes["time"], classes["period"], classes["teacher"]))
                    for clas, period, teacher in wednesday_schedule:
                        print(f"{clas} : {period} : {teacher}")

                elif user_input == 4:
                    thursday_schedule = []
                    for class_adelfa in thu:
                        thursday_schedule.append((class_adelfa["time"], class_adelfa["period"], class_adelfa["teacher"]))
                    for class_meet, period, teacher in thursday_schedule:
                        print(f"{clas} : {period} : {teacher}")

                elif user_input == 5:
                    friday_schedule = []
                    for classes in fri:
                        friday_schedule.append((classes["time"], classes["period"], classes["teacher"]))
                    for clas, period, teacher in friday_schedule:
                        print(f"{clas} : {period} : {teacher}")

            #If the user types in 0, this asks the user if he or she would want to go back to the menu or not.
            elif user_input == 0  :
                response = input("Would you like to proceed to menu (Y/N)? ")
                if response in list["Y", "y", "N", "n"]:
                    if response.upper() == "Y":
                        break

            else:
                print("Not a valid input")
                response = input("Would you like to continue (Y/N)? ")
                if response in list["Y", "y", "N", "n"]:
                    if response.upper() == "N":
                        break

    #2. This uses a similar structure for checking schedules, except it checks all tasks, regardless of what day.
    def check_tasks():
        print("Task ------> Subject ------> Due Date & Time ------> Priority ------> Progress ------> Goal ------> Is goal reached? ")
        tasks_to_do = []
        for task in reqs:
            tasks_to_do.append((task["task"], task["subject"], task["due_date_and_time"], task["priority"], task["progress"], task["goal"], task["goal_reached"]))
        for to_do, subject, due_date_and_time, priority, progress, goal, goal_reached in tasks_to_do:
            print(f"{to_do}   :   {subject}   :   {due_date_and_time}   :   {priority}   :   {progress}   :   {goal}   :   {goal_reached}")

    #3. This is for updating the schedules, by either deleting or changing a schedule.
    def update_classes():
        while True:
            day = int(input("What day do you want to update?\n 1. Monday\n 2. Tuesday\n 3. Wednesday\n 4. Thursday\n 5. Friday\n 0. Back to menu\nEnter (1,2,3,4,5,0): "))
            if day in list[1,2,3,4,5]:
                class_update = input("What class will be updated(time)?")
                update = input("What do you wanna change (period, or teacher)?")
                change = input("What will you change it to?")
                if day == 1:
                    for classes in mon:
                        if class_update == classes["time"]:
                            classes[update] = change

                elif day == 2:
                    for classes in tue:
                        if class_update == classes["time"]:
                            classes[update] = change

                elif day == 3:
                    for classes in wed:
                        if class_update == classes["time"]:
                            classes[update] = change

                elif day == 4:
                    for classes in thu:
                        if class_update == classes["time"]:
                            classes[update] = change

                elif day == 5:
                    for classes in fri:
                        if class_update == classes["time"]:
                            classes[update] = change

            elif day == 0:
                response = input("Would you like to go back to the menu (Y/N)? ")
                if response in list["Y", "y", "N", "n"]:
                    if response.upper() == "Y":
                        break

            else:
                print("Invalid input")
                response = input("Would you like to continue (Y/N)? ")
                if response in list["Y", "y", "N", "n"]:
                    if response.upper() == "N":
                        break

    #4.\
    #    def update_tasks():
    #    for task in tasks:
    #        if task["progress"] == "Submitted":
    #            del task[tasks.index(tasks)]
    def update_tasks():
       pass


    #This is for the user interface, which decides what is needed to access based on the user's decision.
    def menu():
        while True:
            ans = int(input("Menu: \n 1. Check Tasks\n 2. Check Schedule\n 3. Update Class\n 4. Update Tasks\n 0. Exit\nWhat do you want to do? (1,2,3,4, 0): "))
            if ans == 1:
                check_tasks()

            elif ans == 2:
                show_sched()

            elif ans == 3:
                update_classes()

            elif ans == 4:
                pass

            elif ans == 0:
                response = input("Are you sure you want to exit? (Y/N)")
                if response in list["Y", "y", "N", "n"]:
                    break

            else:
                print("Invalid input.")

    print("Welcome to ChronoSmart!")
    time.sleep(1)
    print("I am Chron, here to help you manage your time")
    time.sleep(1)
    print("Just enter the number for the corresponding choices.")
    time.sleep(1)
    print("Take a look around, this is our menu:")
    time.sleep(1)
    menu()
except FileNotFoundError:
    print("Error: The file 'data.json' was not found")
except  json.JSONDecodeError as e:
    print("Failed to decode JSON: {e}")