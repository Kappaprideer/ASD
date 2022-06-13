def DFS_visit(G,visited,s, sorted_graph):
    for u in G[s]:
        if visited[u]==0:
            visited[u]=1
            DFS_visit(G,visited,u, sorted_graph)
    sorted_graph.append(s)

def topological_sorting(G):
    sorted_graph=[]
    n=len(G)
    visited=[0 for _ in range(n)]
    for u in range(n):
        if visited[u]==0:
            visited[u]=1
            DFS_visit(G,visited,u, sorted_graph)
    sorted_graph=sorted_graph[::-1]

    print(sorted_graph)

    for i in range(n-1):
        exist=False
        for u in G[sorted_graph[i]]:
            if u==sorted_graph[i+1]:
                exist=True
        if not exist:
            return False

    return True

if __name__=="__main__":
    G=[
    [2,5],
    [3],
    [1,3],
    [],
    [2],
    [3,4]
    ]

    print(topological_sorting(G))