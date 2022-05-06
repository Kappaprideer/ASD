# BFS - breadth-first-search
# graf G jest reprezentowany w postaci macierzowej

from queue import Queue

def reading_graph(T):
    n=0
    for edge in T:
        n=max(n, edge[0])
        n=max(n, edge[1])
    G=[[0 for i in range(n+1)] for j in range(n+1)]
    for edge in T: 
        G[edge[0]][edge[1]] = 1
        G[edge[1]][edge[0]] = 1
    return G

def BFS(G):
    Q=Queue()
    n=len(G)
    visited=[False for _ in range(n)]
    Q.put(0)
    visited[0] = True
    lenght=[0 for _ in range(n)]

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if G[i][u] == 1 and not visited[i]:
                lenght[i]=lenght[u]+1
                visited[i]=True
                Q.put(i)
    
    for line in G:
        print(line)

    print("\n",lenght)




if __name__=="__main__":
    T=[[1,0],[1,2],[2,0],[3,1],[2,3]]
    G = reading_graph(T)
    BFS(G)

