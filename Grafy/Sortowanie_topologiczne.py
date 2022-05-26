# dag - directed acyclic graph 
# Algorytm:
# 1. Uruchomić DFS
# 2. Po przetworzeniu wierzchołka dopisać go na początek listy 

def DFS_visited(G, visited, s, sorted_graph):
    for u in G[s]:
        if visited[u]==0:
            visited[u]=1
            DFS_visited(G,visited, u, sorted_graph)
    sorted_graph.append(s)

def DFS(G):
    V=len(G)
    visited=[ 0 for _ in range(V)]
    sorted_graph=[]
    for u in range(V):
        if visited[u]==0:
            DFS_visited(G,visited, u, sorted_graph)
    
    sorted_graph=sorted_graph[::-1]
    return sorted_graph

if __name__=='__main__':
    graph=[[1,2,5],[2,4],[],[],[3,6],[4],[]]
    sorted_graph=DFS(graph)
    print(sorted_graph)
