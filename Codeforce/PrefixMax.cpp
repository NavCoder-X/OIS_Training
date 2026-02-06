#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
 
int main() {
    int t, n;
    cin >> t;
    
    for (int i = 0; i < t; i++)
    {
        int size = 0;
        int elem;
        int massimo = 0;
        cin >> n;

        // soluzione
        for (int j = 0; j < n; j++)
        {
            size++;
            cin >> elem;
            massimo = max(massimo,elem);
        }

        cout << massimo * size << endl;
        
    }
    
    
    return 0;
}