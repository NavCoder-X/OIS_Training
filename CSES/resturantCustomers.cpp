#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int kadanes(map<ll,ll> m){
    int cur = 0;
    int massimo = 0;
    for (auto &p: m){
        cur = max(p.second,cur+p.second);
        massimo = max(massimo,cur);
    }

    return massimo;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    map<ll,ll> m;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        m[a]++;
        m[b]--;
    }

    auto ris = kadanes(m);
    cout << ris << endl;
    return 0;
}