class EsportsEvent:
    def __init__(self, event_name, event_date):
        self.event_name = event_name
        self.event_date = event_date

    def scheduleMatch(self):
        print(f"{self.event_name} match is scheduled on {self.event_date}.")
class StudentDivision(EsportsEvent):
    def __init__(self, event_name, event_date):
        super().__init__(event_name, event_date)

    def registerTeam(self, team_name):
        print(f"Team '{team_name}' has been registered for the {self.event_name} in the Student Division.")

class FacultyDivision(EsportsEvent):
    def __init__(self, event_name, event_date):
        super().__init__(event_name, event_date)

    def assignReferee(self, referee_name):
        print(f"Referee {referee_name} has been assigned for the {self.event_name} in the Faculty Division.")

event = EsportsEvent("University Esports Championship", "April 20, 2025")
event.scheduleMatch()

student_event = StudentDivision("University Esports Championship", "April 20, 2025")
student_event.scheduleMatch()
student_event.registerTeam("Cyber Warriors")

faculty_event = FacultyDivision("University Esports Championship", "April 20, 2025")
faculty_event.scheduleMatch()
faculty_event.assignReferee("Mr. jeff")