use ClassBook;
/*create table Students (id int not null auto_increment primary key unique,
						lastName varchar(30),
                        firstName varchar(30),
                        registrationNr int unique,
                        class tinyint);*/


#insert into Students values (Null, 'Doe','John','14985',10);

/*create table Subjects (id int auto_increment primary key unique,
						subject_name varchar(30) unique);
                        
create table Grades (student_id int,
					foreign key (student_id) references Students(id),
                    subject_id int,
                    foreign key (subject_id) references Subjects(id),
					grade_date date,
                    primary key( student_id, subject_id, grade_date),
                    grade_type enum('test','project'))*/
/*create table Grades (id int auto_increment primary key unique,
					student_id int,
					foreign key (student_id) references Students(id),
                    subject_id int,
                    foreign key (subject_id) references Subjects(id),
					grade int );*/

/*insert into subjects values( Null, 'Mathematics');
insert into subjects values( Null, 'English');
insert into subjects values( Null, 'Informatics');
insert into subjects values( Null, 'Chemistry');*/


