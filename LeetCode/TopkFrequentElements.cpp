#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int,int> freq;
    for (auto n: nums) {
        freq[n]++;
    }

    vector<pair<int,int>> items(freq.begin(), freq.end());
    sort(items.begin(), items.end(), [](const pi &a, const pi &b) {
        return a.second > b.second;
    });

    vector<int> ris;
    for (int i = 0; i < k && i < items.size(); i++) {
        ris.push_back(items[i].first);
    }
    return ris;
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
    
    auto ris = topKFrequent(nums,k);
    for (auto n: ris){
        cout << n << ' ';
    }
    return 0;
}