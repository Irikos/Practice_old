%Definit ̧i un predicat distance/3 pentru a calcula distant ̧a dintre doua
%puncte ıntr-un plan 2-dimensional. Punctele sunt date ca perechi de
%coordonate.

distance((X1, Y1), (X2, Y2), Z) :-
	Z is sqrt((X2 - X1)**2 + (Y2 - Y1)**2).

square(0, Y) :-
	write(Y).

square(X, Y) :- 
	write_line(X, Y, X, X).
	
write_line(0, Y, 1, O) :-
	nl.
	
write_line(0, Y, Z, O) :-
	T is Z - 1,
	nl,
	write_line(O, Y, T, O).

write_line(X, Y, Z, O) :-
	write(Y),
	T is X - 1,
	write_line(T, Y, Z, O).
