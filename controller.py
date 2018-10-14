from view import View
from domain import Student
from domain import Subject


class Controller:

    def __init__(self, repository):
        self.repository = repository

    def createStudent(self, studentInfo):
        firstName, lastName, registrationNr, grade = studentInfo.split(',')
        registrationNr = int(registrationNr)
        grade = int(grade)
        student = Student(firstName, lastName, registrationNr, grade)
        if self.repository.addToList(student) == 0:
            return False
        else:
            # we add the student to the student list
            return True

    def addMark(self, firstName, lastName, subject, mark):
        student = Student(firstName, lastName)
        if self.repository.addMarkToList(student, subject, mark) is False:
            return False

    def returnStudent(self):
        return self.repository.returnStudentList()


    def checkRegistrationNr(self, registrationNr):
        return self.repository.checkRegistrationNr(registrationNr)

    def closingDB(self):
        self.repository.closingDB()