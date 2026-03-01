#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <string>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

int solve(string &s){
    if(s.size() < 2) return 2;
    int c = 1;
    int massimo = 1;
    for (size_t i = 1; i < s.size(); i++)
    {
        if(s[i] != s[i-1]) c = 0;
        else c++;
        massimo = max(massimo,c);
    }
    
    return massimo+1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t; cin >> t;
    for (size_t i = 0; i < t; i++)
    {
        int n; cin >> n;
        string s; cin >> s;
        auto ris = solve(s);
        cout << ris << endl;
    }
    

    return 0;
}