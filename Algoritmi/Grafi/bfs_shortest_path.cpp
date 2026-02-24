#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <fstream>
using namespace std;
 
void load(map<string,map<string,int>>& ldj, bool pesato = false, bool orientato = false){
    ifstream f("output.txt");
    string a, b, peso;
    while (f >> a >> b >> peso)
    {
        int iPeso = stoi(peso);
        if(!pesato) iPeso = 0;
        ldj[a][b] = iPeso;
        if(!orientato) ldj[b][a] = iPeso;
    }
    
}

template <typename T>
void bfs(map<T,map<T,int>> &ldj,T nodo,string Target){
    queue<T> q;
    set<T> seen;
    q.push(nodo);
    while (!q.empty())
    {
        T n = q.front(); q.pop(); seen.insert(n);
        cout << n << " ";
        if(n == Target) break;

        for (auto vicino: ldj[n]){
            if(!seen.count(vicino.first)){
                q.push(vicino.first);
                seen.insert(vicino.first);
            } 
        }
    }

    while (!q.empty())
    {
        cout << q.front() << endl;
        q.pop();
    }
    
}

int main() {
    map<string,map<string,int>> ldj;
    load(ldj);
    string start = "1-1", target = "14-14";
    bfs(ldj,start,target);
    return 0;
}