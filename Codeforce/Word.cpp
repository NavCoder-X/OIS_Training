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
    int up = 0, low = 0;
    cin >> s;

    // conto le lettere , poi scelgo come trasformare
    for (auto c: s){
        if(c >= 'a' && c <= 'z') low++;
        else if(c >= 'A' && c <= 'Z') up++;
    }

    if(low >= up) transform(s.begin(),s.end(),s.begin(),[](unsigned char c){return tolower(c);});
    else transform(s.begin(),s.end(),s.begin(),[](unsigned char c){return toupper(c);});

    cout << s;
    return 0;
}