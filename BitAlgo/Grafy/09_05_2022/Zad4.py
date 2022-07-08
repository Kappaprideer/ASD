# Dany jest ciąg przedziałów postaci [a,b]. Dwa przedziały można skleić, jeżelie mają dokłądnie jeden punkt wspólny.
# Podać algorytm który sprawdza czy da się skleić tak przedziały aby tworzyły odcinek [x,y]

# Na początku tworzę graf w którym wierzchołki to punkty krańcowe przedziałów a oraz b, a krawędź to przedział. Graf jest skierowany.
# np. dla przedziału [2,7],[2,9] graf wygląda 2-->7
#                                             |
#                                              ---> 9

from collections import deque

def graph_making(T):
    n=0
    for u in T:
        n=max(n,u[1])
    n+=1
    tab=[ [] for _ in range(n)]
    for u in T:
        tab[u[0]].append(u[1])
    visited= [ 0 for _ in range(n)]
    return tab, visited

def exist_interval(T,a,b):
    G, visited=graph_making(T)
    q=deque()
    q.append(a)
    while len(q)>0:
        s=q.popleft()
        for i in G[s]:
            if visited[i]==0:
                if i==b:
                    return True
                if i<b:
                    visited[i]=1
                    q.append(i)
    return False

if __name__=="__main__":
    T=[[6,10],[0,2],[1,3],[2,4],[0,3],[3,6]]
    print(exist_interval(T,0,10))