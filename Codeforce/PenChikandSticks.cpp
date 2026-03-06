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

int solve(vi &nums){
    for (int i = 0; i < nums.size()-1; i++)
    {
        if(nums[i] == i+1) continue;
        else if(nums[i] == i+2 && nums[i+1] == i+1){
            swap(nums[i],nums[i+1]);
        }else return false;
    }

    return true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t;cin >> t;
    for (size_t i = 0; i < t; i++)
    {
        int n; cin >> n;
        vi nums(n);
        for (size_t j = 0; j < n; j++)
            cin >> nums[j];
        
        auto ris = solve(nums);
        cout << (ris ? "YES" : "NO") << endl;
    }
    

    return 0;
}