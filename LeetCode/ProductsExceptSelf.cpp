#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, i, x;
    int prefix = 1, suffix = 1;
    cin >> n >> i;
    vi nums, pf, sf(n+1,1);

    pf.push_back(prefix);
    
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        prefix *= x;
        pf.push_back(prefix);
        nums.push_back(x);
    }

    for (int i = n-1; i >= 0; i--)
    {
        suffix *= nums[i];
        sf[i] = suffix;
    }

    cout << pf[i-1] * sf[i+1] << endl;

    return 0;
}