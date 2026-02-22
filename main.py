import json
import time



try:
    filename = "save1.json"
    with open(filename, 'r') as file:
        data = json.load(file)



    print("| Main Menu |")
    print("")









except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")