member(Element,[Element|_List]).
member(Element,[_First|Tail]) :- member(Element,Tail).

delete(X,[Fi|Li],Lo) :-
  Fi = X,
  Li = Lo.
delete(X,[Fi|Li],[Fo|Lo]) :-
  Fi = Fo,
  Fi \= X,
  delete(X,Li,Lo).

/* Sort individual clauses */

sortClauses([], []).
sortClauses([H|List], [H1|Out]) :-
  sort(H,H1),
  sortClauses(List, Out).                                          

/* Sort the independent clauses of input list and call resolve */

resolve(List) :-
  sortClauses(List, L),              
  do_resolve(L).

/* Find a resolvent and if it is empty, the given input is unsatisfiable.
   Else append the resolvent to the input list and continue resolving */

do_resolve(List) :-                       
  once(get_resolvent(List, Resolvent)),
  (Resolvent = []
  -> true
  ;resolve([Resolvent|List])
  ).

/* Taking two clauses A and B from List, and resolve them */

get_resolvent(List, Resolvent) :-
  member(A, List),
  member(B, List),
  A \= B,
  res(A, B, T),
  (T = false
  -> false
  ;(member(T, List)
  -> false
  ; Resolvent = T)
  ).

/* We have two clauses A and B here. We try to find an atomic element in both
   the clauses which is of the form  x, not(x) and cancel them. Append the rest
   of the atoms to form a resolvent. Then sort the final resolvent */

res(A, B, T) :-
  member(A1, A),
  (A1 = X
  -> B1 = -X
  ; -B1 = A1),
  (member(B1, B)
  -> delete(A1, A, TempA),
     delete(B1, B, TempB),
     append(TempA, TempB, Ans),
     sort(Ans, T)
  ; false
  ).       

resolve_pr(List) :-
  sortClauses(List, L),              
  do_resolve_pr(L).

do_resolve_pr(List) :-                       
  once(get_resolvent_pr(List, Resolvent)),
  (Resolvent = []
  -> true
  ; resolve_pr([Resolvent|List])
  ).

/* Printing once we resolve something and get a valid resolvent */

get_resolvent_pr(List, Resolvent) :-
  member(A, List),
  member(B, List),
  A \= B,
  res(A, B, T),
  (T = false
  -> false
  ;(member(T, List)
  -> false
  ;
  Resolvent = T),
  write('Source 1 : '),writeln(A),
  write('Source 2 : '),writeln(B), 
  write('Resolvent : '),writeln(Resolvent),writeln('')
  ).
