#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: The three kinds of traversal methods for a binary tree.
             Including recurrent method and non-recurrent method.

Author: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/09/12 09:31:22
"""
import os

os.sys.path.insert(0, "./")

from tqdm import trange
from binarytree import Node
from binarytree import BinaryTree
from binarytree import SearchBinaryTree

def nr_preorder_traversal(node):
    """
    The non-recurrent preorder traversal method for a binary tree.
    Args:
        node: The node of the tree, usually root node.
    Return:
        res: the traversal results.
    """
    res = []
    stack = [node]
    while len(stack) > 0:
        res.append(node.value)
        if node.rchild is not None:
            stack.append(node.rchild)
        if node.lchild is not None:
            stack.append(node.lchild)
        node = stack.pop()
    return res

def nr_inorder_traversal(node):
    """
    The non-recurrent inorder traversal method for a binary tree.
    Args:
        node: The node of the tree, usually root node.
    Return:
        res: the traversal results.
    """
    res = []
    stack = []
    pos = node
    while pos is not None or len(stack) > 0:
        if pos is not None:
            stack.append(pos)
            pos = pos.lchild
        else:
            pos = stack.pop()
            res.append(pos.value)
            pos = pos.rchild
    return res

def nr_postorder_traversal(node):
    """
    The non-recurrent postorder traversal method for a binary tree.
    Args:
        node: The node of the tree, usually root node.
    Return:
         res: the traversal results.
    """
    res = []
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.lchild is not None:
            stack.append(node.lchild)
        if node.rchild is not None:
            stack.append(node.rchild)
    while len(stack2) > 0:
        res.append(stack2.pop().value)
    return res

if __name__ == "__main__":
    stree = SearchBinaryTree()
    inlst = [1, 2, 3, 4, 5, 6, 7]
    for i in trange(len(inlst)):
        stree.root = stree.insert(stree.root, inlst[i])
        print("add %d into the search-binary-tree successfully!" % inlst[i])
    root = Node()
    root = stree.root
    print("nr_preorder_traversal: ", nr_preorder_traversal(root))
    print("nr_inorder_traversal: ", nr_inorder_traversal(root))
    print("nr_postorder_traversal: ", nr_postorder_traversal(root))