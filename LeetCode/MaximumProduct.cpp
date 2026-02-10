#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int maxProduct(vector<int> &nums){
    if(nums.size() <= 1) return nums[0];

    int prefixMax = nums[0];
    int suffixMax = nums[nums.size()-1];
    int currPrefix = 1;
    int currSuffix = 1;

    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] != 0) currPrefix *= nums[i];
        else{
            if(i < nums.size()-1){
                currPrefix = nums[i+1];
                i++;
            }
            prefixMax = max({prefixMax,currPrefix,nums[i]});
            continue;
        }
        prefixMax = max({prefixMax,currPrefix,nums[i]});
    }
    
    for (int i = nums.size()-1; i >= 0; i--)
    {
        if (nums[i] != 0) currSuffix *= nums[i];
        else{
            if(i > 0){
                currSuffix = nums[i-1];
                i--;
            }
            suffixMax = max(suffixMax,currSuffix);
            continue;
        }
        suffixMax = max(suffixMax,currSuffix);
    }
    
    return prefixMax > suffixMax ? prefixMax : suffixMax;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;
    vi nums(n);

    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }

    auto ris = maxProduct(nums);
    cout << ris;
    
    return 0;
}