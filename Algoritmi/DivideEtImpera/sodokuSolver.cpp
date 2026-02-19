#include <iostream>
#include "mat.hpp"

using namespace std;

bool isValid(Mat<int> &sodoku,int i,int j,int num){
    for (int k = 0; k < sodoku.rows; k++)
        if(sodoku[i][k] == num) return false;
        
    for (int l = 0; l < sodoku.rows; l++)
        if(sodoku[l][j] == num) return false;

    int iQuadrante = i - (i%3);
    int jQuadrante = j - (j%3);
    for (int k = 0; k < 3; k++)
        for (int l = 0; l < 3; l++)
            if(sodoku[iQuadrante+k][jQuadrante+l] == num) return false;
    
    return true;
}

bool solve(Mat<int> &sodoku){
    for (int i = 0; i < sodoku.rows; i++)
    {
        for (int j = 0; j < sodoku.cols; j++)
        {
            if(sodoku[i][j] == 0){
                for (int k = 1; k <= 9; k++)
                {
                    if(isValid(sodoku, i, j, k)){
                        sodoku[i][j] = k;
                        if(solve(sodoku)) return true;  
                        sodoku[i][j] = 0;  // Backtrack
                    }
                }
                return false;  
            }
        }
    }
    return true;  
}

int main() {
    auto maze = Mat<int>::load("input4.txt");
    cout << maze << endl;

    if(solve(maze)){
        cout << endl << "Solution:" << endl << maze;
    } else {
        cout << endl << "No solution found!" << endl;
    }
    return 0;
}