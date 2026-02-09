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
 
    string s, ris = "";
    cin >> s;

    int numbers[4] = {0};
    for (auto c: s){
        if(c == '1') numbers[1]++;
        else if(c == '2') numbers[2]++;
        else if(c == '3') numbers[3]++;
    }

    for (int i = 1; i < 4; i++)
    {
        while(numbers[i]--){
            ris += to_string(i)+"+";
        }
    }

    ris.pop_back();
    cout << ris << endl;
    
    return 0;
}