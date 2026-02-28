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

ll solve(vll &candies,vll &oranges){
    ll minCandy = candies[0], minOrange = oranges[0];
    for (size_t i = 1; i < candies.size(); i++)
    {
        if(candies[i] < minCandy) minCandy = candies[i];
        if(oranges[i] < minOrange) minOrange = oranges[i];
    }
    
    ll c = 0;
    for (size_t i = 0; i < candies.size(); i++)
    {
        while(candies[i] != minCandy || oranges[i] != minOrange){
            if(candies[i] > minCandy && oranges[i] > minOrange){
                ll massimo = min(candies[i]-minCandy,oranges[i]-minOrange);
                c += massimo; oranges[i] -= massimo; candies[i] -= massimo;
            }else if(candies[i] > minCandy){
                c += candies[i]-minCandy; candies[i] = minCandy;
            }else{
                c += oranges[i]-minOrange; oranges[i] = minOrange;
            }
        }
    }
    
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t; cin >> t;
    for (size_t i = 0; i < t; i++)
    {
        int n; cin >> n;
        vll candies(n), oranges(n);
        for (size_t j = 0; j < n; j++) cin >> candies[j];        
        for (size_t j = 0; j < n; j++) cin >> oranges[j];   
        auto ris = solve(candies,oranges);
        cout << ris << endl;     
    }
    
    return 0;
}