from __future__ import print_function
from domain import Student
import MySQLdb
from MySQL import DB


class Repository:
    def __init__(self, db):
        self.studentList = []
        self.db = db
        self.loadAllStudents()

    # is the first thing that happens when the programme opens
    def loadAllStudents(self):
        try:
            cursor = self.db.query('Select * from Students')
            table = cursor.fetchall()
            # iterate through every data in the table students
            for row in table:
                student = Student()
                student.lastName = row[1]
                student.firstName = row[2]
                student.registrationNr = row[3]
                student.className = row[4]
                self.studentList.append(student)
            # we also have to add the grades in the list
            cursor=self.db.query('select students.registrationNr, subjects.subjectName, grades.grade '
                                   'from grades '
                                   'join students on grades.student_id = students.id '
                                   'join subjects on grades.subject_id= subjects.id;')

            table=cursor.fetchall()
            for row in table:
                # value[0]= registration nr, value[1]= subject name , value[2]=grade
                for student in self.studentList:
                    # if we find a student that has the registration nr to that student we add the grade
                    if row[0] == student.registrationNr:
                        student.addGrades(row[1], row[2])
            # we close the environment
            cursor.close()
            # we close the bd
        except MySQLdb.Error as err:
            print ('Something went wrong:{}'.format(err))

    # adds student info to the DB
    def addInfoToDB(self, student):
        try:
            sql = 'Insert into Students values(NULL,%s,%s,%s,%s);',(student.lastName,student.firstName,student.registrationNr,student.className)
            self.db.query(sql)
            self.db.commit()
            return True
        except MySQLdb.IntegrityError as err:
            print("Error: {}".format(err))
            return False

    # adds the grades to the DB
    def addGradeToDB(self, student, subject, grade):
        # we have to see what is the subjest id and the student id and after add it to the list
        # find the student id
        cursor=self.db.query('Select id from Students where lastName= %s and firstName= %s',
                    (student.lastName, student.firstName))
        studentId = cursor.fetchone()
        # find the subject id
        cursor=self.db.query('Select id from Subjects where subjectName= %s', (subject,))
        subjectId = cursor.fetchone()
        self.db.query('Insert into Grades values (NULL,%s,%s,%s)',
                    (studentId[0], subjectId[0], grade))
        self.db.commit()

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
            self.addInfoToDB(student)
            return True

    def returnStudentList(self):
        # we sort by last name and first name
        self.studentList=[]
        self.loadAllStudents()
        self.studentList = sorted(self.studentList, key=lambda x: (x.lastName, x.firstName))
        return self.studentList

    # this is not that necessary as the registration nr is marked as unique in the DB
    def checkRegistrationNr(self, registrationNr):
        for student in self.studentList:
            if registrationNr == student.registrationNr:
                return False

    def addGradeToList(self, student, subject, grade):
        student = self.findInList(student)
        if student is not False:
            student.addGrades(subject, grade)
            # add to the db as well
            self.addGradeToDB(student, subject, grade)
            return True
        else:
            return False

    def closingDB(self):
        self.db.close()



