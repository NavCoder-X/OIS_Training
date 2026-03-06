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

ll solve(int n){
    if(n > 45) return -1;
    int sum = 0;
    vector<bool> usati(10);
    for (size_t i = 9; i > 0; i--)
    {
        if(sum+i <= n){
            sum += i; usati[i] = 1;
        }
    }
    ll ris = 0;
    for (size_t i = 1; i < 10; i++)
    {
        if(usati[i]){
            ris *= 10;
            ris += i;
        }
    }
    
    return ris;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t; cin >> t;
    for (size_t i = 0; i < t; i++)
    {
        int n; cin >> n;
        auto ris = solve(n);
        cout << ris << endl;
    }
    

    return 0;
}