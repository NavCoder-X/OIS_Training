#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

bool containsNearbyDuplicate(vector<int> nums, int k){
    if(nums.size() <= 1 || k == 0) return 0;
    map<int,int> m;

    for (int i = 0; i < nums.size(); i++)
    {
        if(m.find(nums[i]) != m.end()){
            if(abs(i - m[nums[i]]) <= k) return true;
        }
        m[nums[i]] = i; 
    }
    
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, k;
    cin >> n >> k;
    vi nums(n);

    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    
    auto ris = containsNearbyDuplicate(nums,k);
    cout << ris;
    return 0;
}