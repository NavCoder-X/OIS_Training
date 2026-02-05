#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;

#define DIM 10
#define MAX 9
#define MIN -9

void riempi(int * array,int n){
    for (int i = 0; i < n; i++)
    {
        array[i] = rand()%(MAX-MIN+1)+MIN;
    }
}

void stampa(int * array,int n){
    for (int i = 0; i < n; i++)
    {
        cout << array[i] << " ";
    }
    cout << endl;
}


// scelgo il pivot come primo elemento
// patisco l array in modo da avere tutti gli elemnti minori del pivot prima e quelli maggiori dopo
// alla fine il pivot sara nella pos giusta e ritorno l indice della pos giusta
int ordina(int * array,int low,int high){
    if(high - low < 1) return -1;
    int i = low, j = low+1;
    int pivot = array[low];

    while(j <= high){
        if(array[j] <= pivot){
            i++;
            swap(array[i],array[j]);
        }
        j++;
    }
    array[low] = array[i];
    array[i] = pivot;

    return i;
}

// ordino dal pivot in poi e prima del pivot ricorsivamente
void QuickSort(int * array,int low,int high){
    if(low < high){
        int m = ordina(array,low,high);
        QuickSort(array,low,m-1);
        QuickSort(array,m+1,high);
    }
}

int main() {
    int array[DIM];
    srand(time(NULL));  
    
    riempi(array,DIM);
    stampa(array,DIM);
    QuickSort(array,0,DIM-1);
    stampa(array,DIM);

    return 0;
}