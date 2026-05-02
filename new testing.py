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

    #This prints out tasks based on their name, subject, due date, priority, goal, status of submission, and if the goal put was reached.
    def check_tasks():
        print("Task ------> Subject ------> Due Date & Time ------> Priority ------> Progress ------> Goal ------> Status of Submission ------> Is goal reached? ")
        #It first makes a new list that takes in all values with the specific key.
        tasks_to_do = []
        for task in reqs:
            tasks_to_do.append((task["task"], task["subject"], task["due_date_and_time"], task["priority"],
                                task["progress"], task["goal"], task["submission_status"], task["goal_reached"]))
        #Then from that list, it outputs all of them through an f string.
        for to_do, subject, due_date_and_time, priority, progress, goal, submission_status, goal_reached in tasks_to_do:
            print(f"{to_do} : {subject} : {due_date_and_time} : {priority} : {progress} : {goal} : {submission_status} : {goal_reached}")

    #This serves the same function for checking tasks, except it shows a specific day's schedule, based on what the user wants to see.
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

        #This updates the task automatically to remove tasks that are submitted.
        for goal_list, day_goal, task in tasks_lst2:
            if task["submission_status"]:
                if goal_list >= day_goal:
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

    #This is where the menu is.
    #It calls all sorts of functions based on the user's input.
    def menu():
        time.sleep(2)
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

        print("Menu: \n 1. Check Tasks\n 2. Check Schedule\n 3. Update Class\n 4. Update Tasks\n 0. Exit")
        time.sleep(0.5)
        ans = int(input(" \nWhat do you want to do? (1/2/3/4/0): "))
        #If the user inputs number 1, it will call the function check_tasks()
        if ans == 1:
            check_tasks()

        elif ans == 2:

    with open('tasks.json', 'r') as f:
        reqs = json.load(f)
    with open('tasks.json', 'w') as f:
        json.dump(reqs, f, indent=3)

    yes = True
    while yes:
        menu()
        yes = validate()
except FileNotFoundError:
    print("Error: The file 'data.json' was not found")
except json.JSONDecodeError as e:
    print("Failed to deco/de JSON: {e}")