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
 
    int t, k;
    vi v;
    int ris = 0;
    cin >> t >> k;
    k--;

    for(int i = 0;i < t;i++){
        int n;
        cin >> n;
        v.push_back(n);
    }

    int target = v[k];
    sort(v.begin(),v.end(),greater<int>());

    for (auto n: v){
        if(n > 0 && n >= target) ris++;
    }

    cout << ris;
    return 0;
}