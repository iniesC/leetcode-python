#!/usr/bin/python

'''
Leetcode #200 (solution using BFS)

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

def bfs(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]

    #check if current cell is within the grid boundary
    if r < 0 or r >= R or c < 0 or c >= C:
        return
    
    q = []
    q.append((r,c))

    while q:
        row, col = q.pop(0)

        grid[row][col] = 0   #reset the current cell to 0 to avoid re-examined

        for i in range(4):
            nrow = row + dr[i]
            ncol = col + dc[i]

            # check the neighbor is within grid boundary
            if nrow < 0 or nrow >= R or ncol < 0 or ncol >= C:
                continue

            if grid[nrow][ncol] == 1:
                q.append((nrow, ncol))


def countIslands(grid):
    R = len(grid)
    C = len(grid[0])

    count = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                count += 1
                bfs(grid,i,j)
    
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