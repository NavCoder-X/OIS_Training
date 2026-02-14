#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

class KthLargest {
public:
    priority_queue<int,vector<int>,greater<int>> pq;
    int K;
    KthLargest(int k, vector<int>& nums) {
        this->K = k;
        for (auto n: nums){
            if(pq.size() < k) pq.push(n);
            else if(pq.size() == k && n > pq.top()){
                pq.pop();
                pq.push(n);
            }
        }
    }
    
    int add(int val) {
        if(pq.size() < this->K) pq.push(val);
        else if(pq.size() == this->K && val > pq.top()){
            pq.pop();
            pq.push(val);
        }
        return pq.top();
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int k = 3;
    vi nums = {4,5,8,2};
    KthLargest kl(k,nums);
    cout << kl.add(3) << endl;
    cout << kl.add(5) << endl;
    cout << kl.add(10) << endl;
    cout << kl.add(9) << endl;
    cout << kl.add(8) << endl;
    return 0;
}