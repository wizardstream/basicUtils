#!/usr/bin/env python3
import time
import sys
from datetime import datetime
import secrets
from colorama import Fore, Back, Style
import requests
import os

now = datetime.now()

def wait(timeInSeconds):
    time.sleep(timeInSeconds)

def greet():
    print("Hello, world!")


def getWeather(city):
    # Retrieve the API key from the environment
    api_key = "cf1bb667de5d850e3eddee8ed46e897c"
    if not api_key:
        print("[ERROR] API key not found. Please set the OPENWEATHER_API_KEY environment variable.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"[ERROR] City not found or invalid key: {data.get('message', 'Unknown error')}")
            return

        name = data['name'] + ", " + data['sys']['country'] + ", " + str(data['coord']['lat']) + "N/S, " + str(data['coord']['lon']) + "E/W"
        temp = data['main']['temp']
        feels = data['main']['feels_like']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f"📍 Weather in {name}")
        print(f"🌡️ Temperature: {temp}°C (feels like {feels}°C)")
        print(f"🌥️ Condition: {weather.capitalize()}")
        print(f"💧 Humidity: {humidity}%")

    except Exception as e:
        print("[ERROR] Failed to fetch weather:", str(e))

def help():
    print(Fore.GREEN + """
    -calc     -c          basicUtils -calc [add|sub|mul|div] num1 num2
    -maths
    
    -dateTime -dt         Prints time
    
    -echo     -e          echos

    -greet    -g          Greets the user
    
    --help    --h         Shows this help screen

    -random   -rand       basicUtils -rand _num_   Generates random Hex number _num_ bytes big
    
    -weather              Shows the weather of the city listed after the tag (-weather)
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
    message = ""
    a = 0
    if len(sys.argv) < 3:
        print("")
        return None
    for i in sys.argv:
        a += 1
        if a < 3:
            continue
        message = message + " " + i 
    print(message)
    message = ""
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing arguments, try --help for help.")
        sys.exit(1)

    command = sys.argv[1]

    if command == "-greet" or command == "-g":
        greet()
    elif command == "-weather":
        getWeather(sys.argv[2])
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
