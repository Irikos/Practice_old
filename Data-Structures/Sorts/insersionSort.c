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
  }

  return 0;

}

void insertionSort(int* arr, int size)
{
  for (int k = 0; k < size; k++)
    printf("%d ", arr[k]);
  printf("\n");

  for (int i = 0; i < size - 1; i++)
  {
    int j = i + 1;
    int currentNumber = arr[j];
    while(j > 0 && currentNumber < arr[j - 1])
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
