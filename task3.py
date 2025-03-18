class Educator:
    def __init__(self, name):
        self.name = name

    def prepareLesson(self):
        print(f"{self.name} is preparing a general educational lesson.")

class ITInstructor(Educator):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def prepareLesson(self):
        print(f"{self.name} is preparing a technical lesson on {self.subject}.")

    def teachCoding(self):
        print(f"{self.name} is teaching coding in {self.subject}.")


class DatabaseInstructor(ITInstructor):
    def __init__(self, name):
        super().__init__(name, "Python and SQL")

    def demonstrateMySQL(self):
        print(f"{self.name} is demonstrating MySQL database queries.")

    def teachCoding(self):
        print(f"{self.name} is teaching how to integrate SQL with Python.")

educator1 = Educator("Mr. udal")
educator1.prepareLesson()

it_instructor1 = ITInstructor("Mr.Rod", "Python")
it_instructor1.prepareLesson()
it_instructor1.teachCoding()

db_instructor1 = DatabaseInstructor("Mrs.noelen")
db_instructor1.prepareLesson()
db_instructor1.teachCoding()
db_instructor1.demonstrateMySQL()