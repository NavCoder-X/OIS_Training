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

ll solve(vector<pair<unsigned,unsigned>> &tasks){
    // ordino per durata
    sort(tasks.begin(),tasks.end());
    ll c = 0, t = 0;
    for (size_t i = 0; i < tasks.size(); i++)
    {
        t += tasks[i].first;
        c += tasks[i].second - t; 
    }
    
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    unsigned n; cin >> n;
    vector<pair<unsigned,unsigned>> nums(n);
    for (size_t i = 0; i < n; i++)
    {
        unsigned a, b; cin >> a >> b;
        nums[i] = make_pair(a,b);
    }
    auto ris = solve(nums);
    cout << ris;
    return 0;
}