#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

ll solve(vll & nums,int k){
    if(k > nums.size()) return -1;
    ll limite = 10e9+1;
    sort(nums.begin(),nums.end());

    if(k == 0 && nums[0]-1 > 0) return nums[0]-1;
    if(nums.size() > k && nums[k-1] == nums[k]) return -1;
    if(nums.size() == k && nums[k-1] < limite) return nums[k-1];
    if(nums.size() >= k && nums[k-1]+1 == nums[k]) return nums[k-1];
    if(nums[k-1]+1 < limite) return nums[k-1]+1;
    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, k;
    cin >> n >> k;

    vll nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = solve(nums, k);
    cout << ris << endl;
    return 0;
}