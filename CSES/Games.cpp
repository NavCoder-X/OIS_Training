#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int solve(vector<pi> &teams){
    int sum = 0;
    for (int i = 0; i < teams.size(); i++)
    {
        for (int j = 0; j < teams.size(); j++)
        {
            if(i != j){
                if(teams[i].second == teams[j].first) sum++;
            }
        }
    }
    
    return sum;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;
    vector<pi> teams(n);

    for (int i = 0; i < n; i++)
    {
        cin >> teams[i].first >> teams[i].second;
    }

    auto ris = solve(teams);
    cout << ris;
    
    return 0;
}