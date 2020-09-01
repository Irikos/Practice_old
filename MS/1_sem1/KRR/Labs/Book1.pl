printColor(snow) :- !, write("It's white.").
printColor(grass) :- !, write("It's green.").
printColor(sky) :- !, write("It's yellow.").
printColor(X) :- !, write("Beats me.").



printColor2(X) :- color(X, Y), !,
	write("It's "), write(Y), write(".").
printColor2(X) :- write("Beats me.").
color(snow, white).
color(sky, yellow).
color(X, Y) :- madeof(X, Z), color(Z, Y).
madeof(grass, vegetation).
color(vegetation, green).