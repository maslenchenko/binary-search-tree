"""
binary search tree implementation.

----------------------------------
*           june 2022            *
*    developed by maslenchenko   *
*          with love XX          *
----------------------------------
"""

class TreeNode:
    """
    representation of a binary search\
    tree node.

    attributes:
    -----------
    data: any data type
        data which node contains

    right: TreeNode object
        right child of a node

    left: TreeNode object
        left child of a node
    """
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    """
    representation of a binary search tree.

    methods:
    --------
    get_root(self):
        returns a root of\
        the binary search tree.

    add(self, element, start_point):
        adds element to the binary\
        search tree.

    get_leaves(self):
        returns a list of leaves.

    _children(self, node):
        returns a list of children\
        (TreeNode) objects for specific\
        tree node.

    bfs(self):
        breadth first search function.
        returns a list which consists of\
        list of node levels. 
        if tree node is none, it is marked\
        as '_'.

    path_to_element(self):
        returns a path (a list of\
        elements) to the specific node.

    _up(self):
        returns a father of a node.

    inorder(self):
        traverse from the left subtree to\
        the root then to the right subtree.

    nodes_num(self):
        total number of nodes in\
        binary search tree.

    _is_leaf(self, value):
        checks if tree node is leaf.

    attributes:
    -----------
    _root: TreeNode object
        binary search tree root
    """
    def __init__(self, root=None):
        """
        constructs all necessary attributes\
        for BinarySearchTree object.

        attributes:
        -----------
        _root: TreeNode object
            binary search tree root
        """
        self._root = TreeNode(root)
        self.nodes = 0
        if self._root is not None:
            self.nodes = 1

    def get_root(self):
        """
        returns a root of\
        the binary search tree.
        """
        return self._root

    def add(self, element, start_point):
        """
        adds element to the binary\
        search tree.
        """
        if start_point is None:
            start_point = TreeNode(element)
            self.nodes += 1
        else:
            if start_point.data > element:
                if start_point.left is None:
                    start_point.left = TreeNode(element)
                    self.nodes += 1
                else:
                    self.add(element, start_point.left)
            elif start_point.data < element:
                if start_point.right is None:
                    start_point.right = TreeNode(element)
                    self.nodes += 1
                else:
                    self.add(element, start_point.right)
            else:
                return "this element already exists in binary search tree"

    def get_leaves(self):
        """
        returns a list of leaves.
        """
        levels = self.bfs()
        leaves = levels[-1]
        for element in leaves[::-1]:
            if element == "_":
                leaves.remove(element)
        return leaves

    def path_to_element(self, value):
        """
        returns a path (a list of\
        elements) to the specific node.
        """
        levels = self.bfs(object=True)
        node = None
        for level in levels:
            for element in level:
                if isinstance(element, TreeNode):
                    if element.data == value:
                        node = element
        if node is not None:
            path = [value]
            while self._up(node) is not None:
                path.append(self._up(node).data)
                node = self._up(node)
            if len(path) > 0:
                return path
            else:
                return "element does not exist"

    def _up(self, node):
        """
        returns a father of a node.
        """
        levels = self.bfs(object=True)
        level = -1
        for ind in range(len(levels)):
            for element in levels[ind]:
                if isinstance(element, TreeNode):
                    if element.data == node.data:
                        level = ind
        if level != -1:
            father_level = level - 1
            if father_level == -1:
                return None
            for element in levels[father_level]:
                if element != "_":
                    if node.data in self._children(element, data=True):
                        return element
        else:
            return None

    def _children(self, node, data=False):
        """
        returns a list of children\
        (TreeNode) objects for specific\
        tree node.
        """
        children = []
        if data is False:
            if node.left is not None:
                children.append(node.left)
            else:
                children.append("_")
            if node.right is not None:
                children.append(node.right)
            else:
                children.append("_")
        else:
            if node.left is not None:
                children.append(node.left.data)
            else:
                children.append("_")
            if node.right is not None:
                children.append(node.right.data)
            else:
                children.append("_")
        return children

    def bfs(self, object=False):
        """
        breadth first search function.
        returns a list which consists of\
        list of node levels. 
        if tree node is none, it is marked\
        as '_'.
        """
        levels = []
        level = [self._root]
        while level.count("_") != len(level):
            next_level = []
            for element in level:
                if element != "_":
                    next_level.extend(self._children(element))
                else:
                    next_level.extend(["_", "_"])
            levels.append(level)
            level = next_level
        if object is False:
            for element in levels:
                for ind in range(len(element)):
                    node = element[ind]
                    try:
                        element[ind] = node.data
                    except:
                        pass
        return levels

    def __str__(self):
        """
        returns string representation\
        of binary search tree.
        """
        levels = self.bfs()
        max_len = len(levels[-1]) * 2 - 1
        result = ""
        for level in levels:
            length = len(level)
            if length == 1:
                result += "_ " * int(((max_len - 1)/2))
                result += f"{level[0]}"
                result += "_ " * int(((max_len - 1)/2))
                result += "\n"
            else:
                result += "_ " * int(((max_len - len(level))/2))
                sub_str = ""
                for el in level:
                    sub_str += f"{el} _ "
                sub_str = sub_str[:-2]
                result += sub_str
                result += "_ " * int(((max_len - len(level))/2))
                result += "\n"
        return result[:-1]
        
    def inorder(self):
        """
        traverse from the left subtree to\
        the root then to the right subtree.
        """
        marked = []
        inorder = []
        to_discover = []
        nodes_num = self.nodes_num()
        current = self._root
        while len(inorder) != nodes_num:
            to_discover.extend(self._children())
            to_discover = 

    def nodes_num(self):
        """
        total number of nodes in\
        binary search tree.
        """
        return self.nodes

    def _is_leaf(self, value):
        """
        checks if tree node is leaf.
        """
        levels = self.bfs(object=True)
        for level in levels:
            for node in level:
                if node != "_":
                    if node.data == value:
                        tree_node = node
        if tree_node:
            return tree_node.left is None and tree_node.right is None
        else:
            return None

    @staticmethod
    def _remove_empty_nodes(list):
        for element in list[::-1]:
            if element == "_":
                list.remove(element)
        return list
