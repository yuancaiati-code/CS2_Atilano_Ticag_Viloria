import json
import time
from datetime import datetime, timedelta
try:
    #This function gets the schedule from separate files using variables
    #The parameter "day" is the name of the json file.
    def get_sched(day):
        with open(f'{day}.json','r') as f1:
            return json.load(f1)

    #This saves schedule updates.
    def save_sched(day, data):
        with open(f'{day}.json','w') as f1:
            json.dump(data,f1,indent=3)

    # This validates if the user wants to continue the specific function, or the whole application itself.
    def validate():
        res = input("Would you like to continue? (Y/N): ")
        if res in ["Y", "y", "N", "n"]:
            if res.upper() == "N":
                return False
            elif res.upper() == "Y":
                return True
        else:
            return validate()

    #1.) This prints out tasks based on their name, subject, due date, priority, goal, status of submission, and if the goal put was reached.
    def check_tasks():
        print("Task ------> Subject ------> Due Date & Time ------> Priority ------> Progress ------> Goal ------> Status of Submission ------> Is goal reached? ")
        #It first makes a new list that takes in all values with the specific key.
        tasks_to_do = []
        win = 0
        accomplished = 0
        count = 0
        for task in reqs:
            tasks_to_do.append((task["task"], task["subject"], task["due_date_and_time"], task["priority"],
                                task["progress"], task["goal"], task["submission_status"], task["goal_reached"]))
            count = + 1
            if task["goal_reached"]:
                win = +1
            if task["progress"] == "Finished":
                accomplished = + 1

        #These are counters for finished tasks.

        #Then from that list, it outputs all of them through an f string.
        for to_do, subject, due_date_and_time, priority, progress, goal, submission_status, goal_reached in tasks_to_do:
            print(f"{to_do} : {subject} : {due_date_and_time} : {priority} : {progress} : submitted before - {goal} : {submission_status} : {goal_reached}")

        print("")

        #This commends the user for finished tasks
        if win == count:
            print("You accomplished all your tasks based on your goal!!! Maintain your discipline.")

        if count == 0:
            print("Congratulations on submitting all your tasks!!")

        if accomplished > 0 and win < count:
            print(f"Good job for finishing {accomplished} tasks. Regardless of not finishing them all based on your goal, it's great to see that you finished them")
            if accomplished == 1 and win == 0:
                print(f"Good job for finishing 1 task. Regardless of not finishing them all based on your goal, it's great to see that you finished one already. ")

        if 0 < win < count:
            if win > 1:
                print(f"You accomplished {win} tasks based on your goal! Keep going! You can do this!")

            elif win == 1:
                print("You have accomplished 1 task based on your goal! This is a stepping stone for success. Keep it up!")

        print("")

    #2.) This serves the same function for checking tasks, except it shows a specific day's schedule, based on what the user wants to see.
        #The parameter "chose" is the name of the json file which could be in the following: m, t, w, th, f
    def show_sched(chose):
        #This calls the function that opens the file
        schedule = get_sched(chose)
        #Then it is now printed.
        print("Schedule:")
        print("Time -------> Period --------> Teacher")
        day_schedule = []
        for classes in schedule:
            day_schedule.append((classes["time"], classes["period"], classes["teacher"]))
        for clas, period, teacher in day_schedule:
                print(f"{clas} : {period} : {teacher}")

    #3.) This is for updating tasks.
        #It uses the parameter "res" which gets the choice of the user, regardless of whether he or she wants to add, change, or delete a task.
    def update_tasks(res):
        if res == "+":
            print("What would you like to add?")
            #This gets the new task and subject.
            new_task = input("- Enter task: ")
            new_sub = input("- Enter subject: ")

            #This is where the due date is:
            print("When is the due date? ")
            y2 = input("- Enter year(yy)")
            m2 = input("- Enter month(mm)")
            d2 = input("- Enter day(dd)")
            print("- Enter in military time:")
            h2 = input(" > Enter hour(HH)")
            mins2 = input(" > Enter minutes(MM)")

            # Since our format is %Y-%m-%d, %H:%M, the users input will be put here.
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
            new_submission_status = False
            reached = False

            added = {"task": new_task, "subject": new_sub, "due_date": new_due_date, "priority": new_priority, "progress": new_prog, "goal": new_goal, "submission status": new_submission_status, "goal_reached": reached}
            reqs.append(added)


        #This then changes a specific task's aspect.
        elif res == "0":
            #This determines which task needs to be updated
            tsk = input("What task would you like to change? ")
            upd = input("What do you want to change; task, subject, due date, progress, goal or submission status?? (t/s/d/p/g/ss): ")

            if upd in ["T", "S", "D", "P", "G", "SS", "Ss", "t", "s", "d", "p", "g", "ss"]:
                upd = upd.lower()
                #This updates the task name.
                if upd == "t":
                    new_task = input("What will you change it to?: ")
                    for task in reqs:
                        if task["task"] == tsk:
                            task["task"] = new_task

                #This updates the task's due date and hour of due submission.
                elif upd == "d" or upd == "g":
                    y = input("- Enter year (yy): ")
                    m = input("- Enter month (mm): ")
                    d = input("- Enter day (dd): ")
                    print("- Enter in military time:")
                    h = input(" > Enter hour (HH): ")
                    mins = input(" > Enter minutes (MM): ")

                    if upd == "d":
                        for task in reqs:
                            if task["task"] == tsk:
                                date = f"{y}-{m}-{d}, {h}:{mins}"
                                task["due_date_and_time"] = date

                    else:
                        for task in reqs:
                            if task["task"] == tsk:
                                date = f"{y}-{m}-{d}, {h}:{mins}"
                                task["goal"] = date

                #This updates the progress of the task, based on the whole number percentage of how much is done.
                elif upd == "p":
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
                        print("Invalid input.")

                elif upd == "ss":
                    sub_stats = input("Did you submit this task? (Y/N): ")
                    if sub_stats in ["Y", "y", "n", "N"]:
                        sub_stats = sub_stats.lower()
                        for task in reqs:
                            if task["task"] == tsk:
                                if sub_stats == "y" :
                                    task["submission_status"] = True
                                else:
                                    task["submission_status"] = False
                    else:
                        print("Invalid input")

                else:
                    print("Invalid input.")


            #This deletes a task manually, even if it isn't marked as True in submission status.
        elif res == "-":
            delete = input("What task would you like to delete? (task): ")
            for task in reqs:
                if delete == task["task"]:
                    reqs.remove(task)
                else:
                    print("Invalid input")
            #This automatically deletes all submitted tasks.
        for task in reqs:
            if task["submission_status"]:
                reqs.remove(task)

        with open('tasks.json', 'w') as f:
            json.dump(reqs, f, indent=3)



    #4. This updates classes for adding, changing, or deleting a task.
        #The parameter chose is for the specific day json file, and res is the user's choice of update.
    def update_classes(chose, res):
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
            if upd in ["P", "p", "T", "t", "teach", "Teach", "TEACH"]:
                upd = upd.lower()
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
            else:
                print("Invalid input.")
                validate()

        elif res == "-":
            delete = input("What class would you like to delete? (period): ")
            for classes in schedule:
                if delete == classes["period"]:
                    schedule.remove(classes)

        else:
            print("Invalid input.")
            validate()

        save_sched(chose, schedule)


    #This function is for notifying the user about tasks close to the due date.
    def notify():
        #These lists are important for saving the due dates.
        time_list = []
        goal_list = []
        day_goal = []
        tasks_lst = []
        tasks_lst2 = []
        for task in reqs:
            #This gets the due_date from the json file.
            due = task["due_date_and_time"]
            #This formats the string into time.
            due_date = datetime.strptime(due, "%Y-%m-%d, %H:%M")
            #This is the wanted submission date of the user.
            goal = task["goal"]
            #This formats the string into time.
            set_goal = datetime.strptime(goal, "%Y-%m-%d, %H:%M")
            #This determines how many days the task should be done before submitting according to when the user wants it finished.
            days = due_date - set_goal
            #This gets the current time.
            time_now = datetime.now()
            days_from_now = due_date - time_now
            # This determines if the task should be notified to the user as a warning.
            time_left = days
            time_list.append(time_left)
            #This saves the items in tuples or pairs in a list.
            tasks_lst.append((time_left, task))
            goal_list.append(days)
            day_goal.append(days_from_now)
            tasks_lst2.append((goal_list, day_goal, task))

        one_day_left = []
        one_week_left = []
        one_hour_left = []
        overdue = []

        #This checks the tasks that are due within the week, within a day, within an hour, and overdue
        for time_left, task in tasks_lst:
            if timedelta(days=0) < time_left <= timedelta(days=1):
                one_day_left.append((time_left, task))
                task["priority"] = "High"
            elif timedelta(days=2) < time_left <= timedelta(days=7):
                one_week_left.append((time_left, task))
                task["priority"] = "Medium"
            elif timedelta(minutes=1) < time_left <= timedelta(minutes=60):
                one_hour_left.append((time_left, task))
                task["priority"] = "Critical"
            elif timedelta(minutes=1) > time_left:
                overdue.append((time_left, task))
                task["priority"] = "Cooked"

        #This updates if the user's goal is achieved.
        for goal_list, day_goal, task in tasks_lst2:
            if task["progress"] == "Finished":
                if goal_list <= day_goal:
                    task["goal_reached"] = True
                else:
                    task["goal_reached"] = False
            else:
                task["goal_reached"] = False


        #This is the notifying stage that shows the user what he or she has to finish.
        #If there is nothing saved in the lists of tasks due, it prints out "None"
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

        with open('tasks.json', 'w') as f:
            json.dump(reqs, f, indent=3)

    #This is where the menu is.
    #It calls all sorts of functions based on the user's input.
    def menu():
        time.sleep(1)
        print("")
        print("=" * 138)
        print("                                       _____________________________________________")
        print(r"                                     [_____________________________________________]")
        print(r"                                        |WW|     //===================\\     |WW|")
        print(r"                                        |  |   //                       \\   |  |")
        print(r"                                        |  |  ||                    | |  ||  |  |")
        print(r"                                        |  |  ||                    | |  ||  |  |")
        print(r"                                        |  |  ||                    | |  ||  |  |")
        print(r"                                        |  |  ||                    | |  ||  |  |")
        print(r"                                        |  |  ||                    | |  ||  |  |")
        print(r"                                        |  |  ||~~~~~~~~~~~~~~~~~~~~|-|~~||  |  |")
        print(r"                                        |  |  ||XXXXXXXXXXXXXXXXXXXX| |XX||  |  |")
        print(r"                                        |  |  ||_________________________||  |  |")
        print(r"                                        |  |   \|         MENU          |//  |  |")
        print(r"                                        |  |    |1. Check tasks         |/   |  |")
        print(r"                                        |  |    |2. Check schedule      |    |  |")
        print(r"                                        |  |    |3. Update tasks        |    |  |")
        print(r"                                        |  |    |4. Update schedule     |    |  |")
        print(r"                                        |  |    |_______________________|    |  |")
        print(r"                                        |  |            //  **  \\           |  |")
        print(r"                                        |  |          //    *  \  \\         |  |")
        print(r"                                        |  |        //      *    \  \\       |  |")
        print(r"                                        |  |      //        *     \   \\     |  |")
        print(r"                                        |  |    //           `     \   \\    |  |")
        print(r"                                        |  |   //         A|##|AAA      \\   |  |")
        print(r"                                        |  |  ||    A AAAAAAAAAAAAAA| |  ||  |  |")
        print(r"                                        |  |  || AAAAAAAAAAAAAAAAAAA| |AA||  |  |")
        print(r"                                        |  |  ||XXXXXXXXXXXXXXXXXXXX| |XX||  |  |")
        print(r"                                        |  |  ||XXXXXXXXXXXXXXXXXXXX| |XX||  |  |")
        print(r"                                        |  |  ||XXXXXXXXXXXXXXXXXXXX| |XX||  |  |")
        print(r"                                        |  |  ||XXXXXXXXXXXXXXXXXXXX| |XX||  |  |")
        print(r"                                        |  |  ||XXXXXXXXXXXXXXXXXXXX| |XX||  |  |")
        print(r"                                        |  |  ||XXXXXXXXXXXXXXXXXXXX| |XX||  |  |")
        print(r"                                        |  |   \\xxxxxxxxxxxxxxxxxxxxxxx//   |  |")
        print(r"                                       _|MM|_____\\===================//_____|MM|_")
        print(r"                                      [___________________________________________]")
        print("=" * 138)

        time.sleep(0.5)
        ans = int(input(" \nWhat do you want to do? (1/2/3/4/0): "))
        #If the user inputs number 1, it will call the function check_tasks()
        if ans == 1:
            check_tasks()

        #This uses the same json files, so we put it in one option
        elif ans == 2 or ans == 4:
            choice = input("What day do you want?\n - Monday\n - Tuesday\n - Wednesday\n - Thursday\n - Friday\n - Back to menu\nEnter (M/T/W/Th/F/Menu): ")
            if choice in ["m", "t", "w", "th", "f", "M", "T", "W", "Th", "TH", "F"]:
                choice = choice.lower()

            #This shows the schedule of the day.
            if ans == 2:
                show_sched(choice)

            elif ans == 4:
                response = input("Would you like to add, change, or delete from the schedule? (+, 0, -): ")
                update_classes(choice, response)

            elif ans in ["Menu", "menu"]:
                menu()

        elif ans == 3:
            response = input("Would you like to add, change, or delete from the schedule? (+, 0, -): ")
            update_tasks(response)

        elif ans == 0:
            pass

        else:
            print("Invalid input.")

    with open('tasks.json', 'r') as f:
        reqs = json.load(f)

        # Opening
        print("Welcome to ChronoSmart!")
        time.sleep(1)
        print("I am Chron, here to help you manage your time")
        time.sleep(1)
        print("Just enter the number for the corresponding choices.")
        time.sleep(1)
        print("")
        print("=" * 138)
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
        print(r"                                          _\_______  /\  / // /  /  /\ /  /\//  /\ / //_/\\/ /1\__\/")
        print(r"                                         /_/\_____/_/ //____/__/__/ //_____   / // /\\_\/ /____/\  ")
        print(r"                                         \__________\/ \__________\/ \_____\\_\/ \_\/     \____\/ ")
        print("")
        print("=" * 138)
        time.sleep(3)
        notify()
        print("")
        time.sleep(1)
        print("Take a look around, this is our menu:")

    yes = True
    while yes:
        menu()
        yes = validate()

except FileNotFoundError:
    print("Error: The file 'data.json' was not found")
except json.JSONDecodeError as e:
    print("Failed to deco/de JSON: {e}")