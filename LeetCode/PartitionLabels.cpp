#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <string>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

vector<int> partitionLabels(string s) {
    map<char,int> counter;
    set<char> currents;
    vector<int> ris;
    int c = 0, last = -1;

    // conto frequenze O(n)
    for (auto c: s) counter[c]++;

    // inizializzo la prima partizione
    c = counter[s[0]]; currents.insert(s[0]);
    for (size_t i = 0; i < s.size(); i++)
    {
        if(!currents.count(s[i])){
            c += counter[s[i]];
            currents.insert(s[i]);
        }
        int dim = i - last;
        if(dim == c){
            currents.clear();
            ris.push_back(c);
            last = i;
            if(i < s.size()-1){
                c = counter[s[i+1]];
                currents.insert(s[i+1]);
            }
        }
    }

    return ris;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    string s; cin >> s;

    auto ris = partitionLabels(s);
    for (auto n: ris){
        cout << n << ' ';
    }
    return 0;
}