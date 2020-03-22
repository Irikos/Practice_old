#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  char* s = malloc(strlen("let's test this") + 1);
  char* t = malloc(strlen("let's test this") + 1);
  strcpy(s, "let's test this                        now");
  // strcpy(t, "testing...");

  printf("s -> %s\n", s);
  printf("t -> %s\n", t);

  printf("address of s: %d and size: %lu\n", s, strlen(s));
  printf("address of t: %d and size: %lu\n", t, strlen(t));
  free(s);
  free(t);

  return 0;
}
