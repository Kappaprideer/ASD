


def domkniecia_grafu(G):
    count=0
    n=len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if G[i][k]==1 and G[k][j]==1 and G[i][j]==0:
                    G[i][j]=1
                    count+=1
    return count//2


if __name__=="__main__":
    # graf reprezentowany w postaci listy krawędzi 
    graph=[    
    [4,7,5],
    [2],
    [1,5],
    [8],
    [0],
    [2,0,8],
    [8],
    [0],
    [5,6,3]]
    n=len(graph)
    G=[ [0 for _ in range(n)] for i in range(n)]
    for i in range(n):
        for u in graph[i]:
            G[i][u]=1
    print(domkniecia_grafu(G))