#include <iostream>
using namespace std;
 
int main() {
    int t;
    int x, n;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> x >> n;
        if(n & 1) cout << x << endl;
        else cout << 0 << endl;
    }
    
    return 0;
}