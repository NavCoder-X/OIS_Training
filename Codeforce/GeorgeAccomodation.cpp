#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int solve(vector<pi> &rooms){
    int available = 0;
    for (auto &r: rooms){
        if(r.second - r.first >= 2) available++;
    }

    return available;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;
    vector<pi> rooms(n);

    for (int i = 0; i < n; i++)
    {
        cin >> rooms[i].first >> rooms[i].second;
    }

    auto ris = solve(rooms);
    cout << ris;
    
    return 0;
}