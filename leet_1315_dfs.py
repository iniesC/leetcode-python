
'''
Sum of Nodes with Even-Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.
'''

class Node:
   def __init__(self, value) -> None:
      self.val = value
      self.left = None
      self.right = None



def dfs(node, parent, grandparent):
   if not node:
      return 0
   
   sum = 0

   if grandparent and grandparent.val % 2 == 0:
      sum += node.val
   
   sum += dfs(node.left, node, parent) + dfs(node.right, node, parent)

   return sum


def main():
   root = Node(6)
   root.left = Node(7)
   root.right = Node(8)

   root.left.left = Node(2)
   root.left.right = Node(7)
   root.right.left = Node(1)
   root.right.right = Node(3)

   root.left.left.left = Node(9)
   root.left.right.left = Node(1)
   root.left.right.right = Node(4)

   root.right.right.right = Node(5)

   print("sum of nodes with even grand parents: ", dfs(root, None, None))


if __name__ == "__main__":
   main()

