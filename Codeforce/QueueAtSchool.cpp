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
 
    int n, t;
    string s;
    cin >> n >> t;
    cin >> s;

    // Brute force
    for (int i = 0; i < t; i++)
    {
        for (int j = 0; j < n-1; j++)
        {
            if(s[j] == 'B' && s[j+1] == 'G') {
                swap(s[j],s[j+1]);
                j++;
            }
        }
    }
    
    cout << s;
    
    return 0;
}