#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

ll powerOfTwo(map<ll,int> &m){
    // costruisco look up table delle potenze di due
    ll limite = 10e9, x = 2;
    set<ll> lut;
    while (x < limite)
    {
        lut.insert(x);
        x <<= 1;
    }

    // cerco ogni combinazione per ogni potenza di due per ogni numero
    ll ris = 0;
    for (auto &p: m){
        ll a = p.first;
        ll ca = p.second;

        for (auto power: lut){
            // cerco target
            ll target = power - a;
            auto it = m.find(target);
            if(it == m.end()) continue;
            ll b = it->first;
            ll cb = it->second;
            if (b < a) continue;

            // calcolo
            if(a == b){
                if(cb > 1) ris += cb * (cb-1) / 2;
            }else ris += ca * cb;
        }
    }
    
    return ris;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    map<ll,int> m;
    for(int i = 0;i < n;i++){
        ll x;
        cin >> x;
        m[x]++;
    }
    auto ris = powerOfTwo(m);
    cout << ris << endl;
    return 0;
}