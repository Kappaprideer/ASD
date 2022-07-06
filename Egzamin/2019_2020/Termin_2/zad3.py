from zad3testy import runtests

def DFS_visit(G,visited,s,ans):
    for u in G[s]:
        if visited[u]==0:
            visited[u]=1
            DFS_visit(G,visited,u,ans)
    ans.append(s)

def tasks(T):
    n=len(T)
    G=[ [] for _ in range(len(T))]
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j]==1:
                G[i].append(j)

    ans=[]
    visited=[0 for _ in range(n)]
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            DFS_visit(G,visited,i,ans)
    ans=ans[::-1]
    
    return ans 



runtests( tasks )
