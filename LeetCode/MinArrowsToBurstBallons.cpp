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

int findMinArrowShots(vector<vector<int>>& points) {
    // ordino per istante iniziale, e se uguali per finale minore
    auto f = [](vector<int> &a,vector<int> &b){
        if (a[0] == b[0]) return a[1] < b[1];
        return a[0] < b[0];
    };
    sort(points.begin(),points.end(),f);

    int c = 1, start = points[0][0], end = points[0][1];
    for (size_t i = 1; i < points.size(); i++)
    {
        if(points[i][0] <= end && points[i][0] >= start){
            start = points[i][0];
            end = min(points[i][1],end);
        }else{
            c++;
            start = points[i][0];
            end = points[i][1];
        }
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

    auto ris = findMinArrowShots(nums);
    cout << ris << endl;
    return 0;
}