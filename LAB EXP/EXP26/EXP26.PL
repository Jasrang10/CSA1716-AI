% ---------- Facts: fruit(Name, Color) ----------
fruit(apple,      red).
fruit(apple,      green).
fruit(banana,     yellow).
fruit(grapes,     green).
fruit(grapes,     purple).
fruit(orange,     orange).
fruit(strawberry, red).
fruit(mango,      yellow).
fruit(cherry,     red).
fruit(blueberry,  blue).

% ---------- Rules ----------

% 1. Find all colors of a given fruit (backtracking over colors)
colors_of(Fruit, Color) :-
    fruit(Fruit, Color).

% 2. Find all fruits of a given color (backtracking over fruits)
fruits_of(Color, Fruit) :-
    fruit(Fruit, Color).

% 3. Print every fruit with its color using forced backtracking
show_all :-
    fruit(F, C),
    write(F), write(' is '), write(C), nl,
    fail.            % force backtracking to the next fact
show_all.            % succeed at the end

% 4. Print all fruits of a given color
show_color(Color) :-
    fruit(F, Color),
    write(F), nl,
    fail.
show_color(_).
