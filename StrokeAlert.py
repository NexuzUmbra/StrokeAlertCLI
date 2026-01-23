import sys
import random

age = random.randint(45, 100)
ageStr = (f"Age: {age}")

symOnsetMinutes = random.randint(15, 720)
symOnsetMinutesStr = (f"Last known well: {symOnsetMinutes} minutes")

faceDroop = random.choice([True, False])
if faceDroop == True:
    faceDroopStr = "Facial Droop: Yes"
else:
    faceDroopStr = "Facial Droop: No"

armDrift = random.choice([True, False])
if armDrift == True:
    armDriftStr = "Arm Drift: Yes"
else:
    armDriftStr = "Arm Drift: No"

speechDiff = random.choice([True, False])
if speechDiff == True:
    speechDiffStr = "Speech Dif: Yes"
else:
    speechDiffStr = "Speech Dif: No"

case = f"Information:\n {ageStr}\n {symOnsetMinutesStr}\n {faceDroopStr}\n {armDriftStr}\n {speechDiffStr}"

input("Stroke Alert Simulator, Press enter to continue")

start = input("Input 1 to start or 2 to quit: ")
i = True

while i:
    if start.isdigit():
        start_int = int(start)
        if start_int == 1:
            print("Using the provided information, decide to call a stroke alert or not")
            i = False
            break
        elif start_int == 2:
            sys.exit("Quitting")
            i = False
            break
        else:
            print("Invalid input")
            start = input("Input 1 to start or 2 to quit: ")
            continue
print(case)