#include <iostream>
#include <set>
#include <map>
#include <queue>
#include "mat.hpp"

using namespace std;
enum Cell { WALL, EMPTY, STEP, TARGET };

void stampaPercorso(map<pair<int,int>,pair<int,int>> &visitati,pair<int,int> &end,Mat<int> &maze){
    vector<int> path;
    pair<int,int> null = make_pair(-1,-1);
    auto current = end;
    while (current != null)
    {
        maze[current.first][current.second] = STEP;
        cout << current.first << "-" << current.second << endl;
        current = visitati[current];
    }
}

void solve(Mat<int> &maze,pair<int,int> start){
    // inizializzo
    int max_row = maze.rows, max_col = maze.cols;
    map<pair<int,int>,pair<int,int>> visitati;
    queue<pair<int,int>> q;
    vector<pair<int,int>> direzioni = {{0,1},{0,-1},{1,0},{-1,0}};
    q.push(start); visitati[start] = {-1,-1};

    // bfs
    while (!q.empty())
    {
        auto node = q.front(); q.pop();

        // se e la cella target finisco e stampo il percorso
        if(maze[node.first][node.second] == TARGET){
            stampaPercorso(visitati,node,maze);
            return;
        }

        // per ogni vicino controllo se e una cella vuota e la metto in q e visitati
        for (auto &d: direzioni){
            int ni = node.first + d.first, nj = node.second + d.second;
            if(ni >= 0 && ni < max_row && nj >= 0 && nj < max_col && maze[ni][nj] != WALL){
                auto newNode = make_pair(ni,nj);
                if(visitati.find(newNode) == visitati.end()){
                    visitati[newNode] = node;
                    q.push(newNode);
                }
            }
        }
    }
    
}

int main() {
    auto maze = Mat<int>::load("input1.txt");
    cout << maze;

    unsigned start_row = 0, start_col = 0;
    maze.find(Cell::STEP, &start_row, &start_col);

    maze[start_row][start_col] = Cell::EMPTY;
    solve(maze,make_pair(start_row,start_col));
    cout << endl << maze;
    return 0;
}