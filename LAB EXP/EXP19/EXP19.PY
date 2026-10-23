
student(101, 'Arun').
student(102, 'Priya').
student(103, 'Rahul').

teacher('Ravi', 'Python').
teacher('Meena', 'AI').
teacher('Kumar', 'Prolog').

subject(101, 'Python').
subject(102, 'AI').
subject(103, 'Prolog').

student_teacher(Name, Teacher, Subject) :-
    student(ID, Name),
    subject(ID, Subject),
    teacher(Teacher, Subject).
