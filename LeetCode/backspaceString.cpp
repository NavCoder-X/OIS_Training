#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

bool backspaceCompare(string s, string t) {
    stack<char> sx, tx;

    for (auto c: s){
        if(c == '#' && !sx.empty()) sx.pop();
        else if(c != '#') sx.push(c);
    }
    for (auto c: t){
        if(c == '#' && !tx.empty()) tx.pop();
        else if(c != '#') tx.push(c);
    }
    
    if(sx.size() != tx.size()) return 0;
    while (!sx.empty())
    {
        if(sx.top() != tx.top()) return 0;
        sx.pop(); tx.pop();
    }
    
    return 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    string s, t;
    cin >> s >> t;

    auto ris = backspaceCompare(s,t);
    cout << ris;
    return 0;
}