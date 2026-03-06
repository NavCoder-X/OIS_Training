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

int solve(vi &sveglie,int inizio){
    sort(sveglie.begin(),sveglie.end());
    for (size_t i = 0; i < sveglie.size(); i++)
    {
        if(sveglie[i] >= inizio){
            return sveglie[i]-inizio;
        }
    }

    return (24*60)-inizio + sveglie[0];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t; cin >> t;
    for (size_t i = 0; i < t; i++)
    {
        int n, h, m;cin >> n >> h >> m;
        int inzio = h*60+m;
        vi sveglie(n);
        for (size_t j = 0; j < n; j++)
        {
            cin >> h >> m;
            sveglie[j] = h*60 + m;
        }
        auto ris = solve(sveglie,inzio);
        h = ris/60, m = ris%60;
        cout << h << " " << m << endl;
    }
    
    return 0;
}