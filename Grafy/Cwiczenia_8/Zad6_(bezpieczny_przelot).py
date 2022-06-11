exist=False

def visit(G,visited,s,t,pulap):
    global exist
    visited[s]=1
    if not exist:
        for u in G[s]:
            if visited[u[0]]==0 and u[1]==pulap and not exist:
                if u[0]==t:
                    exist=True
                    return
                visit(G,visited,u[0],t,pulap)
    visited[s]=0

def saveadventure(G,s,t):
    n=len(G)
    global exist
    visited=[0 for _ in range(n)]
    pulap=0
    for u in G[s]:
        if not exist:
            visit(G,visited,u[0],t,u[1])
    return exist


if __name__=="__main__":
    graph=[ (0,2,8),(2,5,4),(5,6,8),(3,6,7),(0,3,8),(3,2,4),(4,2,8),(3,5,8),(1,5,5),(1,6,6),(4,6,2),(0,5,4)]    # graf zapisany w postaci listy krawędzi
    n=0
    for u in graph:
        n=max(n,u[0])
        n=max(n,u[1])
    n+=1
    G = [ [] for _ in range(n)]
    for u in graph:
        G[u[0]].append((u[1],u[2]))
        G[u[1]].append((u[0],u[2]))
    for line in G:
        print(line)
    s=2
    t=6
    print("Przelot w tym samym pułapie jest możliwy:", saveadventure(G,s,t))