# Napisz program sprawdzający czy graf posiada cykl 
from collections import deque

def Is_cycle(G,visited,s,parent):
    exist=False
    visited[s]=1
    for u in G[s]:
        if visited[u]==0:
            exist = exist or Is_cycle(G,visited,u,s)
        elif visited[u]==1 and u!=parent:
            exist=True
    visited[s]=2    
    return exist

def DFS(G):
    visited=[0 for _ in range(len(G))]
    for i in range(len(G)):
        if Is_cycle(G,visited,i,None):
            return True
    return False

if __name__=="__main__":
    G=[[3],[2],[1,4,5],[0,4],[2,3,5],[4,2]]
    print(DFS(G))








