#include <iostream>
#include <ctime>
#include <cstdlib>

/*
NOTA: versione poco piu ottimizata rispetto allo sapzio utilizzando un buffer di apoggio in modo da non riempire lo stack e allocare sempre nuovi array.
forse a sto punto e meglio farlo iterativo?

*/

using namespace std;

#define SIZE 10
#define MAX 10
#define MIN 1

int buffer[SIZE];

void riempi(int arr[],int size) {
    for(int i = 0; i < size; i++) {
        arr[i] = rand() % (MAX - MIN + 1) + MIN;
    }
}

void stampa(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void copia(int * a, int * b,int start,int end){
    for (size_t i = start; i < end; i++)
    {
        a[i] = b[i];
    }
}

void merge(int * array,int start, int mid, int end){
    int i = start, j = mid, k = start;
    while (i < mid && j < end)
    {
        if(array[i] < array[j]) buffer[k++] = array[i++];
        else buffer[k++] = array[j++];
    }

    while(i < mid) buffer[k++] = array[i++];
    while(j < end) buffer[k++] = array[j++];
    copia(array,buffer,start,end);
}

void divide(int * array,int start,int end){
    if(end - start <= 1) return;

    int mid = (start+end)/2;
    divide(array,start,mid);
    divide(array,mid,end);

    return merge(array,start,mid,end);
}

int main(){
    int array[SIZE];
    riempi(array,SIZE);
    stampa(array,SIZE);
    divide(array,0,SIZE);
    stampa(array,SIZE);

    return 0;
}