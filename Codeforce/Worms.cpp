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

void solve(vi &worms,vi &goods){
    // somma cumulativa
    vi sum(worms.size());
    sum[0] = worms[0]; 
    for (int i = 1; i < worms.size(); i++){
        sum[i] = sum[i-1] + worms[i];
    }

    // ricerca vermi buoni
    for (int i = 0; i < goods.size(); i++)
    {
        int l = 0, r = worms.size();
        int answer = r;
        while (l <= r)
        {
            int mid = l + (r-l)/2;
            if(sum[mid] >= goods[i]){
                answer = mid+1;
                r = mid-1;
            }else l = mid+1;
        }
        cout << answer << endl;
    }
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, m; cin >> n;
    vi piles(n); 
    for (int i = 0; i < n; i++)
        cin >>  piles[i];
    cin >> m;
    vi goods(m);
    for (int i = 0; i < m; i++)
        cin >>  goods[i];
    
    solve(piles,goods);
    return 0;
}