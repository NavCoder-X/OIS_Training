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

int solve(vector<pll> &movies){
    // ordino per istante finale
    int c = 0, istanteAttuale = 0;
    auto f = [](pll &a,pll &b){
        return a.second < b.second;
    };
    sort(movies.begin(),movies.end(),f);

    for (int i = 0; i < movies.size(); i++)
    {
        if(movies[i].first >= istanteAttuale){
            istanteAttuale = movies[i].second;
            c++;
        }
    }
    
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    vector<pll> nums(n);
    for(int i = 0;i < n;i++){
        ll a, b; cin >> a >> b;
        nums[i] = make_pair(a,b);
    }

    auto ris = solve(nums);
    cout << ris << endl;
    return 0;
}