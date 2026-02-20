#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

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
    for (const auto &x : v) { _print(x); dbg << " "; }
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

#define debug(x) dbg << " | " << #x << " = ", _print(x);
#define debugln(x) dbg << " | " << #x << " = ", _print(x), dbg << '\n';
#define debug_endl dbg << '\n';
#define debug2(x,y) dbg << #x << "," << #y << " = ", _print(x), dbg << " | ", _print(y), dbg << '\n';
#else
#define debug(x)
#define debugln(x)
#define debug_endl
#define debug2(x,y)
#endif
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    // Test variabili semplici sulla stessa riga
    int a = 10, b = 20, c = 30;
    debug(a); debug(b); debug(c); debug_endl;
    
    // Test vector
    vi nums = {1, 2, 3, 4, 5};
    debugln(nums);
    
    // Test string
    string s = "ciao";
    debugln(s);
    
    // Test pair
    pi p = {100, 200};
    debugln(p);
    
    // Test set
    set<int> st = {5, 3, 8, 1};
    debugln(st);
    
    // Test map
    map<int, string> mp;
    mp[1] = "uno";
    mp[2] = "due";
    mp[3] = "tre";
    debugln(mp);
    
    // Test multiplo: vector e set sulla stessa riga
    vi v2 = {10, 20};
    set<int> s2 = {100, 200};
    debug(v2); debug(s2); debug_endl;
    
    // Test vector di pair
    vector<pi> vp = {{1,2}, {3,4}, {5,6}};
    debugln(vp);

    debug_endl;
    debug_endl;
    debug_endl;
    debug_endl;
    debug_endl;
    debug_endl;

    debug(vp);
    debug(vp);



    return 0;
}