
la_stanga(X,Y):- X is Y - 1. % is este "==" .... ; este SAU     , este SI   . este final
la_dreapta(X,Y):- X is Y + 1.
vecin(X,Y):- la_stanga(X,Y) ; la_dreapta(X,Y).
pred(Pers):- All = [
				casa(1, Nat1,Col1, Animal1,Drink1,Smoke1),
				casa(2, Nat2,Col2, Animal2,Drink2,Smoke2),
				casa(3, Nat3,Col3, Animal3,Drink3,Smoke3),
				casa(4, Nat4,Col4, Animal4,Drink4,Smoke4),
				casa(5, Nat5,Col5, Animal5,Drink5,Smoke5)
				],
			member(casa(_,britanic,rosie,_,_,_),All),  %Britanicul locuieşte în casa roşie.
			member(casa(_,suedez,_,caine,_,_),All), %Suedezul are un câine.
			member(casa(_,_,galbena,_,_,dunhill),All), %Locatarul din casa galbenă fumează Dunhill.
			member(casa(_,_,verde,_,cafea,_),All), %Locatarul casei verzi bea cafea.
			
			member(casa(3,_,_,_,lapte,_),All), %Locatarul casei din mijloc bea lapte.
			member(casa(1,norvegian,_,_,_,_),All),%Norvegianul locuieşte în prima casă.
			member(casa(_,_,_,pasare,_,pallmall),All), %Persoana care fumează Pall Mall are o pasăre.
			member(casa(_,_,_,_,bere,winfield),All),%Fumătorul de Winfield bea bere.
			member(casa(_,german,_,_,_,rothmans),All),%Germanul fumează Rothmans.
			member(casa(P1,norvegian,_,_,_,_),All), %Norvegianul locuieşte lângă casa albastră.
			member(casa(P2,_,albastra,_,_,_),All),	
			vecin(P1,P2),
			member(casa(P3,_,verde,_,_,_),All),%Casa verde se află în stânga casei albe.			
			member(casa(P4,_,alba,_,_,_),All),
			la_stanga(P3,P4),
			member(casa(P5,_,_,_,_,marlboro),All),%Fumătorul de Marlboro locuieşte lângă cel care are o pisică.
			member(casa(P6,_,_,pisica,_,_),All),
			vecin(P5,P6),
			member(casa(P7,_,_,cal,_,_),All),%Locatarul care are un cal locuieşte lângă cel care fumează Dunhill.
			member(casa(P8,_,_,_,_,dunhill),All),
			vecin(P7,P8),
			member(casa(P9,_,_,_,apa,_),All),%Fumătorul de Marlboro are un vecin care bea apă.
			member(casa(P10,_,_,_,_,marlboro),All),
			vecin(P9,P10),
			member(casa(_,_,_,_,ceai,_),All),
			member(casa(_,danez,_,_,_,_),All),
			member(casa(_,Pers,_,pesti,_,_),All).
			
				/*
			member(casa(_,danez,_,_,_,_),All),
			member(casa(_,britanic,_,_,_,_),All),
			member(casa(_,suedez,_,_,_,_),All),
			member(casa(_,norvegian,_,_,_,_),All),
			member(casa(_,german,_,_,_,_),All),
			
			member(casa(_,_,rosie,_,_,_),All),
			member(casa(_,_,alba,_,_,_),All),
			member(casa(_,_,albastra,_,_,_),All),
			member(casa(_,_,galbena,_,_,_),All),
			member(casa(_,_,verde,_,_,_),All),
			
			member(casa(_,_,_,pisica,_,_),All),
			member(casa(_,_,_,pasare,_,_),All),
			member(casa(_,_,_,caine,_,_),All),
			member(casa(_,_,_,pesti,_,_),All),
			
			member(casa(_,_,_,_,ceai,_),All),
			member(casa(_,_,_,_,lapte,_),All),
			member(casa(_,_,_,_,bere,_),All),
			member(casa(_,_,_,_,apa,_),All),
			member(casa(_,_,_,_,cafea,_),All),
			
			member(casa(_,_,_,_,_,pallmall),All),
			member(casa(_,_,_,_,_,winfield),All),
			member(casa(_,_,_,_,_,dunhill),All),
			member(casa(_,_,_,_,_,marlboro),All),
			member(casa(_,_,_,_,_,rothmans),All),
			*/
			
			
			
			
			
			
			
			
			
			
			
			
			%member(casa(_,Pers,_,pesti,_,_),All), write(Pers).
			
			%! daca vreau sa se opreasca dupa prima varianta
			
			%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
			%member(casa(_,danez,_,_,ceai,_),All),%Regula lipsa! : The Dane drinks tea.
			%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%













