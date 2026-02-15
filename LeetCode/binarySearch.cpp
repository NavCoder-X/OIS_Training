#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int search(vector<int>& nums, int target) {
    int l = 0, r = nums.size() -1;
    while (l <= r)
    {
        int mid = l + (r-l)/2;
        if(nums[mid] == target) return mid;
        else if(nums[mid] > target) r = mid-1;
        else l = mid+1;
    }
    
    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, target;
    cin >> n >> target;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }
    auto ris = search(nums,target);
    cout << ris << endl;
    return 0;
}