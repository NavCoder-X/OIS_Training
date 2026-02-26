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

bool canJump(vector<int>& nums) {
    unsigned maxRaggiungibile = 0;
    for (unsigned i = 0; i < nums.size(); i++)
    {
        if(maxRaggiungibile >= nums.size()-1) return true;
        if(i <= maxRaggiungibile){
            maxRaggiungibile = max(maxRaggiungibile,i+nums[i]);
        }
    }
    
    return false;
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

    auto ris = canJump(nums);
    cout << ris << endl;
    return 0;
}