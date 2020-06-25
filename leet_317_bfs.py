#!/usr/bin/python

'''
Leetcode #317 using BFS (Anything shortest on a graph always use BFS)

Shortest distance from all buildings

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

'''
import math 

def bfs(grid, r, c, reach, dist ):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    q = []
    q.append((r,c))
    
    visited[r][c] = True
    
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    count = 0
    while q:
        qlen = len(q)
        count += 1

        for _ in range(qlen):
            row, col = q.pop(0)
            
            for i in range(4):
                nrow = row + dr[i]
                ncol = col + dc[i]

                if nrow < 0 or nrow >= len(grid) or ncol < 0 or ncol >= len(grid[0]) or visited[nrow][ncol]:
                    continue

                if grid[nrow][ncol] == 0:
                    visited[nrow][ncol] = True # important to mark the neighbors has visited right before you add them to queue (or else it will count duplicates)
                    reach[nrow][ncol] += 1
                    dist[nrow][ncol] += count
                    q.append((nrow,ncol))


def getMinimumDistance(grid):
    R = len(grid)
    C = len(grid[0])

    reach = [ [0 for _ in range(C)] for _ in range(R)] # keeps track of number of buildings reachable from the cell
    dist  = [ [0 for _ in range(C)] for _ in range(R)] # keeps track of total distance from this cell to all reachable buildings

    totalBuildings = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                totalBuildings += 1
                bfs(grid, r, c, reach, dist)

    min_distance = math.inf
    for r in range(R):
        for c in range(C):
            if reach[r][c] == totalBuildings and dist[r][c] < min_distance:
                min_distance = dist[r][c]
    
    return min_distance if min_distance != math.inf else -1

def main():
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    print("Minimum distance: ", getMinimumDistance(grid))




if __name__ == "__main__":
    main()

