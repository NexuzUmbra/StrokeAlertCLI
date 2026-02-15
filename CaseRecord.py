class CaseRecord:
    def __init__(self, patient, user_called, was_candidate):
        self.patient = patient
        self.user_called = user_called
        self.was_candidate = was_candidate

    def was_correct(self):
        return self.user_called == self.was_candidate

    def __str__(self):
        result = "CORRECT" if self.was_candidate else "INCORRECT"
        return(f'{self.patient}\n'
               f'User called alert: {self.user_called}\n'
               f'Result: {result}')
