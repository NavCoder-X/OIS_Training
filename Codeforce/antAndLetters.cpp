#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <sstream>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int count(string &s){
    if(s.size() == 0) return 0;
    set<string> letters;
    string x;
    stringstream ss(s);

    getline(ss,x,',');
    x = " " + x;
    letters.insert(x);
    while (getline(ss,x,','))
    {
        letters.insert(x);
    }
    
    return letters.size();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    string s;
    getline(cin,s,'\n');
    s = s.substr(1,s.size()-2);

    auto ris = count(s);
    cout << ris << endl;
    return 0;
}