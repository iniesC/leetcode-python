#!/usr/bin/python

'''
Leetcode #1254 (using DFS 2 -pass)

Number of Closed Islands:

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
'''

def dfs(grid, r, c):
    R = len(grid)
    C = len(grid[0])

    if r < 0 or r >= R or c < 0 or c >= C:
        return

    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    grid[r][c] = 1

    for i in range(4):
        nrow = r + dr[i]
        ncol = c + dc[i]

        if nrow < 0 or nrow >= R or ncol < 0 or ncol >= C: 
            continue
   
        if grid[nrow][ncol] == 0:
            dfs(grid,nrow,ncol)
            

def countClosedIslands(grid):
    R = len(grid)
    C = len(grid[0])
    count = 0

    # 1st pass - to elminate border zeros or fake islands (fill them with 1s)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i == 0 or i == R-1 or j == 0 or j == C-1) and grid[i][j] == 0:
                dfs(grid, i,j)

    # 2nd pass - the actual count of close islands
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                dfs(grid, i,j)
                count = count + 1 
    
    return count

def main():

    #test 1
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]

    print("Number of closed Islands: " , countClosedIslands(grid))

    #test 2
    grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]

    print("Number of closed Islands: " , countClosedIslands(grid))

    grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]

    print("Number of closed Islands: " , countClosedIslands(grid))

if __name__ == "__main__":
    main()
