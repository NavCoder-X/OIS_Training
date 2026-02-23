#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
 
typedef unsigned long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

bool f(ll x,vll &machines,ll t){
    ll sum = 0;
    for (int i = 0; i < machines.size(); i++)
    {
        sum += x/machines[i];
        if(sum >= t) return true;
    }
    
    return false;
}

ll solve(vll &machines,ll t){
    ll l = 0, r = machines[0]*t; // al max ci impieghiamo m[0] * t
    ll answer = r;
    while (l <= r)
    {
        ll mid = l + (r-l)/2;
        if(f(mid,machines,t)){
            answer = mid;
            r = mid-1;
        }else l = mid+1;
    }
    
    return answer;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    ll t;
    cin >> n >> t;
    vll machines(n);
    for (int i = 0; i < n; i++)
        cin >> machines[i];

    auto ris = solve(machines,t);
    cout << ris;
    return 0;
}