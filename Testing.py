import json
import time
from datetime import datetime, timedelta
try:
    def validate():
        res = input("Would you like to continue? (Y/N)")
        if res in ["Y", "y", "N", "n"]:
            if res.upper() == "N":
                return False
            elif res.upper() == "Y":
                return True
        else:
            return validate()
    yes = True
    while yes:
        print("Yes, you gae")
        yes = validate()
except FileNotFoundError:
    print("Error: The file 'data.json' was not found")
except json.JSONDecodeError as e:
    print("Failed to deco/de JSON: {e}")