from view import View
from domain import Student
from domain import Subject


class Controller:

    def __init__(self, repository):
        self.repository = repository

    # send a student object to the repository so it can be added to the database
    # the student information is received form view as a string that has to be splitted
    def createStudent(self, studentInfo):
        firstName, lastName, registrationNr, className = studentInfo.split(',')
        registrationNr = int(registrationNr)
        className = int(className)
        # create the object student
        student = Student(firstName, lastName, registrationNr, className)
        if self.repository.addToList(student) == 0:
            # if the student was already in the DB we return False
            return False

    # calls a function from the repository that adds a grade to a certain student
    def addGrade(self, firstName, lastName, subject, grade):
        student = Student(firstName, lastName)
        if self.repository.addGradeToList(student, subject, grade) is False:
            # if the student was not fond in the database we return false
            return False

    def returnStudent(self):
        return self.repository.returnStudentList()

    def closingDB(self):
        self.repository.closingDB()