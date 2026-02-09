#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    unordered_set<char> chars;
    string s;
    cin >> s;

    for (auto c: s){
        chars.insert(c);
    }

    if(chars.size() & 1) cout << "IGNORE HIM!";
    else cout << "CHAT WITH HER!";

    return 0;
}