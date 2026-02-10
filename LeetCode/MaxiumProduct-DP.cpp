#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int maxProduct(vector<int> &nums){
    if(nums.size() <= 1) return nums[0];
    int massimo = 1, minimo = 1;
    int ris = nums[0];

    for (int i = 0; i < nums.size(); i++)
    {
        if(nums[i] == 0){
            massimo = 1; minimo = 1;
            ris = max(ris,0);
            continue;
        }
        int m1, m2;
        m1 = nums[i] * massimo;
        m2 = nums[i] * minimo;
        massimo = max({m1,m2,nums[i]});
        minimo = min({m1,m2,nums[i]});
        ris = max(ris,massimo);
    }
    
    return ris;
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

    auto ris = maxProduct(nums);
    
    return 0;
}