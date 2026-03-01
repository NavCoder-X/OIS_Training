#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t; cin >> t;
    for (unsigned i = 0; i < t; i++)
    {
        int n; cin >> n;
        int x = n / 3;
        int a = x, b = x;
        int resto = n%3;
        if(resto == 1)a++;
        if(resto == 2)b++;
        cout << a << " " << b << endl;
    }
    
    return 0;
}