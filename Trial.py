import json
try:
    enter = str(input("Enter day: (M, T, W, Th, F"))
    if enter in["M", "T", "W", "Th", "F" , "m", "t", "w", "th", "TH", "f"]:
        enter =  enter.lower()
        with open(f'{enter}.json', 'r') as file:
            schedule = json.load(file)
        with open(f'{enter}', 'w') as file:
            json.dump(schedule, file, indent =3 )
        print("Schedule:")
        print("Time -------> Period --------> Teacher")
        day_schedule = []
        for classes in enter:
            day_schedule.append((classes["time"], classes["period"], classes["teacher"]))
        for clas, period, teacher in day_schedule:
            print(f"{clas} : {period} : {teacher}")



except FileNotFoundError:
    print("Error: The file 'data.json' was not found")
except json.JSONDecodeError as e:
    print("Failed to decode JSON: {e}")