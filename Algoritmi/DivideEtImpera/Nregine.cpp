#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// costanti
#define REGINA 1
#define EMPTY 0
#define N 4

vector<vector<int>> soluzioni;
vector<int> soluzioneAttuale(N,-1);

void printScacchiera(vector<vector<int>> &scacchiera,vector<int> &soluzione){
    // metto nella scacchiera la soluzione
    for (int i = 0; i < soluzione.size(); i++)
        if(soluzione[i] != -1) scacchiera[i][soluzione[i]] = REGINA;
    
    for (int i = 0; i < scacchiera.size(); i++)
    {
        for (int j = 0; j < scacchiera.size(); j++)
            cout << scacchiera[i][j] << " ";
        cout << endl;
    }
    cout << endl;

    // svuoto la scacchiera
    for (int i = 0; i < soluzione.size(); i++)
        if(soluzione[i] != -1) scacchiera[i][soluzione[i]] = EMPTY;
}

bool SottoAtacco(vector<vector<int>> &scacchiera,int i,int j){
    int k, l;
    
    // controllo della colonna
    for (k = 0; k < i; k++)
        if(scacchiera[k][j] == REGINA) return true;

    // controllo sotto diagonale principale
    for (k = i-1, l = j-1; k >= 0 && l >= 0; k--, l--)
        if(scacchiera[k][l] == REGINA) return true;
    
    // controllo diagonale secondaria
    for (k = i-1, l = j+1; k >= 0 && l < scacchiera.size(); k--, l++)
        if(scacchiera[k][l] == REGINA) return true;
    
    return false;
}

void posizioneRegina(vector<vector<int>> &scacchiera,int n,int rigaFinale){
    if (n == rigaFinale){
        soluzioni.push_back(soluzioneAttuale);
        return;
    }

    for (int j = 0; j < scacchiera.size(); j++)
    {
        if(!SottoAtacco(scacchiera,n,j)){
            scacchiera[n][j] = REGINA;
            soluzioneAttuale[n] = j;
            posizioneRegina(scacchiera,n+1,rigaFinale);
            soluzioneAttuale[n] = -1;
            scacchiera[n][j] = EMPTY;
        }
    }
    
    return;
}

void posizioneRegineN(vector<vector<int>> &scacchiera,int n){
    if(n == 0){
        soluzioni.push_back(soluzioneAttuale);
        return;
    }else if(n > scacchiera.size()){
        cout << "Errore: n deve essere minore o uguale alla dimensione della scacchiera." << endl;
        return;
    }

    for (int i = 0; i < scacchiera.size()-n+1; i++)
    {
        posizioneRegina(scacchiera, i, i+n);
    }
    
}

int main() {
    // inizializzo la scacchiera
    vector<vector<int>> scacchiera;
    for (int i = 0; i < N; i++)
    {
        vector<int> v(N, EMPTY);
        scacchiera.push_back(v);
    }

    posizioneRegineN(scacchiera,N);
    for (auto v: soluzioni){
        printScacchiera(scacchiera,v);
    }
    cout << "Soluzioni trovate: " << soluzioni.size() << endl;
    
    return 0;
}