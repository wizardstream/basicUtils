#!/usr/bin/env python3
import time
import sys
from datetime import datetime
import secrets
from colorama import Fore, Back, Style

now = datetime.now()

def wait(timeInSeconds):
    time.sleep(timeInSeconds)

def greet():
    print("Hello, world!")

def help():
    print(Fore.GREEN + """
    -calc     -c          basicUtils -calc [add|sub|mul|div] num1 num2
    -maths
    
    -dateTime -dt         Prints time
    
    -echo     -e          echos

    -greet    -g          Greets the user
    
    --help    --h         Shows this help screen

    -random   -rand       basicUtils -rand _num_   Generates random Hex number _num_ bytes big      
    """)
    print(Fore.WHITE + "")
def calc():
    if len(sys.argv) < 4:
        print("Missing arguments, try --help for help.")
        return

    op = sys.argv[2]
    try:
        a = float(sys.argv[3])
        b = float(sys.argv[4])
    except ValueError:
        print(Fore.RED + "Error:"+ Fore.WHITE +  " operands must be numbers.")

    if op == "add":
        print (a+b)
    if op == "sub":
        print(a-b)
    if op == "mul":
        print(a*b)
    if op == "div":
        if b == 0:
            print(Fore.RED + "Error: " + Fore.WHITE  + "division by zero")
        else:
            print(a/b)

def getTime():
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def HexRandom():
    if len(sys.argv) < 3:
        print("Missing arguments, try --gelp for help.")
        return
    print(secrets.token_hex(int(sys.argv[2])))

def echo():
    if len(sys.argv) < 3:
        print("")
        return None
    print(sys.argv[3])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing arguments, try --help for help.")
        sys.exit(1)

    command = sys.argv[1]

    if command == "-greet" or command == "-g":
        greet()
    elif command == "--help" or command == "--h":
        help()
    elif command == "-calc" or command == "-c" or command == "-maths":
        calc()
    elif command == "-dt" or command == "-dateTime":
        getTime()
    elif command == "-random" or command == "-rand":
        HexRandom()
    elif command == "-echo" or command == "-e":
        echo()
    else:
        print(f"Unknown command: {command}\nTry --help")
