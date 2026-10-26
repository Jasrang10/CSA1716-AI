% Facts
male(john).
male(paul).
male(tom).
female(mary).
female(lisa).

parent(john, paul).
parent(mary, paul).
parent(paul, tom).
parent(lisa, tom).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
