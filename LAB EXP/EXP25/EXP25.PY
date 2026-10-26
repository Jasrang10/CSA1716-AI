% Initial state
% state(MonkeyPosition, BoxPosition, MonkeyStatus, HasBanana)

move(state(middle, middle, onbox, no),
     grasp,
     state(middle, middle, onbox, yes)).

move(state(P, P, onfloor, no),
     climb,
     state(P, P, onbox, no)).

move(state(P1, B, onfloor, no),
     walk(P1, P2),
     state(P2, B, onfloor, no)) :-
    P1 \= P2.

move(state(P1, B1, onfloor, no),
     push(B1, B2),
     state(B2, B2, onfloor, no)) :-
    P1 = B1,
    B1 \= B2.

% Goal state
goal(state(_, _, _, yes)).

% Solve the problem
solve(State, []) :-
    goal(State).

solve(State, [Action|Rest]) :-
    move(State, Action, NextState),
    solve(NextState, Rest).
