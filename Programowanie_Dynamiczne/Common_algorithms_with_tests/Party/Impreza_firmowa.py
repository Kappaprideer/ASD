class Employee:
    def __init__(self,fun):
        self.fun=fun
        self.emp=[]  #tablica dzieci wezla
        self.f = -1
        self.g = -1

def g(v):
    if v.g != -1:
        return v.g
    v.g=0
    for u in v.emp:
        v.g+=f(u)
    return v.g

def f(v):
    if v.f != -1:
        return v.f
    f1= g(v)
    f2= v.fun
    for u in v.emp:
        f2+=g(u)
    v.f=max(f1,f2)
    return v.f

if __name__=="__main__":
    pass