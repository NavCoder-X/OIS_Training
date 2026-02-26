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

int jump(vector<int>& nums) {
    if(nums.size() <= 1) return 0;
    unsigned m = nums[0], massimo = 0, c = 1;
    for (unsigned i = 1; i < nums.size(); i++)
    {
        if(i > m){
            c++;
            m = massimo;
            massimo = 0;
        }
        massimo = max(massimo,i+nums[i]);
    }
    return c;
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

    auto ris = jump(nums);
    cout << ris << endl;
    return 0;
}