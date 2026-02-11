#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

bool canConstruct(string &note, string &magazzino){
    if(note.size() > magazzino.size()) return 0;
    map<char,int> m;

    for (auto c: magazzino){
        m[c]++;
    }

    for (auto c: note){
        if(m[c] <= 0) return 0;
        m[c]--;
    }

    return 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    string note, magazzino;
    cin >> note >> magazzino;

    auto ris = canConstruct(note,magazzino);
    cout << ris;
    return 0;
}