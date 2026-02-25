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

bool can(vector<int>& weights, int days, unsigned cap){
    unsigned c = 0, sum = 0, i = 0;
    while (i < weights.size())
    {
        sum += weights[i];
        if(sum > cap){
            sum = 0; c++;
        }else i++;
    }
    if(sum > 0) c++;
    return c <= days;
}

int shipWithinDays(vector<int>& weights, int days) {
    unsigned l = *max_element(weights.begin(),weights.end()), r = l*weights.size();
    unsigned answer = r;
    while (l <= r)
    {
        auto mid = l + (r-l)/2;
        if(can(weights,days,mid)){
            answer = mid;
            r = mid-1;
        }else l = mid+1;
    }
    
    return answer;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, d;
    cin >> n >> d;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = shipWithinDays(nums,d);
    cout << ris << endl;
    return 0;
}