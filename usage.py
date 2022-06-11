"""
here are some examples of binary search tree usage.
"""

from binarysearchtree import BinarySearchTree

tree = BinarySearchTree(7)
root = tree.get_root()
tree.add(5, root)
tree.add(6, root)
tree.add(9, root)
tree.add(10, root)
tree.add(1, root)
tree.add(8, root)
tree.add(11, root)
tree.add(12, root)
tree.add(12, root)
print(tree)
print(tree.bfs())
print(tree.get_leaves())
print(tree.path_to_element(6))
print(tree.nodes_num())
print(tree._is_leaf(11))
print(tree._is_leaf(12))
root = tree.get_root(data=True)
print(tree.inorder(root))
print(tree.preorder(root))
print(tree.postorder(root))
