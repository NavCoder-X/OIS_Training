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
 
    ll n; cin >> n;
    vll monete = {100,20,10,5,1};
    ll c = 0;
    for (auto m: monete){
        c += n / m;
        n = n % m;
    }
    cout << c;
    
    return 0;
}