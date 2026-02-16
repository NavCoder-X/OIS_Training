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

void solve(map<ll,ll> &flowers){
    auto first = flowers.begin(), last = flowers.end();
    last--;
    if(flowers.size() == 1){
        cout << 0 << " " << first->second * (first->second - 1) / 2;
    }else{
        cout << abs(first->first - last->first) << " " << first->second * last->second;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    map<ll,ll> m;
    for(int i = 0;i < n;i++){
        ll x; 
        cin >> x;
        m[x]++;
    }

    solve(m);
    return 0;
}