from tests_party import runtests

class Employee:
    def __init__(self, fun):
        self.fun = fun 
        self.emp = []
        self.f = -1 
        self.g = -1

def party_without_boss(v):
    if v.g != -1:
        return v.g
    v.g=0
    for u in v.emp:
        v.g+=party(u)
    return v.g

def party(root):
    if root.f != -1:
        return root.f
    f1 = party_without_boss(root)
    f2 = root.fun
    for u in root.emp:
        f2+=party_without_boss(u)
    root.f = max(f1, f2)
    return root.f


runtests ( party )