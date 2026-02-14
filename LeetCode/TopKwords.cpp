#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

vector<string> topKFrequent(vector<string>& words, int k) {
    unordered_map<string,int> m;
    vector<pair<string,int>> v;
    vector<string> ris;
    for (auto &s: words){
        m[s]++;
    }

    for (auto &n: m){
        v.push_back(n);
    }

    sort(v.begin(),v.end(),[](const pair<string,int> &a,const pair<string,int> &b){
        if(a.second == b.second) return a < b;
        return a.second > b.second;
    });

    for (int i = 0; k && i < v.size(); i++)
    {
        k--;
        ris.push_back(v[i].first);
    }
    
    return ris;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, k;
    cin >> n >> k;

    vector<string> words(n);
    for(int i = 0;i < n;i++){
        cin >> words[i];
    }
    auto ris = topKFrequent(words,k);
    for (auto n: ris){
        cout << n << endl;
    }
    return 0;
}