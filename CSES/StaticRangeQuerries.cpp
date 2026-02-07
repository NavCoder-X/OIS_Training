#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<ll> vi;
typedef pair<int,int> pi;

ll Querry(vi &v,ll a,ll b){
    return v[b] - v[a-1];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    ll n, q;
    ll x, sum = 0;
    vi prefixSum;
    cin >> n >> q;

    // lettura
    for(int i = 0;i < n;i++){
        prefixSum.push_back(sum);
        cin >> x;
        sum += x;
    }
    prefixSum.push_back(sum);

    // for (auto n: prefixSum){
    //     cout << n << ' ';
    // }

    for (int i = 0; i < q; i++)
    {
        ll a, b;
        cin >> a >> b;
        auto ris = Querry(prefixSum,a,b);
        cout << ris << endl;
    }

    return 0;
}