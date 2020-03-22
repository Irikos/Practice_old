#include <stdio.h>
#include <stdlib.h>

int collatz(int);
int main(int argc, char** argv)
{
  if (argc != 2)
  {
    printf("Invalid number of arguments, %d\n", argc);
    return 1;
  }
  else
  {
    int nr = atoi(argv[1]);
    int times = collatz(nr);
    printf("%d steps.\n", times);
    return 0;
  }
}


int collatz(int n)
{
  if (n == 1)
  {
    printf("%d\n", n);
    return 0;
  }
  else
  {
    printf("%d -> ", n);
    if (n % 2 == 0)
      return (1 + collatz(n / 2));
    else
      return (1 + collatz(3*n + 1));
    }
}
