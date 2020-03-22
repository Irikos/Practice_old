parinte(ion, maria).
parinte(ana, maria).
parinte(ana, dan).
parinte(maria, elena).
parinte(maria, radu).
parinte(elena, nicu).
parinte(radu, gigi).
parinte(radu, dragos).


max(X,Y,X):-X > Y,!.
max(_,Y,Y).

membru(X,[X|_]).
membru(X,[_|T]):-membru(X,T).


concat([], X, X).
concat([H|T], X, [H|D]):-concat(T,X,D).



remove(X, [X], []).
remove(X, [Y], [Y]):- X \==Y.
remove(X, [X|T], T1):- remove(X, T, T1).
remove(X, [Y|T], [Y|T1]):- X\==Y, remove(X, T, T1).



