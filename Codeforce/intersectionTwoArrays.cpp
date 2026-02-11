#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    unordered_set<int> us;
    unordered_set<int> ris;
    vector<int> ris_v;

    for (auto n: nums1){
        us.insert(n);
    }
    for (auto n: nums2){
        if(us.find(n) != us.end()) ris.insert(n);
    }
    for (auto n: ris){
        ris_v.push_back(n);
    }

    return ris_v;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, m;
    cin >> n >> m;
    vi a1(n), a2(m);

    for (int i = 0; i < n; i++)
    {
        cin >> a1[i];
    }
    for (int i = 0; i < m; i++)
    {
        cin >> a2[i];
    }

    auto ris = intersection(a1,a2);
    for (auto n: ris){
        cout << n << ' ';
    }
    return 0;
}