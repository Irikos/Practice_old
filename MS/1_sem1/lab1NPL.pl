/* 
irinaciocan.ro -lab1 = sistemeExpert -> lab1 
SICStus Prolog -> file -> consult */

p(X):- 2 + X < 7 , X mod 2 =:= 0.

culoare(rosu).
culoare(albastru).
culoare(galben).

/*
% P (+X) --- inseamna ca X trebuie sa fie instantiat, sa aiba o valoare
% culoare(?X)

, = and
; = or
\+ = not


! --- cut, opreste backtrackingul

*/

obiect(a).
obiect(b).
obiect(c).
/*
pred(X,Y):- obiect(x), obiect(y).

\?- pred(x, y).

*/

afis(N):- N > 0, write('#'), N1 is N-1, afis(N1).
afis(0).

afis_l([H|T]):- write(H), afis_l(T).
afis_l([]).

%membru(2, [1, 2, 3]) .
membru(X, [X | _ ]).
membru(X, [_ | T]):- membru(X, T).