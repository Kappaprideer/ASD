# Algorytm:
# - przechodzenie DFS ale nie korzystając z tablicy visited
#   tylko usuwając krawędzie po których przeszliśmy 
# - po przetworzeniu wierzchołka dopisujemy go na poczatku 
#   tworzonego cyklu 
# ---------------------------------------------------------------

def DFS_visited(G,result,s):
    for u in G[s]:
        G[s].remove(u)
        G[u].remove(s)
        DFS_visited(G,result,u)
    result.append(s)
    
def find_Euler_cycle(G):
    V = len(G)
    result=[]
    DFS_visited(G,result,0)
    result=result[::-1]
    return result

# -------------------------------------------------------------


if __name__=="__main__":
    graph=[[1,2],[0,2,3,5],[0,1,3,5],[1,2,4,5],[3,5],[1,2,3,4]]
    print(find_Euler_cycle(graph))