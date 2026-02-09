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
    cin >> s;

    transform(s.begin(),s.begin()+1,s.begin(),[](unsigned char c){
        return toupper(c);
    });

    cout << s;
    return 0;
}