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

            # add exception handling in case the user doesn't comply
            while True:
                try:
                    option = int(raw_input('Enter option: '))
                    if (option >= 0) and (option <= 4):
                        break
                    else:
                        print("The option you chose is not valid")
                except ValueError:
                    print("The option you chose is not valid")
            if option == 0:
                self.controller.closingDB()
                break
            if option == 1:
                # we call a function to ask for data about the student and is has to be called only once
                studentInfo = self.studentInfo()
                if studentInfo is not False and self.controller.createStudent(studentInfo) is False:
                    print('The student is already in the database')

            if option == 2:
                # we call functions in order to add the mark for a subject to a specific student
                # the results will then be send to controller and after to repository
                lastName = self.addString('last name')
                firstName = self.addString('first name')
                subject = self.addSubject()
                mark = self.addMark()
                if self.controller.addGrade(lastName, firstName, subject, mark) == False:
                    print ('The student has not yet been added to the database')
            if option == 3:
                listaElevi = self.controller.returnStudent()
                for elev in listaElevi:
                    print(elev.getStudent())
            if option == 4 :
                listaElevi = self.controller.returnStudent()
                for elev in listaElevi:
                    print(elev)
    def studentInfo(self):
        lastName = self.addString('last name').title()
        firstName = self.addString('first name').title()
        registrationNr = self.addRegitrationNr()
        # when we add the registration number we fave to make sure that there is no other student with that number
        # we could just as well generate a random registration number
        # but we still have to check if there are duplicates
        if self.controller.checkRegistrationNr(registrationNr) is False :
            print ('There is another student in the database with the same registration number')
            # we end the adding to the list now
            return False
        else:
            grade = self.addGrade()
            return '{},{},{},{}'.format(lastName,firstName, registrationNr, grade)

    def addString(self, string):
        while True:
            person = raw_input('Add {}: '.format(string))
            if all(char.isalpha() or char == ' ' for char in person):
                break
            else:
                print("{} can contain only letters.".format(string))
        return person

    def addRegitrationNr(self):
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

    def addGrade(self):
        while True:
            try:
                grade = int(raw_input("Add grade: "))
                if grade in range(0, 13):
                    break
                else:
                    print ("The grade can be between 1 and 12.")
            except ValueError:
                print ("The grade can be between 1 and 12.")
        return grade

    def addSubject(self):
        while True:
            curriculum = ('mathematics', 'chemistry', 'physics','informatics','english')
            subject = raw_input('Add subject: ')
            #transforms the string in lowercase and removes the spaces
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

    def addMark(self):
        while True:
            mark = int (raw_input('Add mark: '))
            if mark in range(1,11):
                break
            else:
                print('The mark should be in the interval 1 - 10.')
        return mark


