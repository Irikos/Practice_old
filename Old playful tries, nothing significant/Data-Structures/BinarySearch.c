#include <stdio.h>
#include <stdlib.h>

void buildArray(int* array, int size, char** elements);
int binarySearch(int value, int values[], int size);

int main(int argc, char** argv)
{
  int size = argc-1;
  int* array = malloc(size * sizeof(int));
  buildArray(array, size, argv);

  int find = binarySearch(9, array, size);
  printf("result: %d\n", find);
}

int binarySearch(int value, int values[], int size)
{
  int start = 0;
  int end = size;
  int mid;

  do
  {
    mid = (start + end) / 2;
    if (value == values[mid])
    {
      return 0;
    }
    else
    {
      if (value < values[mid])
      {
        printf("value(%d) < mid(%d)\n", value, values[mid]);
        end = mid - 1;
      }
      else
      {
        printf("value(%d) > mid(%d)\n", value, values[mid]);
        start = mid + 1;
      }
    }
  }while (value != values[mid] && start <= end);
  return -1;
}


void buildArray(int* array, int size, char** elements)
{
  if (size > 0)
  {
    for (int i = 1; i < size + 1; i++)
    {
      array[i-1] = atoi(elements[i]);
    }
  }
}
