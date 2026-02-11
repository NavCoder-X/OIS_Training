#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        if(i & 1 && i != n) cout << "I hate that ";
        else if(i & 1 && i == n) cout << "I hate it ";
        else if(i % 2 == 0 && i != n) cout << "I love that ";
        else cout << "I love it ";
    }
    
    return 0;
}