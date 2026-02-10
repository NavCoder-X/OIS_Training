#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string s;
    int unos = 0, zeros = 0;
    bool dangerous = 0;
    cin >> s;

    // calcolo somma cumulativa di fila
    for (auto c: s){
        if(dangerous) break;
        if(c == '0'){
            unos = 0;
            zeros++;
            if(zeros >= 7) dangerous = 1;
        }
        if(c == '1'){
            zeros = 0;
            unos++;
            if(unos >= 7) dangerous = 1;
        }
    }

    if(dangerous) cout << "YES";
    else cout << "NO";
    
    return 0;
}