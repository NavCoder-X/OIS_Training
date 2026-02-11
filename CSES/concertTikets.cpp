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
        if(biglietto != prices.end() && biglietto->first <= n){
            cout << biglietto->first << endl;
            if(biglietto->second == 1) prices.erase(biglietto);
            else prices[biglietto->first]--;
        }else if(biglietto != prices.begin()){
            biglietto--;
            cout << biglietto->first << endl;
            if(biglietto->second == 1) prices.erase(biglietto);
            else prices[biglietto->first]--;
        }else{
            cout << -1 << endl;
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
        cin >> customers[i];
    }

    solve(prices,customers);
    
    return 0;
}