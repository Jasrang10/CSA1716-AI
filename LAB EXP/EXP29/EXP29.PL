:- dynamic known/1.

% rule(Conditions, Conclusion)
rule([has_fever, has_cough], flu).
rule([flu, has_body_ache], needs_rest).
rule([needs_rest], take_medicine).

forward :-
    rule(Conds, Concl),
    \+ known(Concl),
    all_known(Conds),
    assert(known(Concl)),
    format('Derived: ~w~n', [Concl]),
    forward.
forward.

all_known([]).
all_known([H|T]) :- known(H), all_known(T).
