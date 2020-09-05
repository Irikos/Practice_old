join_string(Str1, Str2, Str3) :-
	name(Str1, StrList1),
	name(Str2, StrList2),
	append(StrList1, StrList2, StrList3),
	name(Str3, StrList3).






write_list([]).
write_list([Head|Tail]) :-
	write(Head), nl,
	write_list(Tail).





:- dynamic(father/2).
:- dynamic(likes/2).
:- dynamic(friend/2).
:- dynamic(stabs/3).

father(lord_montague, romeo).
father(lord_capulet, juliet).

likes(mercutio, dancing).
likes(benvolio, dancing).
likes(romeo, dancing).
likes(romeo, juliet).
likes(juliet, romeo).
likes(juliet, dancing).

friend(romeo, mercutio).
friend(romeo, benvolio).

stabs(tybalt, mercutio, sword).
stabs(romeo, tybalt, sword).









guess_number :- loop(0).

loop(15) :- write('You guessed it!').

loop(X) :- 
	X \= 15,
	write(X),
	write(' is not the number'), nl,
	write('Guess Number'),
	read(Guess),
	loop(Guess).








count_to_10(10) :- write(10), nl, !.
count_to_10(X) :-
	write(X), nl,
	Y is X + 1,
	count_to_10(Y).


count_down(Low, High) :-
	between(Low, High, Y),
	Z is High - Y,
	write(Z), nl.

count_up(Low, High) :-
	between(Low, High, Y),
	Z is Y + Low,
	write(Z), nl.


write_to_file(File, Text) :- 
	open(File, write, Stream),
	write(Stream, Text), nl,
	close(Stream).

read_file(File) :-
	open(File, read, Stream),
	get_char(Stream, Char1),
	process_stream(Char1, Stream),
	close(Stream).
	
	
process_stream(end_of_file, _) :- !.

process_stream(Char, Stream) :-
	write(Char),
	get_char(Stream, Char2),
	process_stream(Char2, Stream).



fav_char :-
	write('what is your favourite character?'),
	get(X),
	format('ascii value: ~w', [X]),
	put(X), nl.


say_hi :-
	write('what is your name?'),
	read(X),
	write('Hi '),
	write(X).


double_digit(X) :-
	Y is X * 2,
	write(Y).


is_even(X) :-
	Y is X // 2,
	X =:= 2 * Y.









warm_blooded(penguin).
warm_blooded(human).

produce_milk(penguin).
produce_milk(human).

have_feather(penguin).
have_hair(human).

mammal(X) :-
	warm_blooded(X),
	produce_milk(X),
	have_hair(X).



customer(tom, smith, 20.55).
customer(sally, smith, 120.55).

get_customer_balance(FName, LName) :-
	customer(FName, LName, Bal),
	write(FName), tab(1),
	format('~w owes us $~2f ~n', [LName, Bal]).

vertical(line(point(X,Y), point(X, Y2))).

horizontal(line(point(X,Y), point(X2, Y))).


owns(albert, pet(cat, olive)).






male(albert).
male(bob).
male(bill).
male(carl).
male(charlie).
male(dan).
male(edward).

female(alice).
female(betsy).
female(diana).

parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).

parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).

parent(bob, carl).
parent(bob, charlie).


related(X, Y) :-
	parent(X, Y).
	

related(X, Y) :- 
	parent(X, Z),
	related(Z, Y).


get_grandchild(Z) :- 
	parent(Z, X),
	parent(X, Y),
	write(Z),
	write(' grandchild is: '),
	write(Y), nl.
	
get_grandparent(X, Y) :- 
	parent(Y, X),
	parent(Z, Y),
	format('~w ~s grandparent of ~w ~n', [Z, "is the", X]).
	
brother(bob, bill).

get_uncle(X) :-
	parent(Y, X),
	brother(Y, Z),
	format('~w is the grandparent of ~w ~n',[Z, X]).

blushes(X) :- human(X).
human(derek).

stabs(tybalt, mercutio, sword).
hates(romeo, X) :- stabs(X, mercutio, sword).


what_grade(5) :-
	write('Go to kindergarten'),
	!.
	
what_grade(6) :-
	write('Go to 1st Grade').
	
what_grade(Other) :- 
	Grade is Other - 5,
	format('Go to grade ~w', [Grade]).



loves(romeo, juliet). 

loves(juliet, romeo) :- loves(romeo, juliet).

happy(albert).
happy(alice).
happy(bob).
happy(bill).
with_albert(alice).


runs(albert) :-
	happy(albert).
	
dances(alice) :-
	happy(alice),
	with_albert(alice).
	
does_alice_dance :- dances(alice),
	write('When Alice is happy and with albert she dances').
	
	
swims(bill) :-
	happy(bill).
	
swims(bill) :-
	near_water(bill).