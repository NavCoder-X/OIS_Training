#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

vector<string> findRelativeRanks(vector<int>& score) {
    map<int,int,greater<int>> m;
    vector<string> ris(score.size());
    for (int i = 0; i < score.size(); i++)
    {
        m[score[i]] = i;
    }

    int i = 0;
    for (auto &p: m){
        i++;
        if(i == 1) ris[p.second] = "Gold Medal";
        else if(i == 2) ris[p.second] = "Silver Medal";
        else if(i == 3) ris[p.second] = "Bronze Medal";
        else ris[p.second] = to_string(i);
    }   
    
    return ris;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = findRelativeRanks(nums);
    for (auto n: ris){
        cout << n << endl;
    }
    return 0;
}