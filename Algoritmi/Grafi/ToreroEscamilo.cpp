#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <unordered_map>
#include <unordered_set>
using namespace std;

unordered_set<int> visitati;
void dfs(unordered_map<int,unordered_set<int>> &dipendenze,int nodo){
    visitati.insert(nodo);
    for (auto n: dipendenze[nodo]){
        if(!visitati.count(n)) dfs(dipendenze,n);
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, m, q; cin >> n >> m >> q;
    unordered_map<int,unordered_set<int>> dipendenze;
    for (size_t i = 0; i < m; i++)
    {
        int a, b; cin >> a >> b;
        dipendenze[a].insert(b);
    }

    dfs(dipendenze,q);
    cout << n - visitati.size();
    
    return 0;
}