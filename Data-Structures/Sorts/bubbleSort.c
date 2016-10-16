#include<stdlib.h>
#include<stdio.h>


void buildArray(int*, int, char**);
void bubbleSort(int*, int);

int main(int argc, char** argv)
{
  if (argc > 1)
  {
    int size = argc-1;
    int* array = malloc(size * sizeof(array));

    buildArray(array, size, argv);

    bubbleSort(array, size);
  }

  return 0;

}

void bubbleSort(int* arr, int size)
{
  int swapCounter = -1;
  do
  {
    for (int i = 0; i < size; i++)
      printf("%d ", arr[i]);
    printf("\n");
    swapCounter = 0;
    for (int i = 0; i < size - 1; i++)
    {
      if (arr[i] > arr[i+1])
      {
        int aux = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = aux;
        swapCounter++;
      }
    }
  }while (swapCounter != 0);
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
