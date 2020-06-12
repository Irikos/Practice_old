%logica trebuie sa fie invers: concatenezi doar cele care sunt diferite
%4  Eliminate an element from a list (one/all the occurrencesof that element).
eliminate([], X, L) :-
	write(L).

eliminate([X|T], X, L) :-
	eliminate(T, X, [X|L]).
	
eliminate([H|T], X, L) :-
	eliminate(T, X, L).




write_list([]).
write_list([Head|Tail]) :-
	write(Head), nl,
	write_list(Tail).

%end of 4



%3 Calculate the alternate sum of the elements of a list.

alternate([], ST, S) :-
	S is ST.

alternate([X], ST, S) :-
	ST1 is ST + X,
	alternate([], ST1, S).

alternate([H1, H2|T], ST, S) :-
	ST1 is H1 + ST,
	ST2 is ST1 - H2,
	alternate(T, ST2, S).

%end of 3

%2 member and concat
concat([], L, L).

concat([H|T], L2, [H|L3]) :-
	concat(T, L2, L3).
	
concat2([],L,L).

concat2([H|T],L2,[H|L3])  :-  
	concat2(T,L2,L3). 

member2(X, [X|T]) :- !.
	
member2(X, [H|T]) :-
	member2(X, T).
%end of 2

%1 Write the max predicate that calculates the maximum between 2 values.
max(X, Y) :-
	X < Y,
	write(Y).

max(X, Y) :-
	X > Y,
	write(X).
	
max(X, Y) :-
	X =:= Y,
	write('equals').

%end of 1

f(X,0) :-
	X =< 3,
	!.
f(X,2) :-
	3 < X, 
	X =< 6,
	!.
f(X,4) :-
	6 < X,
	!.



parent(ion,maria).
parent(ana,maria).
parent(ana,dan).
parent(maria,madalina).
parent(maria,radu).
parent(maria,elena).
parent(elena,nicu).
parent(radu,george).
parent(radu,dragos).



brothers(X, Y) :-
	parent(Z, X),
	parent(Z, Y),
	X \== Y.
	
	

grandparent(X, Y) :-
	parent(Z, Y),
	parent(X, Z).
	

pred(X, Y) :- 
	parent(X, Y).
pred(X, Z) :- 
	parent(X, Y), 
	pred(Y, Z).

pred2(X, Y) :- 
	parent(X, Y).
	
pred2(X, Z) :-
	parent(Y, Z),
	pred2(X, Y).