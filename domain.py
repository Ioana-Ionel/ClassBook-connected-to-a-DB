class Student:

    def __init__(self,  lastName="", firstName="", registrationNr = 0, className=0):
        self.lastName = lastName
        self.firstName = firstName
        self.registrationNr = registrationNr
        self.className = className
        self.subjects = []

    def __repr__(self):
        return "{},{},{},{}".format(self.lastName, self.firstName, self.registrationNr, self.className)

    def __str__(self):
        strSubjects = " "
        #we want to show the result as a string
        for s in self.subjects:
            strSubjects += str(s) + " "
        return "{} {} with the registration number {} is in class {} and has the grades: {}".format(self.lastName, self.firstName, self.registrationNr, self.className, strSubjects)

    def getStudent(self):
        return "{} {} with the registration number {} is in class {}".format(self.lastName, self.firstName, self.registrationNr, self.className)

    def getSudentGrades(self):
        strSubjects = " "
        # we want to show the result as a string
        for s in self.subjects:
            strSubjects += str(s) + " "
        return "{} {} has the following grades: {}".format(self.lastName, self.firstName, strSubjects)

    # this function adds a grade to the subject list
    def addGrades(self, subjectName, grade):
        for s in self.subjects:
            # for the existing subjects we will add grades in their own lists
            if s.getSubjectName() == subjectName:
                s.addGrade(grade)
                # it will return the result and not go further
                return
        # in case we don't find the subject we create a new one
        # if we don't have any subject in the list we create a new one
        subject = Subject(subjectName)
        subject.addGrade(grade)
        self.subjects.append(subject)


class Subject:

    def __init__(self, subject="", grades=None):
        self.subject = subject
        if grades is None:
            self.grades = []
        else:
            self.grades = grades

    def __str__(self):
        strGrades=""
        for grade in self.grades:
            strGrades += " " + str(grade)
        return self.subject + strGrades

    def addGrade(self, grade):
        self.grades.append(grade)

    def getSubjectName(self):
        return self.subject

    def getGrades(self):
        strGrades = ''
        for grade in self.grades:
            strGrades = strGrades + self.subject + ' ' + str(grade) + ' : '
        return strGrades

