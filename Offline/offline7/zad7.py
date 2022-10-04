# Program uruchamia DFS ktory przechodzi po kolei wierzchołki sprawdzając za każdym razem czy przyszedł od bramy północej czy południowej, jeśli przyszedł z północej
# to idzie dalej sprawdzając południowe bramy i analogicznie dla południowej. DFS rozpoczyna pracę zawsze od wierzchołka o numerze ,,0,, ponieważ jeśli ścieżka przechodzi
# przez każde miasto to musi go również uwzględnić. Program kończy działanie jeśli DFS dojdzie do wierzchołka zero ponownie, przekraczając bramę z innej strony niż zaczynał
# oraz gdzy liczba odwiedzonych przez niego szybciej miast jest równa liczbie wszytkich miast. W przeciwnym razie jeśli warunki nie zostaną spełnione program zwraca None.

from zad7testy import runtests

s_v=0
current=False
def DFS_visit(G,s,visited, parent, start):    # s_v - sum of visited - suma odwiedzonych wierzchołkow
    global s_v
    global current
    if current==True:
        return
    s_v+=1
    came=-1
    visited[s]=True
    for i in range(2):
        for x in G[s][i]:
            if x==parent[s]:
                came=(i+1)%2
                break
    
    if s==0 and came==start and s_v==len(G):
        current=True
        return

    elif s==0:
        visited[s]=False
        s_v-=1
    
    else:
        for u in G[s][came]:
            if not visited[u]:
                parent[u]=s
                DFS_visit(G,u,visited,parent,start)
                if current:
                    return
        visited[s]=False
        s_v-=1
    


def droga( G ):
    visited=[ False for _ in range(len(G))] 
    parent=[-1 for _ in range(len(G))]
    result=[]
    global current
    global s_v
    current=False
    s_v=0
    for i in range(2):
        for u in G[0][i]:
            parent[u]=0
            DFS_visit(G,u,visited,parent,i)
            if current:
                p=parent[0]
                for w in range(len(G)):
                    result.append(p)
                    p=parent[p]
                return result

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )