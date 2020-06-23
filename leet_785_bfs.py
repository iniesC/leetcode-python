#!/usr/bin/python

'''
Leetcode #785 - using BFS

Is Graph Bi-partite?

 Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

'''
def bfs(starting_node, adjList, colors):
    starting_color = 0

    q = []
    q.append(starting_node)
    colors[starting_node] = starting_color
    while q:
        current_node = q.pop(0)
        # flip the color for next the neighbors
        next_color = 1 - colors[current_node]

        for neighbor in adjList[current_node]:
            if neighbor not in colors:
                colors[neighbor] = next_color
                q.append(neighbor)
            else:
                if colors[neighbor] == colors[current_node]: # if neighbors have the same color then it cannot be bipartite
                    return False    

    return True

def isBipartite(L): 
    #building the braph ir adjacency list
    adjList = {}
    for src,dests in enumerate(L):
        adjList[src] = dests

    colors = {}
    for node in adjList: # we have to go through all unvisited nodes to check for bipartite
        if node not in colors:
            if not bfs(node, adjList, colors):
                return False

    return True 

    

#driver code
def main():
    #test 1
    L = [[1,3], [0,2], [1,3], [0,2]]
    print(isBipartite(L))

    #test 2
    L = [[1,2,3], [0,2], [0,1,3], [0,2]]
    print(isBipartite(L))

    #test 3:
    L = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    print(isBipartite(L))

    #test 4
    L = [[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]
    print(isBipartite(L))
    
if __name__ == "__main__":
    main()
