#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

string removeOuterParentheses(string s) {
    if(s.size() <= 1) return "";
    string ris = "";
    stack<char> parentesi;

    for(auto p: s){
        if(p == '('){
            if(!parentesi.empty()) ris += p;
            parentesi.push(p);
        }else{
            parentesi.pop();
            if(!parentesi.empty()) ris += p;
        }
    }

    return ris;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    string s;
    cin >> s;
    auto ris = removeOuterParentheses(s);
    cout << ris;

    return 0;
}