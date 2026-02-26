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

int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    unsigned c = 0, last = 0;
    // ordino per istante finale minore
    auto f = [](vector<int> &a,vector<int> &b){
        return a[1] < b[1];
    };
    sort(intervals.begin(),intervals.end(),f);

    for (size_t i = 1; i < intervals.size(); i++)
    {
        if(intervals[i][0] < intervals[last][1]) c++;
        else last = i;
    }
    
    return c;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    vector<vector<int>> nums;
    for(int i = 0;i < n;i++){
        int a, b; cin >> a >> b;
        vi v = {a,b};
        nums.push_back(v);
    }

    auto ris = eraseOverlapIntervals(nums);
    cout << ris << endl;
    return 0;
}