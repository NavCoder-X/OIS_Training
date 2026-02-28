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

int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int totalFuel = 0, totalCost = 0, currentFuel = 0;
    int start = 0;
    for (size_t i = 0; i < gas.size(); i++)
    {
        totalCost += cost[i]; totalFuel += gas[i];
        currentFuel += gas[i]-cost[i];
        if(currentFuel < 0){
            currentFuel = 0;
            start = i+1;
        }
    }
    if(totalFuel >= totalCost) return start;
    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, m;
    cin >> n >> m;

    vi nums(n);
    vi costs(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }
    for(int i = 0;i < m;i++){
        cin >> costs[i];
    }

    auto ris = canCompleteCircuit(nums,costs);
    cout << ris << endl;
    return 0;
}