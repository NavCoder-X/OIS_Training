#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int findKthLargest(vector<int>& nums, int k){
    priority_queue<int> pq;
    k--;
    for (auto n: nums){
        pq.push(n);
    }

    while (!pq.empty() && k--)
    {
        pq.pop();
    }
    
    return pq.top();
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
    
    auto ris = findKthLargest(nums,k);
    cout << ris << endl;
    return 0;
}