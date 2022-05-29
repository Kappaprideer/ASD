# Andrzej Zaborniak
# Program przechodzi przez 


from zad8testy import runtests
import math

class Node:
    def __init__(self, value):
        self.parent=self
        self.value = value
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1


def highway( A ):
    n=len(A)
    G=[]

    for i in range(n):
         for j in range(i+1,n):
             G.append(( (math.ceil(math.sqrt((A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2))), i, j) )

    G.sort(key=lambda x: x[0])
    odp=10**10
    distance=[ None for _ in range(n)]

    for s in range(len(G)):
        for i in range(n):
            distance[i]=Node(i)

        najkrocej=10**10
        najdluzej=-1
        v=0
        left=s-1
        right=s+1
        union(distance[G[s][1]], distance[G[s][2]])
        najkrocej=min(najkrocej,G[s][0])
        najdluzej=max(najdluzej, G[s][0])

        while v<n-2:
            if left>=0 and right<n:
                if G[s][0]-G[left][0]<G[right][0]-G[s][0]:
                    e=left
                    left-=1
                else:
                    e=right
                    right+=1
            elif left<0:
                e=right
                right+=1
            elif right>=n:
                e=left
                left-=1
            if find(distance[G[e][1]]) != find(distance[G[e][2]]):
                union(distance[G[e][1]], distance[G[e][2]])
                najkrocej=min(najkrocej,G[e][0])
                najdluzej=max(najdluzej, G[e][0])
                v+=1

        odp=min(odp,najdluzej-najkrocej)   
    
    return odp

    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True  )