#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Description: The Deep-First-Search Method for a binary tree.

Author: gengmingjin(gengmingjin@bupt.edu.cn)
Date: 2019/10/15 17:55:22
"""
import os
os.sys.path.insert(0, "../../Binary_Tree/")

from tqdm import trange

from binarytree import SearchBinaryTree

def dfs_recurrent(root, res):
    """
    Deep-First-Search Method for a tree(Recurrent)
    Args:
        root: The root node of a tree.
        res: a blank list to save the visited results.
    """
    if root == None:
        return res
    res.append(root.value)
    if root.lchild:
        dfs_recurrent(root.lchild, res)
    if root.rchild:
        dfs_recurrent(root.rchild, res)

def dfs_nonrecurrent(root):
    """
    Deep-First-Search Method for a tree(Non-Recurrent)
    Args:
        root: The root node of a tree.
    """
    res = []
    stack = []
    if root == None:
        return res
    stack.append(root)

    while(len(stack) != 0):
        tmp = stack[-1]
        res.append(tmp.value)
        stack.pop()  #list.pop(), remove the element with the index=-1.
                     # stack.pop() == stack.remove(tmp)

        if tmp.rchild:
            stack.append(tmp.rchild)
        if tmp.lchild:
            stack.append(tmp.lchild)

    return res

if __name__ == "__main__":
    # Generate a binary search tree to test the bfs function
    stree = SearchBinaryTree()
    inlst = [2, 1, 5, 7, 6, 4, 3]
    for i in trange(len(inlst)):
        stree.root = stree.insert(stree.root, inlst[i])
    res = []
    dfs_recurrent(stree.root, res)
    print(res)
    print(dfs_nonrecurrent(stree.root))

