
planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).
planet(saturn, 6).
planet(uranus, 7).
planet(neptune, 8).

show_planet(Name) :-
    planet(Name, Position),
    write('Planet: '), write(Name),
    write(', Position: '), write(Position).
