#include <iostream>
#include <algorithm>
using namespace std;
 
int main() {
    int t, l, a, b;
    cin >> t;

    // per ogni test
    for (int i = 0; i < t; i++)
    {
        cin >> l >> a >> b;
        int massimo = a;
        
        // brute force
        for (int j = 0; j < l; j++)
        {
            a = (a+b) % l;
            massimo = max(a,massimo);
        }

        cout << massimo << endl;
        
    }
    
    return 0;
}