time=0

def dfs_visited(visited,parent, t_1, t_2, G, s):
    global time
    time+=1
    visited[s]=1
    for e in G[s]:
        if visited[e]==0:
            parent[e]=s
            t_1[e]=time
            dfs_visited(visited, parent, t_1, t_2, G, e)
    time+=1
    t_2[e]=time

def DFS(G):
    v=len(G)
    visited=[0 for _ in range(v)]
    t_1=[0 for _ in range(v)]
    t_2=[0 for _ in range(v)]
    parent=[None for _ in range(v)]
    for e in range(v):
        if visited[e]==0:
            dfs_visited(visited,parent,t_1,t_2,G, e)
    print(t_1)
    print(t_2)

if __name__=="__main__":
    graph=[[1,2],[0,2],[0,1]] # reprezentaca grafu w postaci listowej 
    DFS(graph)