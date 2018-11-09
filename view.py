from __future__ import print_function


class View:

    def __init__(self, controller):
        self.controller = controller

    def mainMenu(self):
        while True:
            print ("0.To exit press 0")
            print ("1.To add a new student press 1")
            print ("2.To add a grade to a student press 2")
            print ("3.To show the students press 3")
            print ("4.To show the grades press 4")

            # add exception handling in case the user or the programmer doesn't comply
            while True:
                try:
                    option = int(raw_input('Enter option: '))
                    if (option >= 0) and (option <= 4):
                        break
                    else:
                        print("The option you chose is not valid")
                except ValueError:
                    print("The option you chose is not valid")

            # add the if statemens
            if option == 0:
                self.controller.closingDB()
                break

            if option == 1:
                # we call a function to ask for data about the student and is has to be called only once
                student = self.studentInfo()
                if self.controller.createStudent(student) is False:
                    print('The student is already in the database or the registration number already exists.')

            if option == 2:
                # we call functions in order to add the grade for a subject to a specific student
                # the results will then be send to controller and after to repository
                lastName = self.createString('last name')
                firstName = self.createString('first name')
                subject = self.createSubject()
                grade = self.createGrade()
                # we have to add grades to the students that are already in the database
                if self.controller.addGrade(lastName, firstName, subject, grade) == False:
                    print ('The student has not yet been added to the database.')

            if option == 3:
                listaElevi = self.controller.returnStudent()
                for elev in listaElevi:
                    print(elev.getStudent())

            if option == 4 :
                listaElevi = self.controller.returnStudent()
                for elev in listaElevi:
                    print(elev.getSudentGrades())

    def studentInfo(self):
        lastName = self.createString('last name').title()
        firstName = self.createString('first name').title()
        registrationNr = self.createRegistrationNr()
        className = self.createClassName()
        return '{},{},{},{}'.format(lastName,firstName, registrationNr, className)

    def createString(self, string):
        while True:
            person = raw_input('Add {}: '.format(string))
            if all(char.isalpha() or char == ' ' for char in person):
                break
            else:
                print("{} can contain only letters.".format(string))
        return person

    def createRegistrationNr(self):
        while True:
            try:
                registrationNr = raw_input("Add registration number: ")
                if len(registrationNr) == 5:
                    break
                else:
                    print ("The registration number has only 5 numbers.")
            except ValueError:
                print("The registration number has only 5 numbers.")
        return int(registrationNr)

    def createClassName(self):
        while True:
            try:
                className = int(raw_input("Add class: "))
                if className in range(0, 13):
                    break
                else:
                    print ("The class can be between 1 and 12.")
            except ValueError:
                print ("The class can be between 1 and 12.")
        return className

    def createSubject(self):
        while True:
            curriculum = ('mathematics', 'chemistry', 'physics','informatics','english')
            subject = raw_input('Add subject: ')
            # transforms the string in lowercase and removes the spaces
            subject = subject.lower().strip()
            found = False
            for s in curriculum:
                if subject == s:
                    found = True
            if found is True:
                break
            else:
                print('The subject is not found in the curriculum')
        return subject

    def createGrade(self):
        while True:
            grade = int (raw_input('Add grade: '))
            if grade in range(1,11):
                break
            else:
                print('The grade should be in the interval 1 - 10.')
        return grade


