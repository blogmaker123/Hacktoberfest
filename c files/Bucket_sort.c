#include <stdio.h>
#include <stdlib.h>
 
typedef struct bucket 
{
    int count;
    int* value;
}B;
 
int compareIntegers(const void* first, const void* second)
{
    int x = *((int*)first), y =  *((int*)second);
    if (x == y)
    {
        return 0;
    }
    else if (x < y)
    {
        return -1;
    }
    else
    {
        return 1;
    }
}
 
void bucket_sort(int array[],int n)
{
    B b[3];
    int i, j, k;
    for (i = 0; i < 3; i++)
    {
        b[i].count = 0;
        b[i].value = (int*)malloc(sizeof(int) * n);
    }
    
    for (i = 0; i < n; i++)
    {
        if (array[i] < 0)
        {
            b[0].value[b[0].count++] = array[i];
        }
        else if (array[i] > 10)
        {
            b[2].value[b[2].count++] = array[i];
        }
        else
        {
            b[1].value[b[1].count++] = array[i];
        }
    }
    for (k = 0, i = 0; i < 3; i++)
    {
        // now using quicksort to sort the elements of buckets...
		// Using the library function for quick sort...

        qsort(b[i].value, b[i].count, sizeof(int), &compareIntegers);
        for (j = 0; j < b[i].count; j++)
        {
            array[k + j] = b[i].value[j];
        }
        k += b[i].count;
        free(b[i].value);
    }
}
 
int main(char *arg[]) {
 
    int n = 10;	// Size o the array...

	// The array elements...
	int array[100] = { 5, 65, 10, 1, -4, 145, 5, 4, 1234, 7 };
    
    bucket_sort(array, n); 
    
    for (int k = 0; k<10; k++)
    printf("%d ", array[k]);   

	printf("\n");
 	return 0;
}
