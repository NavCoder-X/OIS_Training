#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

#define MAX_NODES 10
#define MAX_EDGES 10

int main() {
    int mdj[MAX_NODES][MAX_EDGES] = {0};
    cout << "inserisci una matrice di adiacenza (nodi,archi): ";

    int n, e; cin >> n >> e;
    for (int i = 0; i < e; i++)
    {
        int a, b;
        int peso;
        cout << "a->b peso : ";
        cin >> a >> b >> peso;
        mdj[a][b] = peso;
        mdj[b][a] = peso;
    }
    
    cout << "---------------------------------------------------------------" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << mdj[i][j] << " ";
        }
        cout << endl;
    }
        
    return 0;
}