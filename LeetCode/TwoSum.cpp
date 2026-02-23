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

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> answer(2);
    for (int i = 0; i < nums.size(); i++)
    {
        int l = i+1, r = nums.size()-1;
        int t = target - nums[i];
        debug2(l,r) debug_endl debug_endl
        while (l <= r)
        {
            int mid = l + (r-l)/2;
            debug(mid) debug_endl
            if(nums[mid] == t) return {i,mid};
            else if(nums[mid] > t) r = mid-1;
            else l = mid+1;
        }
    }
    
    return {-1,-1};
}

vector<int> twoSum(vector<int>& nums, int target){
    map<int,int> m;
    for (int i = 0; i < nums.size(); i++)
    {
        int t = target - nums[i];
        if(m.find(t) != m.end()) return {i,m[t]};
        m[nums[i]] = i;
    }
    
    return {-1,-1};
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, t;
    cin >> n >> t;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = twoSum(nums,t);
    cout << ris[0] << " " << ris[1] << endl;
    return 0;
}