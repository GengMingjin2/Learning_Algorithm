import os

os.sys.path.insert(0, "../../Binary_Tree/")
from queue import Queue

from tqdm import trange

from binarytree import SearchBinaryTree

def bfs(root):
    """ Breadth-First-Search Method for a tree
    Args:
        root: The root node of a tree. """
    if root == None:
        return
    q = Queue()
    q.put(root)

    res = []
    while not q.empty():
        temp = q.get()
        res.append(temp.value)

        if temp.lchild:
            q.put(temp.lchild)
        if temp.rchild:
            q.put(temp.rchild)
    return res

if __name__ == "__main__":
    # Generate a binary search tree to test the bfs function
    stree = SearchBinaryTree()
    inlst = [2, 1, 5, 7, 6, 4, 3]
    for i in trange(len(inlst)):
        stree.root = stree.insert(stree.root, inlst[i])
    print(bfs(stree.root))

