# Dostajemy drzewo w reprezentacji krawędziowej oraz wyróżniony wierzchołek. Każdy wierzchołek tworzy swoje własne poddrzewo.
# Dla każdego wierzchołka wyznaczyć ilość wierzchołków w jego poddrzewie. 

from collections import deque

def tree_size(T,root):
    n=0
    for i in T:
        n=max(n,i[0])
        n=max(n,i[1])
    n+=1
    G=[ [] for _ in range(n)]
    for i in T:
        G[i[0]].append(i[1])
        G[i[1]].append(i[0])
    visited = [ 0 for _ in range(n)]
    result= [ 0 for _ in range(n)]

    def visit(G,s):
        nonlocal result
        if len(G[s])==1:
            return 1
        for u in G[s]:
            if visited[u]==0:
                visited[u]=1
                result[s]+=visit(G,u)
        return result[s]+1

    visited[root]=1
    visit(G,root)
    x=0
    print("Wypisuje numer poddrzewa oraz jego rozmiar:")
    for line in result:
        print(x,line)
        x+=1

if __name__=="__main__":
    tab=[(5,4),(5,2),(5,0),(4,1),(4,3),(4,10),(10,11),(0,6),(6,7),(7,8),(7,9)]
    tree_size(tab, 5)
