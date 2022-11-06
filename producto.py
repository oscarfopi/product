import os
import time
def print_optioins():
    print("menu products")
    print("*" * 30)
    print("select option:")
    print("[C]reate product")
    print("[L]ist products")
    print("[M]odify product")
    print("[R]emove product")
    print("[S]earch product")
    print("[E]xit")

def run():
    print_options()

    command = input()
    command = command.upper()

    if comman == "C":
        pass
    elif command == "L":
        pass
    elif command == "M":
        pass
    elif command == "R":
        pass
    elif command == "S":
        pass
    elif command == "E":
        os._exit(1)
    else:
        print("Invalid Command")
        time.sleep(1)
        run()

    if _name_ == "_main_":
        run()
