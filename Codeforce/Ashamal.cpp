#include <iostream>
#include <string>
#include <vector>
using namespace std;

// aproccio gready, provo entrambe le combinazioni e scelgo la migliore. visto che i contraints sono piccoli
string solve(vector<string> & stringhe){
    if(stringhe.size() <= 1) return stringhe[0];
    string temp;
    string sol = stringhe[0];
    for (int i = 1; i < stringhe.size(); i++)
    {
        temp = sol;
        sol += stringhe[i];
        temp = stringhe[i] + temp;
        if(temp < sol){
            sol = temp;
        }
    }
    
    return sol;
}
 
int main() {
    int t;
    cin >> t;
    
    // per ogni test
    for (int i = 0; i < t; i++)
    {
        // leggo le stringhe
        int n;
        vector<string> stringhe;
        cin >> n;
        for(int j = 0;j < n;j++) {
            string s;
            cin >> s;
            stringhe.push_back(s);
        }

        // soluzione
        auto sol = solve(stringhe);
        cout << sol << endl;
    }
    
    return 0;
}