from Patient import Patient
from CaseRecord import CaseRecord

history = []

input("Stroke Alert Simulator, Press enter to continue")

inGame = True
while inGame:

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

    current_patient = Patient()
    print(current_patient)
    is_candidate = current_patient.check_is_candidate()

    #Stroke alert should be called if the patient is within the window (4 hours) AND has at least one FAST symptom

    callAlert = input("Would you like to call a stroke alert? (y/n) ")
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
            callAlert = input("Would you like to call a stroke alert? (y/n) ")
            callAlert = callAlert.lower()
            continue

    if callAlert == "y":
        callAlertStr = "called a stroke alert"
    else:
        callAlertStr = "did not call a stroke alert"

    print(f"You {callAlertStr} for this patient:")
    print(current_patient)


    if is_candidate and callAlert == "y":
       print("CORRECT! The patient was a stroke candidate and you correctly called the stroke alert!")
    elif is_candidate and callAlert == "n":
        print("The patient WAS a stroke candidate and the alert was missed!")
    elif not is_candidate and callAlert == "y":
        print("The patient was not a stroke candidate and the alert was incorrectly called!")
    else:
        print("CORRECT! The patient was not a stoke candidate")

    current_patient.explain_candidate()

    record = CaseRecord(
        current_patient,
        callAlert == 'y',
        is_candidate
    )

    history.append(record)

    gameAgain = input("Would you like to play again? (y/n) ").strip().lower()

    if gameAgain != "y":
        print("Exiting the simulator!")
        break

