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

int solve(vi &nums,int t){ // SE fosse ordinato
    for (int i = 0; i < nums.size(); i++)
    {
        int l = i+1, r = nums.size()-1;
        int tx = t-nums[i];
        while (l <= r)
        {
            int mid = l + (r-l)/2;
            if(nums[mid] == tx){
                cout << i << " " << mid << endl;
                return 1;
            }else if(nums[mid] > tx) r = mid-1;
            else l = mid+1;
        }
        
    }
    cout << "IMPOSSIBOLE" << endl;
    return -1;
}

int Hsolve(vi &nums,int t){
    map<int,int> m;
    for (int i = 0; i < nums.size(); i++)
    {
        int tx = t-nums[i];
        if(m.find(tx) != m.end()){
            cout << i+1 << " " << m[tx]+1 << endl;
            return 1;
        }
        m[nums[i]] = i;
    }
    cout << "IMPOSSIBLE" << endl;
    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, t;
    cin >> n >> t;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    Hsolve(nums,t);
    return 0;
}