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
 
    string s1, s2;
    cin >> s1 >> s2;

    transform(s1.begin(),s1.end(),s1.begin(),[](unsigned char c){return tolower(c);});
    transform(s2.begin(),s2.end(),s2.begin(),[](unsigned char c){return tolower(c);});

    if(s1 == s2) cout << 0;
    else if(s1 < s2) cout << -1;
    else cout << 1;
    
    return 0;
}