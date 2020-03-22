#include <stdio.h>
#include <stdlib.h>


int main(int argc, char** argv)
{
  int k = 4;
  int* pk = &k;
  printf("%d and %d", k, *pk);
}
