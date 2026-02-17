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

int solve(vi & prezzi, int n){
    if(n <= 0) return 0;

    // look up table
    vector<int> lut(n+1);
    for (int i = 0; i <= n; i++)
    {
        int massimo = prezzi[i];
        for (int j = i-1; j > 0; j--)
        {
            int precedente = lut[j] + prezzi[i-j];
            massimo = max(massimo,precedente);
        }
        lut[i] = massimo;
    }
    
    return lut[n];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n; cin >> n;
    vi prezzi(n+1);

    for (int i = 0; i < n; i++)
    {
        cin >> prezzi[i+1];
    } 
    prezzi[0] = 0;

    auto ris = solve(prezzi,n);
    cout << ris << endl;
    return 0;
}