#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
from re import T


class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Initialize size of Leaf to 1
    v.size = 1
    # If there's a left/right subtree, reassign v.size to equal its size
    if v.left:
        v.size = calculate_sizes(v.left) + v.size
    if v.right:
        v.size = calculate_sizes(v.right) + v.size
    # Return the size at each node starting at the bottom of the tree
    
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)

def find_vertex(r):
    n = r.size 
    if r.left and r.right:
        if r.size < n/2:
            return r
        if r.left.size > r.right.size:
            find_vertex(r.left)
        if r.right.size > r.left.size:
            find_vertex(r.right)
    elif r.left:
        r = r.left
        find_vertex(r)
    elif r.right:
        r = r.right
        find_vertex(r)
    return r