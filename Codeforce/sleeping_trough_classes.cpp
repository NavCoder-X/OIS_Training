#include <iostream>
#include <string>
// #include <fstream>

using namespace std;

int main(){
    // ifstream cin("input.txt");
    // ofstream cout("output.txt");
    int TESTS;
    int n, k;
    int c = 0;
    int sleeping = 0;

    cin >> TESTS;

    for (int i = 0; i < TESTS; i++)
    {
        string s;
        cin >> n >> k;
        cin >> s;
        for (int j = 0; j < n; j++)
        {
            if(s[j] == '1'){
                sleeping = k;
                continue;
            }
            if(sleeping-- > 0) continue;
            c++;
        }

        cout << c << endl;
        c = 0;
        sleeping = 0;
    }
    



    return 0;
}
