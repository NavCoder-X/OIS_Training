#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

bool isValid(string s) {
    if(s.size() <= 1) return false;
    map<char,char> m;
    m[')'] = '(';
    m[']'] = '[';
    m['}'] = '{';
    stack<char> parentesi;

    for (auto p: s){
        if(m.find(p) == m.end()) parentesi.push(p);
        else{
            if(!parentesi.empty() && parentesi.top() == m[p]) parentesi.pop();
            else return false;
        }
    }

    return parentesi.empty();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    string s;
    cin >> s;
    auto ris = isValid(s);

    cout << ris;
    return 0;
}