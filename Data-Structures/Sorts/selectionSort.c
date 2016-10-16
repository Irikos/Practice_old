#include<stdlib.h>
#include<stdio.h>


void buildArray(int*, int, char**);
void selectionSort(int*, int);

int main(int argc, char** argv)
{
  if (argc > 1)
  {
    int size = argc-1;
    int* array = malloc(size * sizeof(int));

    buildArray(array, size, argv);

    selectionSort(array, size);
  }

  return 0;

}

void selectionSort(int* arr, int size)
{
  int minPosition = 0;

  for (int k = 0; k < size; k++)
    printf("%d ", arr[k]);
  printf("\n");
  
  for (int i = 0; i < size; i++)
  {
    minPosition = i;
    for (int j = i; j < size; j++)
    {
      if (arr[j] < arr[minPosition])
      {
        minPosition = j;
      }
    }
    int aux = arr[i];
    arr[i] = arr[minPosition];
    arr[minPosition] = aux;

    for (int k = 0; k < size; k++)
      printf("%d ", arr[k]);
    printf("\n");
  }
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
