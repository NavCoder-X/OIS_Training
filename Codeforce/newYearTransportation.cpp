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

#ifndef ONLINE_JUDGE
#include <fstream>
ofstream dbg("debug.txt");

template<typename T>
void _print(const T &x) { dbg << x; }

template<typename A, typename B>
void _print(const pair<A,B> &p) {
    dbg << "{";
    _print(p.first);
    dbg << ", ";
    _print(p.second);
    dbg << "}";
}

template<typename T>
void _print(const vector<T> &v) {
    dbg << "[ ";
    for (const auto &x : v) 
    { _print(x); dbg << " "; }
    dbg << "]";
}

template<typename T>
void _print(const set<T> &s) {
    dbg << "{ ";
    for (const auto &x : s) { _print(x); dbg << " "; }
    dbg << "}";
}

template<typename K, typename V>
void _print(const map<K,V> &m) {
    dbg << "{ ";
    for (auto &kv : m) { _print(kv); dbg << " "; }
    dbg << "}";
}

#define debug(x) dbg << #x << " = ", _print(x), dbg << '\n';
#define debug2(x,y) dbg << #x << "," << #y << " = ", _print(x), dbg << " | ", _print(y), dbg << '\n';
#else
#define debug(x)
#define debug2(x,y)
#endif

string solve(vi & portals, int t){
    int pos = 0;
    while (pos < t-1)
    {
        pos += portals[pos];
    }
    return (pos == t-1) ? "YES" : "NO";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, t;
    cin >> n >> t;

    vi portals(n);
    for(int i = 0;i < n-1;i++){
        cin >> portals[i];
    }
    portals[portals.size()-1] = 0;
    debug(portals);
    auto ris = solve(portals,t);
    cout << ris << endl;
    return 0;
}