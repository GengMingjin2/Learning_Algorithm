import os

os.sys.path.insert(0, "../../Binary_Tree/")
from queue import Queue

from tqdm import trange

from binarytree import SearchBinaryTree

def dfs(root, res):
    """ Deep-First-Search Method for a tree
    Args:
        root: The root node of a tree. """
    if root == None:
        return res
    res.append(root.value)
    if root.lchild:
        dfs(root.lchild, res)
    if root.rchild:
        dfs(root.rchild, res)

if __name__ == "__main__":
    # Generate a binary search tree to test the bfs function
    stree = SearchBinaryTree()
    inlst = [2, 1, 5, 7, 6, 4, 3]
    for i in trange(len(inlst)):
        stree.root = stree.insert(stree.root, inlst[i])
    res = []
    dfs(stree.root, res)
    print(res)

