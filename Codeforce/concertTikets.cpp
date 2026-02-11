#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

void solve(map<int,int> &prices, vi &customers){
    for (int i = 0; i < customers.size(); i++)
    {
        int n = customers[i];
        auto biglietto = prices.lower_bound(n);
        if(*(biglietto) <= n){

        }
    }
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, m;
    cin >> n >> m;
    vi customers(m);
    map<int,int> prices;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        prices[x]++;
    }

    for (int i = 0; i < m; i++)
    {
        cin >> prices[i];
    }

    solve(prices,customers);
    
    return 0;
}