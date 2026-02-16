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

int solve(vi &planks,int k){
    int i = 0, j = k;
    int sum = 0, minimo = 0, index = 0;

    // computo la somma della prima finestra
    while (i <= k-1) sum += planks[i++];
    minimo = sum; i = 0;

    while (j < planks.size())
    {
        sum -= planks[i++];
        sum += planks[j++];
        if(minimo >= sum){
            minimo = sum;
            index = i;
        }
    }
    
    return index+1;
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

    auto ris = solve(nums,k);
    cout << ris << endl;
    return 0;
}