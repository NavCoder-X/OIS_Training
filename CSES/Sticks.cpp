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

ll solve(vll &bastoni){
    ll c = 0;
    // ordino per lunghezza
    sort(bastoni.begin(),bastoni.end());
    ll mid = bastoni[bastoni.size()/2];
    for (size_t i = 0; i < bastoni.size(); i++)
        c += abs(bastoni[i]-mid);
    
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    vll nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = solve(nums);
    cout << ris << endl;
    return 0;
}