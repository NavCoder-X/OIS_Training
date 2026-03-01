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
    for (size_t i = 0; i < t; i++)
    {
        ll a, b; cin >> a >> b;
        ll ris = (abs(a-b))/10;
        if(abs(a-b) % 10 != 0) ris++;
        cout << ris << endl;
    }
    
    return 0;
}