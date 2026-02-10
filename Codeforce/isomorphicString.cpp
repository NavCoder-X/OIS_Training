#include <iostream>
#include <vector>
#include <map>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

bool isIsomorphic(string s, string t) {
    if(s.size() != t.size()) return false;
    map<char,char> m1;
    map<char,char> m2;

    for (int i = 0; i < s.size(); i++)
    {
        if(m1.find(s[i]) != m1.end()){
            if(m1[s[i]] != t[i]) return false;
        }else{
            m1[s[i]] = t[i];
        }
        if(m2.find(t[i]) != m2.end()){
            if(m2[t[i]] != s[i]) return false;
        }else{
            m2[t[i]] = s[i];
        }
    }

    return true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    string s, t;
    cin >> s >> t;
    auto ris = isIsomorphic(s,t);

    cout << ris << endl;
    return 0;
}