from __future__ import print_function
from domain import Student
from domain import Subject
import MySQLdb


class Repository:
    def __init__(self):
        self.studentList = []
        self.readFromDB()

    def readFromDB(self):
        # connect to the db ClassBook
        db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='ioana', db='ClassBook')
        # create a cursor
        cur = db.cursor()
        # select every last name from the db
        cur.execute('Select * from Students')
        database = cur.fetchall()
        # iterate through every data in database
        for value in database:
            student = Student()
            student.lastName = value[1]
            student.firstName = value[2]
            student.registrationNr = value[3]
            student.className = value[4]
            self.studentList.append(student)
        cur.close()

    def writeToDB(self, student):
        # connect to the db ClassBook
        db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='ioana', db='ClassBook')
        # create a cursor
        cur = db.cursor()
        # we have to write in the Students DB
        cur.execute(('Insert into Students values (NULL,%s,%s,%s,%s)'),
                    (student.lastName,student.firstName,student.registrationNr,student.grade))
        db.commit()

    def findInList(self, student):
        if len(self.studentList) == 0:
            return False
        for currentStudent in self.studentList:
            if student.lastName == currentStudent.lastName and student.firstName == currentStudent.firstName:
                return currentStudent
        return False

    def addToList(self, student):
        # we check if the student is already in the student list
        if self.findInList(student) is not False:
            return False
        else:
            self.studentList.append(student)
            self.writeToDB()
            return True

    def returnStudentList(self):
        # we sort by last name and first name
        self.studentList = sorted(self.studentList, key=lambda x: (x.lastName, x.firstName))
        return self.studentList

    # this is not that necessary as the registration nr is marked as unique in the DB
    def checkRegistrationNr(self, registrationNr):
        for student in self.studentList:
            if registrationNr == student.registrationNr:
                return False





