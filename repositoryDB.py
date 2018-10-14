from __future__ import print_function
from domain import Student
from domain import Subject
import MySQLdb
from MySQL import DB


class Repository:
    def __init__(self, db):
        self.studentList = []
<<<<<<< HEAD
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
=======
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
>>>>>>> parent of 428ee2e... Second commit before class DB

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


    def closingDB(self):
        self.db.close()



