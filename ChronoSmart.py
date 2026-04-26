#Tasks needed to be done by group: Fix errors and make sure they are up to date:
    #1. While loops
    #2. Outputs
    #3. Function flow
    #4. Finish update task function

import json
import time
from datetime import datetime, timedelta

try:
    def get_sched(day):
        with open(f'{day}.json','r') as f1:
            return json.load(f1)

    def save_sched(day, data):
        with open(f'{day}.json','w') as f1:
            json.dump(data,f1,indent=3)

    def show_sched(chose):
            schedule = get_sched(chose)
            print("Schedule:")
            print("Time -------> Period --------> Teacher")
            day_schedule = []
            for classes in schedule:
                day_schedule.append((classes["time"], classes["period"], classes["teacher"]))
            for clas, period, teacher in day_schedule:
                    print(f"{clas} : {period} : {teacher}")

    def check_tasks():
        print("Task ------> Subject ------> Due Date & Time ------> Priority ------> Progress ------> Goal ------> Is goal reached? ")
        tasks_to_do = []
        for task in reqs:
            tasks_to_do.append((task["task"], task["subject"], task["due_date_and_time"], task["priority"], task["progress"], task["goal"], task["goal_reached"]))
        for to_do, subject, due_date_and_time, priority, progress, goal, goal_reached in tasks_to_do:
            print(f"{to_do}   :   {subject}   :   {due_date_and_time}   :   {priority}   :   {progress}   :   {goal}   :   {goal_reached}")

    def update_classes(chose, class_update, update, change):
        while True:
            schedule = get_sched(chose)
            if chose in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "monday"]:
                for classes in chose:
                    if class_update == classes["time"]:
                        classes[update] = change
            save_sched(chose, schedule)


    def update_tasks():
       pass


    #This is for the user interface, which decides what is needed to access based on the user's decision.
    def menu():
        while True:
            print(r"                                         =========                       ========")
            print(r"                                       (============)                 (============)")
            print(r"                                      =============== ------  ------  ==============")
            print(r"                                               []---------- 12 -----------[]")
            print(r"                                            []  ------------A  ------------- []")
            print(r"                                         []-- 11 -----------| ^------------ 1 ---[]")
            print(r"                                      []--------------------| |------------- ------[]")
            print(r"                                     []- -------------------| |-------------------- -[]")
            print(r"            __________     __      __ --  _________ --- __________ --- __ ---- __ --  __________")
            print(r"           / ________/\   / /\    / /\ - /   __   /\ - / ______  /\ _ /  \    / /\ - / ______  /\ ")
            print(r"          / /\_______\/  / /__\__/ / /  /     ___/ /  / /\____/ / /  / /\ \  / / /  / /\____/ / /")
            print(r"         / /_/______    /  _____/ / /  /  /\  \__\/  / /_/___/ / /  / / /\ \/ / /  / /_/___/ / /")
            print(r"        /__________/\  /__/\___/_/ /  /__/  \__\ -- /_________/ /  /_/ /  \__/ /  /_________/ /")
            print(r"        \__________\/  \__\/   \_\/ - \__\ - \__\ - \_________\/ - \_\/ -- \_\/ - \_________\/")
            print(r"                                    []---- -------------------------------------- ----[]")
            print(r"                                     []--- 8 ___________------------------------- 4 --[]      __")
            print(r"                                       []-- / _________/\ --------------------------[]     __/ /\__")
            print(r"                                           /_/\________\/ __ ________ - ______ _ ]  __ __ /__   __/\ ")
            print(r"                                          _\_______  /\  / // /  /  /\ /  /\//  /\ / //_/\\/ /\__\/")
            print(r"                                         /_/\_____/_/ //____/__/__/ //_____   / // /\\_\/ /____/\  ")
            print(r"                                         \__________\/ \__________\/ \_____\\_\/ \_\/     \____\/ ")
            time.sleep(2)


            ans = int(input("Menu: \n 1. Check Tasks\n 2. Check Schedule\n 3. Update Class\n 4. Update Tasks\n 0. Exit\nWhat do you want to do? (1,2,3,4, 0): "))
            if ans == 1:
                check_tasks()

            elif ans == 2 or 3:
                choice = str(input("What day do you want?\n 1. Monday\n 2. Tuesday\n 3. Wednesday\n 4. Thursday\n 5. Friday\n 6. Back to menu\nEnter (M, T, W, Th, F): "))
                if choice in["m", "t", "w", "th", "f", "M", "T", "W", "Th", "TH", "F"]:
                    choice = choice.lower()

                    if ans == 2:
                        show_sched(choice)

                    elif ans == 3:
                        cls= input("What class will be updated(time)?")
                        upd = input("What do you wanna change (period, or teacher)?")
                        cng = input("What will you change it to?")
                        update_classes(choice, cls,  upd, cng)

                elif choice in ["Menu", "menu"]:
                    response = input("Would you like to proceed to menu (Y/N)? ")
                    if response in ["Y", "y", "N", "n"]:
                        if response.upper() == "Y":
                            break

                else:
                    print("Not a valid input")
                    response = input("Would you like to continue (Y/N)? ")
                    if response in list["Y", "y", "N", "n"]:
                        if response.upper() == "N":
                            break

            elif ans == 4:
                pass

            elif ans == 0:
                response = input("Are you sure you want to exit? (Y/N)")
                if response in list["Y", "y", "N", "n"]:
                    break

            else:
                print("Invalid input.")

    with open('tasks.json', 'r') as f:
        reqs = json.load(f)
    with open('tasks.json', 'w') as f:
        json.dump(reqs, f, indent=3)

    def notify():
        time_list = []
        for task in reqs:
            due = task["due_date_and_time"]
            due_date = datetime.strptime(due, "%Y-%m-%d, %H:%M")
            time_now = datetime.now()
            time_left = due_date - time_now
            time_list.append(time_left)


        one_day_left = []
        one_week_left = []
        one_hour_left = []
        for time_left in time_list:
            if timedelta(days=0) < time_left <= timedelta(days=1):
                one_day_left.append(time_left)
            elif timedelta(days=5) < time_left <= timedelta(days=7):
                one_week_left.append(time_left)
            elif timedelta(minutes=59) < time_left <= timedelta(minutes=60):
                one_hour_left.append(time_left)

        print("Tasks due in one week:")
        if not one_week_left:
            print("None")

        else:
            for sub in one_week_left:
                print(f"{sub}\n")

        print("Tasks due in one day:")
        if not one_day_left:
            print("None")
        else:
            for sub in one_day_left:
                print(f"{sub}\n")

        print("Tasks due in one hour:")
        if not one_hour_left:
            print("None")

        else:
            for sub in one_hour_left:
                print(f"{sub}\n")


    print("Welcome to ChronoSmart!")
    time.sleep(1)
    print("I am Chron, here to help you manage your time")
    time.sleep(1)
    print("Just enter the number for the corresponding choices.")
    time.sleep(1)
    print("Take a look around, this is our menu:")
    time.sleep(2)
    notify()
    menu()

except FileNotFoundError:
    print("Error: The file 'data.json' was not found")
except json.JSONDecodeError as e:
    print("Failed to decode JSON: {e}")