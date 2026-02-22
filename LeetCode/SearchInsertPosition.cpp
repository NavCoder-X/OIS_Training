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

int searchInsert(vector<int>& nums, int target) {
    int l = 0, r = nums.size()-1;
    while (l<=r)
    {
        int mid = l + (r-l) / 2;
        if(nums[mid] == target) return mid;
        else if(nums[mid] > target) r = mid-1;
        else l = mid+1;
    }
    return l;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, k;
    cin >> n >> k;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = searchInsert(nums,k);
    cout << ris << endl;
    return 0;
}