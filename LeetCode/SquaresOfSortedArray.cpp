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

vector<int> sortedSquares(vector<int>& nums) {
    vector<int> answer(nums.size());
    int index = nums.size()-1;
    int l = 0, r = nums.size()-1;
    while (l <= r)
    {
        if(abs(nums[l]) >= abs(nums[r])) {
            answer[index--] = (nums[l] * nums[l]);
            l++;
        }else{
            answer[index--] = (nums[r] * nums[r]);
            r--;
        }
    }
    return answer;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = sortedSquares(nums);
    for (auto n: ris){
        cout << n << ' ';
    }
    return 0;
}