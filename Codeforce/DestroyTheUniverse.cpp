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

int solve(vll &nums){
    // conto le porzioni delimitate da zeri
    int c = 0;
    for (size_t i = 0; i < nums.size(); i++)
    {
        if(nums[i] != 0){
            c++;
            while(i < nums.size() && nums[i] != 0) i++;
        }
    }
    
    if(c < 2) return c;
    return 2;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t; cin >> t;
    for (size_t i = 0; i < t; i++)
    {
        int n; cin >> n;
        vll nums(n);
        for (size_t j = 0; j < n; j++) cin >> nums[j];
        auto ris = solve(nums);
        cout << ris << endl;
    }   
    
    return 0;
}