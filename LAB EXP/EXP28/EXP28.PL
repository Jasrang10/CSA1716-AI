:- dynamic yes/1, no/1.

diagnose :- hypothesis(D), !,
    write('Diagnosis: '), write(D), nl, undo.
diagnose :- write('Cannot diagnose the disease.'), nl, undo.

hypothesis(flu)      :- verify(fever), verify(cough), verify(body_ache).
hypothesis(cold)     :- verify(sneezing), verify(runny_nose), verify(sore_throat).
hypothesis(malaria)  :- verify(fever), verify(chills), verify(sweating).
hypothesis(typhoid)  :- verify(fever), verify(headache), verify(stomach_pain).
hypothesis(migraine) :- verify(headache), verify(nausea), verify(light_sensitivity).

verify(S) :- ( yes(S) -> true ; no(S) -> fail ; ask(S) ).

ask(S) :-
    write('Does the patient have '), write(S), write('? (y/n): '),
    read(R),
    (   (R == y ; R == yes) -> assert(yes(S))
    ;   assert(no(S)), fail ).

undo :- retractall(yes(_)), retractall(no(_)).
