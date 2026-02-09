#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int a, b, c = 0;
    cin >> a >> b;

    while (a <= b)
    {
        a *= 3;
        b *= 2;
        c++;
    }

    cout << c;
    
    return 0;
}