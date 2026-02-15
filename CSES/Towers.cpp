#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
 
typedef long long ll;
typedef vector<ll> vi;
typedef pair<int,int> pi;

int nTowers(vi &nums){
    multiset<ll> ms;
    for (int i = 0; i < nums.size(); i++)
    {
        auto it = ms.upper_bound(nums[i]);
        if(it != ms.end()) ms.erase(it);
        ms.insert(nums[i]);
    }
    
    return ms.size();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = nTowers(nums);
    cout << ris << endl;
    return 0;
}