# Pary ludzi znających się. Pierwszego dnia osoba 0 mówi informacje którą się dowiedziała wszystkim osobom które zna, następnego dnia każda kolejna osoba
# mówi swoim znajomym o tej informacji jeśli jeszcze jej nie usłyszeli. Którego dnia i ile najwięcej osób dowie się nowej informacji. 

from collections import deque

def BFS(G):
    visited=[ 0 for _ in range(len(G))]
    day=-1
    maximum=0
    ppl = [ 0 for _ in range(len(G))]
    d = [ 10**10 for _ in range(len(G))]
    Q=deque()
    Q.append(0)
    d[0]=0
    visited[0]=1
    while len(Q)>0:
        s=Q.popleft()
        for u in G[s]:
            if visited[u]==0:
                visited[u]=1
                Q.append(u)
                d[u]=d[s]+1
                ppl[d[u]]+=1
                if ppl[d[u]]>maximum:
                    maximum=ppl[d[u]]
                    day=d[u]
    return day, ppl[day]


if __name__=="__main__":
    G=[[3],[2],[1,4,5],[0,4],[2,3,5],[4,2]]
    day, number_of_ppl = BFS(G)
    print()
    print("Number of ppl:", number_of_ppl, "Day: ", day)
    print()

