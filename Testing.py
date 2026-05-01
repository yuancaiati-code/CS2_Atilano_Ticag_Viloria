
#Tasks needed to be done by group: Fix errors and make sure they are up to date:
    #1. While loops
    #2. Outputs
    #3. Finish update task function

#This imports all needed modules for code.
import json
import time
from datetime import datetime, timedelta

try:
    #This function is for opening the schedule files, without having to open it again.
    def get_sched(day):
        with open(f'{day}.json','r') as f1:
            return json.load(f1)

    #This function is for saving all updates for schedule files.
    def save_sched(day, data):
        with open(f'{day}.json','w') as f1:
            json.dump(data,f1,indent=3)

    #This function is for validating yes and no inputs.


    # 1. This outputs all the tasks with their subjects and due dates.
    def check_tasks():
        print("Task ------> Subject ------> Due Date & Time ------> Priority ------> Progress ------> Goal ------> Is goal reached? ")
        tasks_to_do = []
        for task in reqs:
            tasks_to_do.append((task["task"], task["subject"], task["due_date_and_time"], task["priority"],
                                task["progress"], task["goal"], task["goal_reached"]))
        for to_do, subject, due_date_and_time, priority, progress, goal, goal_reached in tasks_to_do:
            print(
                f"{to_do}   :   {subject}   :   {due_date_and_time}   :   {priority}   :   {progress}   :   {goal}   :   {goal_reached}")


    # 2. This function is for viewing the schedule.
    def show_sched(chose):
            schedule = get_sched(chose)
            print("Schedule:")
            print("Time -------> Period --------> Teacher")
            day_schedule = []
            for classes in schedule:
                day_schedule.append((classes["time"], classes["period"], classes["teacher"]))
            for clas, period, teacher in day_schedule:
                    print(f"{clas} : {period} : {teacher}")

    # 3. This function makes sure tasks are up to date.
    def update_tasks(res):
        if res == "+":
            print("What would you like to add?")
            new_task = input("- Enter task: ")
            new_sub = input("- Enter subject: ")

            print("When is the due date? ")
            y2 = input("- Enter year(yy)")
            m2 = input("- Enter month(mm)")
            d2 = input("- Enter day(dd)")
            print("- Enter in military time:")
            h2 = input(" > Enter hour(HH)")
            mins2 = input(" > Enter minutes(MM)")

            new_due_date = f"{y2}-{m2}-{d2}, {h2}:{mins2}"
            new_priority = ""
            new_prog = ""

            print("- When do you want this to be finished? ")
            y1 = input("- Enter year(yy)")
            m1 = input("- Enter month(mm)")
            d1 = input("- Enter day(dd)")
            print("- Enter in military time:")
            h1 = input(" > Enter hour(HH)")
            mins1 = input(" > Enter minutes(MM)")

            new_goal = f"{y1}-{m1}-{d1}, {h1}:{mins1}"
            reached = False

            added = {"task": new_task, "subject": new_sub, "due_date": new_due_date, "priority": new_priority, "progress": new_prog, "goal": new_goal, "goal_reached": reached}
            reqs.append(added)


        elif res == "0":
            tsk = input("What task would you like to change? ")
            upd = input("What do you want to change; task, subject, due date, goal, or progress? (t/s/d/g/p): ")
            if upd == "t":
                new_task = input("What will you change it to?: ")
                for task in reqs:
                    if task["task"] == tsk:
                        task["task"] = new_task

            elif upd == "d":
                y = input("- Enter year(yy)")
                m = input("- Enter month(mm)")
                d = input("- Enter day(dd)")
                print("- Enter in military time:")
                h = input(" > Enter hour(HH)")
                mins = input(" > Enter minutes(MM)")

                for task in reqs:
                    if task["task"] == tsk:
                        date = f"{y}-{m}-{d}, {h}:{mins}"
                        task["due_date_and_time"] = date

            if upd == "p":

                prog = int(input("How much have you finished out of a hundred percent? (percent without symbol/not decimal): "))
                if prog > 0:
                    for task in reqs:
                        task["progress"] = "Not started"
                elif prog < 100:
                    for task in reqs:
                        task["progress"] = "In progress"
                elif prog == 100:
                    for task in reqs:
                        task["progress"] = "Finished"
                else:
                    print("That's not a valid input.")


        elif res == "-":
            delete = input("What task would you like to delete? (task): ")
            for task in reqs:
                if delete == task["task"]:
                    reqs.remove(task)


    # 4. This updates classes wanted to change, based on the subject period.
    def update_classes(chose, res):
        while True:
            schedule = get_sched(chose)
            if res == "+":
                print("What would you like to add?")
                new_class = input("Enter period: ")
                h1 = input("- What hour does it start(HH)?: ")
                m1 = input("- What minute does it start(MM)?: ")
                h2 = input("- What hour does it end?(HH)?: ")
                m2 = input("- What minute does it end?(MM)?: ")
                new_teacher = input("Enter teacher: ")
                new_tim = f"{ h1}:{m1} - {h2}:{m2}"
                added = {"time": new_tim, "period": new_class, "teacher": new_teacher}

                schedule.append(added)
            elif res == "0":
                cls = input("What class will be updated (period)?")
                upd = input("What do you wanna change; period, time, or teacher? (p/t/teach): ")
                while True:
                    if upd.lower() in [ "p", "t", "teach"]:
                        break
                    else:
                        print("Invalid input")

                if upd == "p":
                    for classes in schedule:
                        if classes["period"] == cls:
                            new_per = input("What period would you want to change it to?: ")
                            classes["period"] = new_per
                        elif not classes["period"]:
                            print("Invalid input")

                elif upd == "t":
                    print("Please enter the following in military time: ")
                    h1 = input("- What hour does it start(HH)?: ")
                    m1 = input("- What minute does it start(MM)?: ")
                    h2 = input("- What hour does it end?(HH)?: ")
                    m2 = input("- What minute does it end?(MM)?: ")
                    for classes in schedule:
                        if classes["period"] == cls:
                            tim = f"{h1}:{m1} - {h2}:{m2}"
                            classes["time"] = tim

                        elif not classes["period"]:
                                print("Invalid input")

                elif upd == "teach":
                    for classes in schedule:
                        if classes["period"] == cls:
                            new_tea = input("Who is your knew teacher? ")
                            classes["teacher"] = new_tea

            elif res == "-":
                delete = input("What class would you like to delete? (period): ")
                for classes in schedule:
                    if delete == classes["period"]:
                        schedule.remove(classes)



            save_sched(chose, schedule)

    #This makes sure that students are notified for subjects due in a week, day, and hour.
    def notify():
        time_list = []
        goal_list = []
        day_goal = []
        tasks_lst = []
        tasks_lst2 = []
        for task in reqs:
            due = task["due_date_and_time"]
            due_date = datetime.strptime(due, "%Y-%m-%d, %H:%M")
            goal = task["goal"]
            set_goal = datetime.strptime(goal, "%Y-%m-%d, %H:%M")
            days = due_date - set_goal
            time_now = datetime.now()
            days_from_now = due_date - time_now
            time_left = due_date - time_now
            time_list.append(time_left)
            tasks_lst.append((time_left, task))
            goal_list.append(days)
            day_goal.append(days_from_now)
            tasks_lst2.append((goal_list, day_goal, task))

        one_day_left = []
        one_week_left = []
        one_hour_left = []
        overdue = []
        for time_left, task in tasks_lst:
            if timedelta(days=0) < time_left <= timedelta(days=1):
                one_day_left.append((time_left, task))
                task["priority"] = "High"
            elif timedelta(days=5) < time_left <= timedelta(days=7):
                one_week_left.append((time_left, task))
                task["priority"] = "Medium"
            elif timedelta(minutes=1) < time_left <= timedelta(minutes=60):
                one_hour_left.append((time_left, task))
                task["priority"] = "Critical"
            elif timedelta(minutes=1) > time_left:
                overdue.append((time_left, task))
                task["priority"] = "Cooked"

        for goal_list, day_goal, task in tasks_lst2:
            if task["progress"] == "Submitted":
                if goal_list >= day_goal:
                    task["goal_reached"] = True
                else:
                    task["goal_reached"] = False
            else:
                task["goal_reached"] = False


        print("Tasks due in one week:")
        if not one_week_left:
            print(None)
        else:
            for time_left, task in one_week_left:
                print(f"{task['task']} - {task['subject']}")

        print("Tasks due in one day:")
        if not one_day_left:
            print(None)
        else:
            for sub, task in one_day_left:
                print(f"{task['task']} - {task['subject']}")

        print("Tasks due within an hour:")
        if not one_hour_left:
            print(None)

        else:
            for sub, task in one_hour_left:
                print(f"{task['task']} - {task['subject']}")

        if not overdue:
            print(None)

        else:
            for sub, task in overdue:
                print(f"{task['task']} - {task['subject']}")


    #This is for the user interface, which decides what is needed to access based on the user's decision.
    def menu():
        while True:
            time.sleep(2)
            print("")
            print("Menu: \n 1. Check Tasks\n 2. Check Schedule\n 3. Update Class\n 4. Update Tasks\n 0. Exit")
            time.sleep(0.5)
            while True:
                ans = (input(" \nWhat do you want to do? (1/2/3/4/0): "))
                if ans in ["1","2","3","4","0"]:
                    ans = int(ans)
                    break
                else:
                    print("Not a valid input")

            if ans == 1:
                check_tasks()

            elif ans == 2 or 3:
                while True:
                    choice = input("What day do you want?\n - Monday\n - Tuesday\n - Wednesday\n - Thursday\n - Friday\n - Back to menu\nEnter (M/T/W/Th/F/Menu): ")
                    if choice.lower() in["m", "t", "w", "th", "f", "menu"]:
                        break
                    else:
                        print("Not a valid input")

                if ans == 2:
                    show_sched(choice)

                elif ans == 3:
                    response = input("Would you like to add, change, or delete from the schedule? (+, 0, -): ")
                    update_classes(choice, response)

                elif choice in ["Menu", "menu"]:
                    break




            elif ans == 4:
                response = input("Would you like to add, change, or delete from the schedule? (+, 0, -): ")
                update_tasks(response)

            elif ans == 0:
                break




    # This opens the json file for tasks.
    with open('tasks.json', 'r') as f:
        reqs = json.load(f)
    with open('tasks.json', 'w') as f:
        json.dump(reqs, f, indent=3)


#Opening
    print("Welcome to ChronoSmart!")
    time.sleep(1)
    print("I am Chron, here to help you manage your time")
    time.sleep(1)
    print("Just enter the number for the corresponding choices.")
    time.sleep(1)
    for i in range(3):
        print("")

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
    print(r"        /__________/\  /__/\___/_/ /  /__/ /\__\ -- /_________/ /  /_/ /  \__/ /  /_________/ /")
    print(r"        \__________\/  \__\/   \_\/ - \__\/- \__\ - \_________\/ - \_\/ -- \_\/ - \_________\/")
    print(r"                                    []---- -------------------------------------- ----[]")
    print(r"                                     []--- 8 ___________------------------------- 4 --[]      __")
    print(r"                                       []-- / _________/\ --------------------------[]     __/ /\__")
    print(r"                                           /_/\________\/ __ ________ - ______ _ ]  __ __ /__   __/\ ")
    print(r"                                          _\_______  /\  / // /  /  /\ /  /\//  /\ / //_/\\/ /\__\/")
    print(r"                                         /_/\_____/_/ //____/__/__/ //_____   / // /\\_\/ /____/\  ")
    print(r"                                         \__________\/ \__________\/ \_____\\_\/ \_\/     \____\/ ")
    time.sleep(2)
    notify()
    print("")
    print("Take a look around, this is our menu:")
    menu()

#Except, me :3
except FileNotFoundError:
    print("Error: The file 'data.json' was not found")
except json.JSONDecodeError as e:
    print("Failed to decode JSON: {e}")