#include<stdlib.h>
#include<stdio.h>


void buildArray(int*, int, char**);
void insertionSort(int*, int);

int main(int argc, char** argv)
{
  if (argc > 1)
  {
    int size = argc-1;
    int* array = malloc(size * sizeof(int));

    buildArray(array, size, argv);

    insertionSort(array, size);

    free(array);
  }

  return 0;

}

void insertionSort(int* arr, int size)
{
  for (int k = 0; k < size; k++)
    printf("%d ", arr[k]);
  printf("\n");

  for (int i = 1; i < size; i++)
  {
    int j = i;
    int currentNumber = arr[i];
    while(j > 0 && arr[j - 1] > currentNumber)
    {
      arr[j] = arr[j - 1];
      j--;
    }
    arr[j] = currentNumber;

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
