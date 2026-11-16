% edge(From, To).   h(Node, HeuristicValue)
edge(s,a). edge(s,b).
edge(a,c). edge(a,d).
edge(b,e). edge(b,f).
edge(e,g). edge(f,g).

h(s,10). h(a,7). h(b,5). h(c,9).
h(d,6).  h(e,3). h(f,4). h(g,0).

best_first(Start, Goal, Path) :-
    h(Start, H),
    bfs([H-[Start]], Goal, RevPath),
    reverse(RevPath, Path).

bfs([_-[Goal|T]|_], Goal, [Goal|T]) :- !.
bfs([_-[N|T]|Rest], Goal, Path) :-
    findall(H-[M,N|T],
            (edge(N,M), \+ member(M,[N|T]), h(M,H)),
            Children),
    append(Children, Rest, Open),
    keysort(Open, Sorted),          % lowest heuristic first
    bfs(Sorted, Goal, Path).
