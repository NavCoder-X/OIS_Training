#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

// O(n x w) s(n*2)
ll knapscak_0_1(vector<pll> & oggetti, ll w, ll n){
    // look up table che considera le ultime due righe della tabella 
    // tabella del tipo lut[i][w] dove i e il numero del ogetto che teniamo in cosiderazione e w la capacita 
    // in ogni cella mettiamo il massimo ottenibile fino a quel momento
    // se non consideriamo nessun elemento allora sara tutto 0
    vector<vector<ll>> lut(2);
    lut[0].resize(w+1,0); // cella inziale per portata 0
    lut[1].resize(w+1);

    for (int i = 0; i < n; i++)
    {
        // riempio celle in cui non posso mettere l ogetto perche troppo pesante
        for (int j = 0; j < oggetti[i].first; j++)
            lut[1][j] = lut[0][j];
        
        // vedo se con portata j e meglio la soluzione di prima senza includere o includendo
        for (int j = oggetti[i].first; j < w+1; j++)
            lut[1][j] = max(lut[0][j],lut[0][j-oggetti[i].first]+oggetti[i].second);
        
        swap(lut[0],lut[1]);
    }
    
    return lut[0][w];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    ll n, w;
    cin >> n >> w;

    vector<pll> ogettti(n);
    for(int i = 0;i < n;i++){
        ll p, c; cin >> p >> c;
        ogettti[i] = make_pair(p,c);
    }

    auto ris = knapscak_0_1(ogettti,w,n);
    cout << ris << endl;
    return 0;
}