#include <stdio.h>
#include <stdlib.h>

//testing char strings and pointers.
int main()
{
  char* name = "Andrei";
  char* incompleteName = name + 2;
  printf("%s\n", name);
  printf("%s\n", incompleteName);
  return 0;
}
