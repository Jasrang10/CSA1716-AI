
person('Rahul', '2002-05-10').
person('Arun', '2001-08-15').
person('Priya', '2003-12-20').

show_dob(Name, DOB) :-
    person(Name, DOB).
