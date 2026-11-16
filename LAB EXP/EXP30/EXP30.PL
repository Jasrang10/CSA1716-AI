% facts
fact(has_fever).
fact(has_cough).
fact(has_body_ache).

% rule(Goal, Subgoals)
rule(flu,           [has_fever, has_cough]).
rule(needs_rest,    [flu, has_body_ache]).
rule(take_medicine, [needs_rest]).

prove(G) :- fact(G).
prove(G) :- rule(G, Subgoals), prove_all(Subgoals).

prove_all([]).
prove_all([H|T]) :- prove(H), prove_all(T).
