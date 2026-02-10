#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    map<string,int> db;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string s;
        cin >> s;

        // se il nome e gia nel data base o non esiste
        if(db.find(s) == db.end()){
            db[s]++;
            cout << "OK" << endl;
        }else{
            cout << s << to_string(db[s]) << endl;
            db[s]++;
        }
    }
    
    return 0;
}