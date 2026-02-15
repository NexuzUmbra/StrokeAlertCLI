import random

class Patient:

    def __init__(self):
        self.age = random.randint(22, 110)
        self.sym_onset_minutes = random.randint(15, 360)
        self.face_droop = random.choice([True, False])
        self.arm_drift = random.choice([True, False])
        self.speech_diff = random.choice([True, False])

    def check_is_candidate(self):

        if self.sym_onset_minutes <=240 and (self.face_droop or self.arm_drift or self.speech_diff):
            return True
        else:
            return False

    def __str__(self):

        age_str = f'Age: {self.age}'
        onset_minutes_str = f'Last Known Well: {self.sym_onset_minutes} minutes'

        if self.face_droop:
            face_droop_str = "Facial Droop: Yes"
        else:
            face_droop_str = "Facial Droop: No"

        if self.arm_drift:
            arm_drift_str = "Arm Drift: Yes"
        else:
            arm_drift_str = "Arm Drift: No"

        if self.speech_diff:
            speech_diff_str = "Speech Dif: Yes"
        else:
            speech_diff_str = "Speech Dif: No"

        return f'{age_str}\n{onset_minutes_str}\n{face_droop_str}\n{arm_drift_str}\n{speech_diff_str}'

    def explain_candidate(self):

        if self.check_is_candidate():
            print("The patient was in the window with at least one FAST symptom")
        elif self.sym_onset_minutes <= 240:
            print("The patient was in the window but did not have any FAST symptoms")
        else:
            print("The patient was not in the window")