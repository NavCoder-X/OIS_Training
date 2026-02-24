#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <fstream>
using namespace std;



template <typename T>
void salva(map<T,map<T,int>> &ldj){
    ofstream f("output.txt");
    for (auto &n: ldj){
        for (auto &x: n.second){
            f << n.first << " " << x.first << " " << x.second << " " << endl;
        }
    } 
}

template <typename T>
void stampa(map<T,map<T,int>> &ldj){
    cout << "---------------------------------------------------------------" << endl;
    for (auto &n: ldj){
        for (auto &x: n.second){
            cout << n.first << " " << x.first << " " << x.second << " " << endl;
        }
    }   
}
 
template <typename T>
void dfs(map<T,map<T,int>> &ldj,T nodo){
    stack<T> s;
    set<T> seen;
    s.push(nodo);
    while (!s.empty())
    {
        // prendo nodo top e segno visto 
        T n = s.top(); s.pop(); seen.insert(n);
        // cout << n << " ";

        // aggiungo vicini 
        for (auto vicino: ldj[n]){
            if(!seen.count(vicino.first)){
                s.push(vicino.first);
                seen.insert(vicino.first);
            } 
        }
    }
}

template <typename T>
void bfs(map<T,map<T,int>> &ldj,T nodo){
    queue<T> q;
    set<T> seen;
    q.push(nodo);
    while (!q.empty())
    {
        T n = q.front(); q.pop(); seen.insert(n);
        // cout << n << " ";

        for (auto vicino: ldj[n]){
            if(!seen.count(vicino.first)){
                q.push(vicino.first);
                seen.insert(vicino.first);
            } 
        }
    }
}

int main() {
    map<char,map<char,int>> ldj;
    cout << "inserisci una lista di adiacenza: (archi) ";
    int n; cin >> n;

    for (int i = 0; i < n; i++)
    {
        char a, b;
        int peso;
        cout << "a->b peso : ";
        cin >> a >> b >> peso;
        ldj[a][b] = peso;
        // ldj[b][a] = peso;
    }

    // string x = "a";
    // bfs(ldj,x);
    salva((ldj));
    return 0;
}