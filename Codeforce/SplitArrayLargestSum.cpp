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

bool can(vector<int>& nums, int k, int s){
    unsigned c = 0, i = 0, sum = 0;
    while (i < nums.size())
    {
        sum += nums[i];
        if(sum > s){
            sum = 0; c++;
        }else i++;
    }
    if(sum > 0) c++;
    return c <= k;
}

int splitArray(vector<int>& nums, int k) {
    unsigned sum = nums[0], massimo = nums[0];
    for (size_t i = 1; i < nums.size(); i++)
    {
        sum += nums[i];
        if(nums[i] > massimo) massimo = nums[i];
    }

    if(k == 1) return sum;

    unsigned l = massimo, r = sum; 
    unsigned answer = r;
    while (l <= r)
    {
        auto mid = l + (r-l)/2;
        if(can(nums,k,mid)){
            answer = mid;
            r = mid-1;
        }else l = mid+1;
    }
    
    return answer;
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

    auto ris = splitArray(nums,k);
    cout << ris << endl;
    return 0;
}