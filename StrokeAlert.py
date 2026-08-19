import random

from patient import Patient

input("Stroke Alert Simulator, Press enter to continue")

inGame = True
while inGame:

    age = random.randint(22, 110)
    ageStr = (f"Age: {age}")

    symOnsetMinutes = random.randint(15, 360)
    symOnsetMinutesStr = (f"Last known well: {symOnsetMinutes} minutes")

    faceDroop = random.choice([True, False])
    if faceDroop:
        faceDroopStr = "Facial Droop: Yes"
    else:
        faceDroopStr = "Facial Droop: No"

    armDrift = random.choice([True, False])
    if armDrift:
        armDriftStr = "Arm Drift: Yes"
    else:
        armDriftStr = "Arm Drift: No"

    speechDiff = random.choice([True, False])
    if speechDiff:
        speechDiffStr = "Speech Dif: Yes"
    else:
        speechDiffStr = "Speech Dif: No"

    case = f"Information:\n {ageStr}\n {symOnsetMinutesStr}\n {faceDroopStr}\n {armDriftStr}\n {speechDiffStr}"
    caseParams = f"\n {ageStr}\n {symOnsetMinutesStr}\n {faceDroopStr}\n {armDriftStr}\n {speechDiffStr}"

    while True:
        start = input("Input 1 to start or 2 to quit: ")

        if start == "1":
            print("Using the provided information, decide to call a stroke alert or not")
            break
        elif start == "2":
            print("Quitting simulator")
            inGame = False
            break
        else:
            print("Invalid input")
    if not inGame:
        break
    print(case)

    isStrokeCandidate = (symOnsetMinutes <= 240 and (faceDroop or armDrift or speechDiff)  )

    #Stroke alert should be called if the patient is within the window (4 hours) AND has at least one FAST symptom

    callAlert = input("Would you like to call a stroke alert? (y/n)")
    callAlert = callAlert.lower()

    while True:
        if callAlert == "y":
            print("Stroke alert called!")
            break
        elif callAlert == "n":
            print("No alert called")
            break
        else:
            print("Invalid input")
            callAlert = input("Would you like to call a stroke alert? (y/n)")
            callAlert = callAlert.lower()
            continue

    if callAlert == "y":
        callAlertStr = "called a stroke alert"
    else:
        callAlertStr = "did not call a stroke alert"

    print(f"You {callAlertStr} for this patient {caseParams}")

    if isStrokeCandidate and callAlert == "y":
        print("CORRECT! The patient was a stroke candidate and you correctly called the stroke alert!")
    elif isStrokeCandidate and callAlert == "n":
        print("The patient WAS a stroke candidate and the alert was missed!")
    elif not isStrokeCandidate and callAlert == "y":
        print("The patient was not a stroke candidate and the alert was incorrectly called!")
    else:
        print("CORRECT! The patient was not a stoke candidate")

    if symOnsetMinutes <= 240 and (faceDroop or armDrift or speechDiff):
        print("The patient was in the window with at least one FAST symptom")
    elif symOnsetMinutes <= 240:
        print("The patient was in the window but did not have any FAST symptoms")
    else:
        print("The patient was not in the window")

    gameAgain = input("Would you like to play again? (y/n)").strip().lower()

    if gameAgain != "y":
        print("Exiting the simulator!")
        break

