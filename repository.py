from __future__ import print_function
from domain import Student
from domain import Subject
import os
import re


class Repository:

    def __init__(self):
        self.studentList = []
        self.readFromFile()

    def findInList(self, student):
        if len(self.studentList) == 0:
            return False
        for currentStudent in self.studentList:
            if student.lastName == currentStudent.lastName and student.firstName == currentStudent.firstName:
                return currentStudent
        return False

    # the data for the student is sent from controller
    def addToList(self, student):
        # we check if the student is already in the student list
        if self.findInList(student) is not False:
            return False
        else:
            self.studentList.append(student)
            self.writeToFile()
            return True

    def writeToFile(self):
        classBook = open('classBook.txt', 'w')
        for student in self.studentList:
            classBook.write(student.firstName + ',' + student.lastName + ',' + str(student.registrationNr)
                            + ',' + str(student.grade)+' :')
            if student.getMarksForFileFormat() == '':
                classBook.write('\n')
            else:
                classBook.write(' ' + student.getMarksForFileFormat() + '\n')
        classBook.close()


    def readFromFile(self):
        classBook = open('classBook.txt')
        if os.path.getsize('classBook.txt') > 0:
            for line in classBook:
                # we separate the data by ':' , the first element will represent the student information
                # the rest is subjects and marks
                studentInfo = re.split(':', line)
                firsName, lastName, registrationNr, grade = studentInfo[0].split(',')
                registrationNr=int(registrationNr)
                grade = int(grade)
                student = Student(firsName, lastName, registrationNr, grade)
                if len(studentInfo) > 1:
                    for index in range(1, len(studentInfo) - 1):
                        subject, mark = studentInfo[index].split()
                        student.addGrade(subject, mark)
                self.studentList.append(student)

    def addMarkToList(self, student, subject, mark):
        # we check if the student is in the list
        student = self.findInList(student)
        if student is not False:
            student.addMark(subject, mark)
            self.writeToFile()
            return True
        else:
            return False

    def returnStudentList(self):
        # we sort by last name and first name
        self.studentList = sorted(self.studentList, key=lambda x: (x.lastName, x.firstName))
        return self.studentList

    # checks if the registration number coincides with the one of another student
    def checkRegistrationNr(self, registrationNr):
        for student in self.studentList:
            if registrationNr == student.registrationNr:
                return False
