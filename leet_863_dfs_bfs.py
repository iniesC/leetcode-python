
'''
 All Nodes Distance K in Binary Tree

 We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  
The answer can be returned in any order.
'''
class Node:
   def __init__(self, value) -> None:
      self.val = value
      self.left = None
      self.right = None


def find_nodes_K_distance(root, target, K):
   
   def dfs(root, parent):
      if not root:
         return
      
      root.parent = parent  # Update node to contain parent

      if root.left:
         dfs(root.left, root)
      if root.right:
         dfs(root.right, root)
   
   dfs(root, None)

   q = []
   q.append((target, 0))
   seen = {target} #set
   while q:
      if q[0][1] == K:
         return [n.val for n,d in q]
      
      n, d = q.pop(0)

      for nei in [n.left, n.right, n.parent]:
         if nei and nei not in seen:
            q.append((nei, d+1))
            seen.add(nei)
   
   return []


def main():
   root = Node(3)
   target = root.left = Node(5)
   root.right = Node(1)

   root.left.left = Node(6)
   root.left.right = Node(2)
   root.right.left = Node(0)
   root.right.right = Node(8)

   root.left.right.left = Node(7)
   root.left.right.right = Node(4)

   print(find_nodes_K_distance(root, target, 2))

if __name__ == "__main__":
   main()

