#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int maxSubarraySumCircular(vector<int>& nums) {
    int maxSum = nums[0], minSum = nums[0], sum = nums[0];
    int currentMax = nums[0], currentMin = nums[0];

    for (int i = 1; i < nums.size(); i++)
    {
        currentMax = max(nums[i], currentMax + nums[i]);
        maxSum = max(maxSum, currentMax);

        currentMin = min(nums[i], currentMin + nums[i]);
        minSum = min(minSum, currentMin);

        sum += nums[i];
    }
    
    if (sum == minSum) {
        return maxSum;
    }
    return max(maxSum, sum - minSum);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    vi nums;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        nums.push_back(x);
    }

    auto ris = maxSubarraySumCircular(nums);
    cout << ris;
    
    return 0;
}