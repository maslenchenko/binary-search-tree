# Binary Search Tree
binary search tree implementation written in Python3
## What is it?
This is a basic binary search tree implementation. While creating a tree, the user should set a root. Before a new component is added, it is compared with every node of a tree and thus placed.
## How to install
To install binarysearchtree.py on your computer, open the terminal and write down <br />
```
pip install my-basic-bst==0.1
```
## What to use it for?
A binary search tree can help implement different searching algorithms and keep data structured and sorted.
## Methods
Here are methods that can be applied to this specific binary search tree: <br />
### 1. get_root() <br /> 
if the user wants to get data that the root stores, a data argument should be set to True.
### 2. add() <br /> 
this method takes two arguments: the first one is a data that a new node should store, and the second one is root as an object (you can find an example in usage.py). if second argument isn't mentioned or set to None, the root will be changed.
### 3. get_leaves() <br /> 
returns a list of leaves.
### 4. path_to_element() <br /> 
returns a path to any specified element.
### 5. bfs() <br /> 
breadth-first search, returns a list of lists, where each list is a tree-level (starts from the zero level - root).
### 6. nodes_num() <br />
returns total number of nodes.
### 7. inorder() <br /> 
inorder traversal.
### 8. preorder() <br /> 
preorder traversal.
### 9. postorder() <br /> 
postorder traversal.
### 10. delete_all_nodes() <br />
deletes all nodes and returns an empty tree.
### 11. delete_node() <br />
deletes specific node if it exists and rebalances existing tree.
### 12. rebalance() <br />
rebalances existing binary search tree.
