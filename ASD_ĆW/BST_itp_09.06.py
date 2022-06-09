# Tworzenie drzewa BST i wstawianie nowych elementów do drzewa BST 

class Node:
    def __init__(self,val):
        self.val=val
        self.parent=None
        self.left=None
        self.right=None


def add_element(root,x):
    if root is None:
        root=x
    else:
        u=root
        while u is not None:
            if u.val<x.val:
                prev = u
                u=u.right
            elif u.val>x.val:
                prev=u
                u=u.left
        if prev.val < x.val:
            prev.right=x
        else:
            prev.left=x
        x.parent=prev
    return root

# Wyszukiwanie następnika 
def maximum(root):
    r=root
    while r.right is not None:
        r=r.right
    return r.val

def minimum(root):
    r=root
    while r.left is not None:
        r=r.left
    return r.val


def succ(root, x):
    if x.right is not None:
        return minimum(x.right)
    v=x
    while v.parent is not None and v!=v.parent.left:
        v=v.parent
        
        
