from zad9ktesty import runtests
from math import inf

def prom(P, g, d):
    gd=g+d
    n=0
    sum=0
    numbers=[]
    while n<len(P) and sum<gd:
        numbers+=tab[n]
        sum+=tab[n]
        n+=1
    if sum>gd:
        sum-=tab[n-1]
        n-=1
    tab=[ [ 0 for _ in range(g+1)] for i in range(n+1)]
    

    



    
    
    
    
    
    
    return 

runtests ( prom )