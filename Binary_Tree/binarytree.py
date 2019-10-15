#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: The defination for class binary tree.

Author: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/11 16:06:22
"""

from tqdm import trange

class Node(object):
    """
    Class defination of Node in a binary tree.
    """
    def __init__(self, value=0, lchild=None, rchild=None):
        """
        The initial function for the node class.
        """
        # 实例化一个node时值为value，同时没有child node
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    """
    Class defination of BinaryTree.(Balanced)
    """
    def __init__(self):
        """
        The initial function for this class.
        """
        # 实例化一棵树时root node为空
        self.root = None
        self.lis = [] # 保存子节点有空缺的节点，便于插入新的节点
    def add(self, value):
        """
        Add a new node into the tree.
        Args:
            value: The initial value of the node.
        Return:
        """
        node = Node(value)
        if self.root == None:
            self.root = node
            self.lis.append(self.root)
        else:
            while True:
                point = self.lis[0]

                if point.lchild == None:
                    point.lchild = node
                    self.lis.append(point.lchild)
                    return
                elif point.rchild == None:
                    point.rchild = node
                    self.lis.append(point.rchild)
                    self.lis.pop(0)
                    return

    def inorder_traversal(self, root):
        """
        The inorder traversal for a binary tree.
        Args:
            root: The root node of a tree.
        Return:
             res: the traversal results.
        """
        if root == None:
            return []
        return self.inorder_traversal(root.lchild) + [root.value] + self.inorder_traversal(root.rchild)

    def preorder_traversal(self, root):
        """
        The preorder traversal for a binary tree.
        Args:
            root: The root node of a tree.
        Return:
            res: the traversal results.
        """
        if root == None:
            return []
        return [root.value] + self.preorder_traversal(root.lchild) + self.preorder_traversal(root.rchild)

    def postorder_traversal(self, root):
        """
        The postorder traversal for a binary tree.
        Args:
            root: The root node of a tree.
        Return:
            res: the traversal results.
        """
        if root == None:
            return []
        return self.postorder_traversal(root.lchild) + self.postorder_traversal(root.rchild) + [root.value]

class SearchBinaryTree(object):
    """
    The defination for search binary tree.
    """
    def __init__(self):
        """
        The initialization for the class object.
        """
        self.root = None

    def insert(self, root, value):
        """
        Insert a new node into the tree.
        Args:
            root: The root node of the tree.
            value: value of the inserting node.
        """
        if root == None:
            root = Node(value)
        elif value < root.value:
            root.lchild = self.insert(root.lchild, value)
        elif value > root.value:
            root.rchild = self.insert(root.rchild, value)
        return root

    def inorder_traversal(self, root):
        """
        The inorder traversal for a binary tree.
        Args:
            root: The root node of a tree.
        Return:
             res: the traversal results.
        """
        if root == None:
            return []
        return self.inorder_traversal(root.lchild) + [root.value] + self.inorder_traversal(root.rchild)

    def preorder_traversal(self, root):
        """
        The preorder traversal for a binary tree.
        Args:
            root: The root node of a tree.
        Return:
            res: the traversal results.
        """
        if root == None:
            return []
        return [root.value] + self.preorder_traversal(root.lchild) + self.preorder_traversal(root.rchild)

    def postorder_traversal(self, root):
        """
        The postorder traversal for a binary tree.
        Args:
            root: The root node of a tree.
        Return:
            res: the traversal results.
        """
        if root == None:
            return []
        return self.postorder_traversal(root.lchild) + self.postorder_traversal(root.rchild) + [root.value]

    def query(self, root, value):
        """
        Query a value in a search binary tree.
        Args:
            root: The root node of the tree.
            value: Value to be searched.
        Return:
            True: The value is in the tree.
            False: The value is not in the tree.
        """
        if root == None:
            return False
        if root.value == value:
            return True
        elif value < root.value:
            return self.query(root.lchild, value)
        elif value > root.value:
            return self.query(root.rchild, value)

    def find_min(self, root):
        """
        Find the minimum in the tree.
        Args:
            root: The root node of the tree
        Return:
             The min value node in the tree.
        """
        if root.lchild:
            return self.find_min(root.lchild)
        else:
            return root

    def find_max(self, root):
        """
        Find the maximum in the tree.
        Args:
            root: The root node of the tree.
        Return:
            The max value node in the tree.
        """
        if root.rchild:
            return self.find_max(root.rchild)
        else:
            return root

    def delete(self, root, value):
        """
        Delete the node of which the node.value is value.
        Args:
            root: The root node of the tree.
            value: The value of the node to be deleted.
        Return:
            The root node of the tree.
        """
        if root == None:
            return
        if value < root.value:
            root.lchild = self.delete(root.lchild, value)
        elif value > root.value:
            root.rchild = self.delete(root.rchild, value)
        else:
            if root.lchild and root.rchild:
                temp = self.find_min(root.rchild, value)
                root.value = temp.value
                root.rchild = self.delete(root.rchild, temp.value)
            elif root.rchild == None and root.lchild == None:
                root = None
            elif root.right == None:
                root = root.lchild
            elif root.lchild == None:
                root = root.rchild
        return root

if __name__ == "__main__":
    tree = BinaryTree()
    stree = SearchBinaryTree()
    inlst = [1, 6, 5, 4, 3, 2, 7]
    for i in trange(len(inlst)):
        tree.add(inlst[i])
        stree.root = stree.insert(stree.root, inlst[i])
        print("add %d into the tree success" % inlst[i])
    print("preorder: ", tree.preorder_traversal(tree.root))
    print("inorder: ", tree.inorder_traversal(tree.root))
    print("posorder: ", tree.postorder_traversal(tree.root))
    print("sbt-preorder: ", stree.preorder_traversal(stree.root))
    print("sbt-inorder: ", stree.inorder_traversal(stree.root))
    print("sbt-postorder: ", stree.postorder_traversal(stree.root))
