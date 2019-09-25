"""
This module implements Binary Trees.

@author a.k
"""
import random

from data_structures.trees.utils import *


class BinaryTree:
    def __init__(self):
        self.root = None
        self.n = 0  # total nodes in the tree

    def insert(self, key, val=None):
        node = TreeNode(key, val)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)
        self.n += 1

    def _insert(self, root: TreeNode, node: TreeNode):
        """
        This helper inserts a node into a binary tree. Uses level-order traversal/bfs like algorithm to ensure balance.
        :param root: root of tree
        :param node: node to be inserted
        :return: none
        :Time: O(N)
        """
        # Initialise a queue and enqueue source node
        bfs_queue = Queue()
        bfs_queue.put(root)

        while not bfs_queue.empty():
            removed = bfs_queue.get()  # Dequeue from front

            # If removed node's left child is empty, insert there
            if removed.left is None:
                removed.left = node
                return
            else:  # If a left child exists, enqueue it to process it
                bfs_queue.put(removed.left)

            # Similarly for the right child
            if removed.right is None:
                removed.right = node
                return
            else:
                bfs_queue.put(removed.right)

    def get(self, key) -> TreeNode:
        ret_val = self._get(self.root, key)
        if ret_val is None:
            raise LookupError("Error! Key doesn't exist!")
        else:
            return ret_val

    def _get(self, root: TreeNode, key: TreeNode) -> TreeNode:
        """
        Helper get method that pre-order traverses tree to get the node associated with key
        :param root: root of tree
        :param key: key to look for
        :return: None if not found, the node, otherwise
        :Time: O(N)
        :Space: O(N)
        """
        # Always do the edge-case check, which could raise an error, FIRST!!
        if root is None:  # BC2 - not found
            return None
        # Pre-order traverse: examine root first, then recur left, then recur right
        if root.key == key:  # BC1 - found
            return root

        result_left_subtree = self._get(root.left, key)
        result_right_subtree = self._get(root.right, key)
        if result_left_subtree is not None:
            return result_left_subtree
        elif result_right_subtree is not None:
            return result_right_subtree
        else:
            return None

    def contains(self, key) -> bool:
        """
        Returns whether the tree contains a given key, this time using level-order traversal (standard BFS)
        :param key: key to be checked
        :return: whether the tree contains the key
        """
        # BFS (level-order traversal) algorithm
        bfs_queue = Queue()
        bfs_queue.put(self.root)  # Enqueue source node and mark as visited

        while not bfs_queue.empty():
            removed = bfs_queue.get()  # Dequeue from front
            if removed.key == key:  # If the removed node matches, return
                return True
            # Add the removed vertex's adjacent unmarked nodes into the queue and mark them
            # But as in the standard BFS, we only add the adjacent vertices that exist (i.e. not None)
            # Since in the adjacency list rep', all vertices adjacent to a vertex in the list, exist by definition

            if removed.left is not None:
                bfs_queue.put(removed.left)  # mark visited
            if removed.right is not None:
                bfs_queue.put(removed.right)  # mark visited
        return False

    def get_max(self):
        return self._get_max(self.root)

    def _get_max(self, root: TreeNode):
        """
        This returns the maximum key in the binary tree.
        Algorithm: Choose any traversal type. Return the max(recurse left subtree, recurse right subtree, root's key)
        :param root: root of tree
        :Time: O(N)
        :Space: O(N)
        :return: the maximum key in the tree
        """
        if root is None:  # BC1
            return float('-inf')

        # Post-order traverse
        max_left = self._get_max(root.left)
        max_right = self._get_max(root.right)
        root_key = root.key
        return max(max_left, max_right, root_key)

    def get_min(self):
        """
        Returns the minimum key in the binary tree using BFS/level-order traversal
        :Time: O(N)
        :Space: O(N)
        :return: the minimum key in the tree
        """
        # Add source node to queue and mark as visited
        bfs_queue = Queue()
        bfs_queue.put(self.root)
        min_elem = float('+inf')

        while not bfs_queue.empty():
            removed = bfs_queue.get()  # Dequeue from queue
            # Compare the removed element to min_elem and update if smaller
            min_elem = min(removed.key, min_elem)

            # Add removed's adjacent vertices to the queue
            if removed.left is not None:
                bfs_queue.put(removed.left)
            if removed.right is not None:
                bfs_queue.put(removed.right)
        return min_elem

    def get_height(self) -> int:
        return self._get_height(self.root)

    def _get_height(self, root) -> int:
        """
        Returns the height of the binary tree.
        Algorithm: max(recur left, recur right) + 1
        Explanation: The height of a binary tree that is rooted at a certain node is equal to the
        maximum of the heights of its left and right subtrees + 1 (take into account the root node)
        :param root: root of the tree
        :return: the height of the tree
        """
        # BC
        if root is None:
            return 0
        # Take the maximum of the height of the left subtree and the right subtree, and add 1 to the result
        height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        return height


if __name__ == "__main__":
    test = BinaryTree()
    for i in range(1, 11):
        test.insert(i, i ** 2)

    print_level_order(test.root)
    print("")
    print_post_order(test.root)
    print("")
    # print(test.get(11))
    print(test.get(7).val)
    print(test.contains(6))

    test_2 = BinaryTree()
    for i in range(1, 11):
        test_2.insert(int(random.random() * 100))
    print_level_order(test_2.root)
    print("")
    print(test_2.get_max())
    print(test_2.get_min())
    print(test_2.get_height())
