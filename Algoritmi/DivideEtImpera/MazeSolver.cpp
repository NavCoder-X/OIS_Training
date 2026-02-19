#include <iostream>
#include <set>
#include "mat.hpp"

using namespace std;

set<pair<int,int>> seen;

enum Cell { WALL, EMPTY, STEP, TARGET };

bool solve(Mat<int> &maze,int i,int j){
    if(i >= maze.rows || i < 0 || j >= maze.cols || j < 0 || maze[i][j] == WALL || maze[i][j] == STEP || seen.count(make_pair(i,j)))
        return false;
    else if(maze[i][j] != EMPTY)
        return maze[i][j] == TARGET;

    maze[i][j] = STEP;
    seen.insert(make_pair(i,j));
    if(solve(maze,i+1,j) || solve(maze,i-1,j) || solve(maze,i,j+1) || solve(maze,i,j-1))
        return true;

    maze[i][j] = EMPTY;
    return false;
}

int main() {
    auto maze = Mat<int>::load("input1.txt");
    cout << maze;

    unsigned start_row = 0, start_col = 0;
    maze.find(Cell::STEP, &start_row, &start_col);

    maze[start_row][start_col] = Cell::EMPTY;
    solve(maze, start_row, start_col);
    cout << endl << maze;
    return 0;
}