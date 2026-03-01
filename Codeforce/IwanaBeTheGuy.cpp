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
 
    int n; cin >> n;
    set<int> s;
    int p; cin >> p;
    for (size_t j = 0; j < p; j++){
        int x; cin >> x; s.insert(x);
    }
    int q; cin >> q;
    for (size_t j = 0; j < q; j++){
        int x; cin >> x; s.insert(x);
    }
    if(s.size() == n) cout << "I become the guy.";
    else cout << "Oh, my keyboard!";        
    
    return 0;
}