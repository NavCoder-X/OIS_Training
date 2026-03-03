#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
 
int main() {
    int m, n, k; cin >> m >> n >> k;
    map<char,map<int,int>> triplette;
    vector<char> sequenza(k);
    for (size_t i = 0; i < k; i++)
        cin >> sequenza[i];
    
    for (size_t i = 0; i < m; i++)
    {
        int a, b; cin >> a >> b;
        char c; cin >> c;
        triplette[c][a] = b;
    }

    int stato = 1;
    for (auto c: sequenza){
        stato = triplette[c][stato];
    }
    
    cout << stato;

    return 0;
}