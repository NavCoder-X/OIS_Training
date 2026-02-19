#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

ll solve(string &s){
    ll sum = 0, c = 0, value;
    map<ll,ll> m;
    m[0]++;

    for (ll i = 0; i < s.size(); i++)
    {
        sum += s[i] - '0';
        value = sum - (i+1);
        if(m.find(value) != m.end()) c+=m[value];
        m[value]++;
    }
    
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        string s;
        cin >> n;
        cin >> s;
        auto ris = solve(s);
        cout << ris << endl;
    }
    
    return 0;
}