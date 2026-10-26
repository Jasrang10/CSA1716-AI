% Facts
bird(parrot).
bird(pigeon).
bird(ostrich).
bird(penguin).

% Rules
can_fly(X) :-
    bird(X),
    X \= ostrich,
    X \= penguin.

cannot_fly(X) :-
    bird(X),
    (X = ostrich ; X = penguin).
