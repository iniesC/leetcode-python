#!/usr/bin/python

'''
Leetcode #200 (solution using DFS)

Number of Islands:

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

def dfs(grid, r, c):
    R = len(grid)
    C = len(grid[0])

    if r < 0 or r >= R or c < 0 or c >= C:
        return
    
    #Move only horizontally or vertically
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]

    if grid[r][c] == 1:
        grid[r][c] = 0
        for i in range(4):
            dfs(grid, r+dr[i], c+dc[i])

def countIslands(grid):
    R = len(grid)
    C = len(grid[0])

    count = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                count += 1
                dfs(grid,i,j)
    
    return count

#Driver code
def main():
    #test 1
    grid = [[1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]
            ]
    
    print("Number of Island: ",countIslands(grid))

    #test 2
    grid = [[1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]
            ]
    
    print("Number of Island: ",countIslands(grid))

if __name__ == "__main__":
    main()