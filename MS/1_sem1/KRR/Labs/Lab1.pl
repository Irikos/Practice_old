parent(ion, maria).
parent(ana, maria).
parent(ana, dan).
parent(maria, elena).
parent(maria, radu).
parent(elena, nicu).
parent(radu, george).
parent(radu, dragos).


brother(X,Y) :- parent(Z,X), parent(Z,Y), X\=Y.

grandparent(X,Y) :- parent(Z, Y), parent(X, Z).