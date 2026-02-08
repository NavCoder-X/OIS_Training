#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
 
typedef long long ll;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t;
    cin >> t;

    for(int i = 0;i < t;i++){
        string s;
        cin >> s;
        if(s.size() > 10){
            cout << s[0] << to_string(s.size()-2) << s.back() << endl;
        }else cout << s << endl;
    }
    return 0;
}