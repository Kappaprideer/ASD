from zad2testy import runtests
from collections import deque


def DFS_visit(v):
    for i in range(len(v.edges)):
        v.sum+=v.weights[i]+DFS_visit(v.edges[i])
    return v.sum

def balance( T ):
    DFS_visit(T)
    difference=10**10
    ans=None
    Q=deque()
    Q.append(T)
    while len(Q)>0:
        s=Q.popleft()
        for i in range(len(s.edges)):
            Q.append(s.edges[i])
            if difference>(abs(T.sum-(s.edges[i]).sum - s.weights[i] - (s.edges[i]).sum)):
                difference=abs(T.sum-(s.edges[i]).sum - s.weights[i] - (s.edges[i]).sum)
                ans=s.ids[i]
    return ans
    
runtests( balance )


