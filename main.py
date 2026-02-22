import json
import time

file = ""

save =int(input("which save file do you want to load 1 , 2 , or 3: "))

if save == 1:
    file = "save1.json"
elif save == 2:
    file = "save2.json"
elif save == 3:
    file = "save3.json"

time.sleep(0.2)
print()
print("loading file...")
time.sleep(2)
print()
print()

try:
    filename = file
    with open(filename, 'r') as file:
        data = json.load(file)



    print("| Main Menu |")
    print("1. john pork")
    print("2. 67")
    print("3. mustard")
    print("4. Tutorial")
    print("5. save")
    print()
    option = int(input("What would you want to do today? : "))

    if option == 1:
        print("do something idk")

    elif option == 2:
        print("what does this do?")

    elif option == 3:
        print("Idk at this point")

    elif option == 4:
        print("Just mess around")
        print("Idk what this program does")

    elif option == 5:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)






except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")