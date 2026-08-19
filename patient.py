import random

class Patient:
    def __init__(self, age, sym_onset, face, arm, speech):
        self.age = age
        self.sym_onset = sym_onset
        self.face = face
        self.arm = arm
        self.speech = speech

    def random_case(self):
        return self(
            random.randint(45,100),
            random.randint(15,720),
            random.choice([True,False]),
            random.choice([True, False]),
            random.choice([True, False]),
        )

    def us_stroke_candidate(self):
        return(
            self.sym_onset <= 240 and (self.face or self.arm or self.speech)
        )

    def __str__(self):
        return(
            f"Information: \n"
            f"Age: {self.age}\n"
            f"Last Known Well: {self.sym_onset} minutes\n"
            f"Facial Droop: {'Yes' if self.face else 'No'}\n"
            f"Arm Drift: {'Yes' if self.arm else 'No'}\n"
            f"Speech Difficulty: {'Yes' if self.speech else 'No'}\n"
        )