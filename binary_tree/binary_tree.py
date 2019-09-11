#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: The defination for class binary tree.

Author: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/11 16:06:22
"""

import os
from tqdm import tqdm
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
    Class defination of BinaryTree.
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


if __name__ == "__main__":
    tree = BinaryTree()
    inlst = [1, 2, 3, 4, 5, 6, 7]
    for i in trange(len(inlst)):
        tree.add(inlst[i])
        print("add %d into the tree success" % inlst[i])
    print("preorder: ", tree.preorder_traversal(tree.root))
    print("inorder: ", tree.inorder_traversal(tree.root))
    print("posorder: ", tree.postorder_traversal(tree.root))