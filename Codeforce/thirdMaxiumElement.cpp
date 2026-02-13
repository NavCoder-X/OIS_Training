#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int thirdMax(vector<int>& nums) {
    priority_queue<int,vector<int>,greater<int>> pq;
    set<int> seen;
    int k = 3;

    for (auto n: nums){
        if(seen.count(n)) continue;

        if(pq.size() < 3) pq.push(n);
        else if(pq.size() == 3 && n > pq.top()){
            pq.pop();
            pq.push(n);
        }

        seen.insert(n);
    }

    if(pq.size() < 3){
        int massimo = pq.top();
        while(!pq.empty()){
            massimo = max(massimo,pq.top());
            pq.pop();
        }
        return massimo;
    }

    return pq.top();
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
    
    auto ris = thirdMax(nums);
    cout << ris << endl;
    return 0;
}