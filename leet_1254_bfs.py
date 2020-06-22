#!/usr/bin/python

'''
Leetcode #1254 (using BFS)

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

def bfs(grid, r, c):
    R = len(grid)
    C = len(grid[0])

    status = True
    if r < 0 or r >= R or c < 0 or c >= C:
        return False

    dr = [1,0,-1,0]
    dc = [0,1,0,-1]

    q = []
    q.append((r,c))


    while q:

        row , col = q.pop(0)
        grid[row][col] = 1

        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]

            if nrow < 0 or nrow >= R or ncol < 0 or ncol >= C:  # if any of the neighbor is out of bounds we dont count that set of cells
                status = False
                continue

            
            if grid[nrow][ncol] == 0:
                q.append((nrow,ncol))
    
    return status
            




def countClosedIslands(grid):

    count = 0
    status = False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                status = bfs(grid, i,j)
                count = count + 1 if status else count
    
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
