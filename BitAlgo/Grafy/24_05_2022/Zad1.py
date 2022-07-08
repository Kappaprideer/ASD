# Windy w drapaczu chmur 
# Wieżowiec ma 100 pięter i n wind, nie ma natomiast schodów. Każda windwa posiada liste pięter, do których dojeżdża i prędkość w sekundach na piętro. 
# Jesteśmy na piętrze "i" oraz chcemy dostać się na piętro "j", ile minimalnie czasu musimy spędzić w windach by dostać się na piętro "j" ? 
# -----------------------------------------------------------------------------------------------------------------------------------------
# Rozwiązanie: 
# Tworzymy graf w którym piętra to wierzchołki, zaś krawędzie mają wagę przejazdu windy z piętra x na y, z uwagi że windy nie
# muszą zatrzymywać się na każdym piętrze po kolei to winda może jechać np z piętra 2 na 4 omijając 3.

from queue import PriorityQueue

def Dijkstra(G,i,j):
    n=len(G)
    Q=PriorityQueue()
    d=[10**10 for _ in range(n)]
    d[i]=0
    Q.put(i)
    while not Q.empty():
        s=Q.get()
        for  u in G[s]:
            if d[u[0]]>d[s]+u[1]:
                d[u[0]]=d[s]+u[1]
                Q.put(u[0])

    return d[j]

if __name__=="__main__":
    # tablica krotek, gdzie każda krotka zawiera: (czas przejazdu windy miedzy pietrami, pietra na których winda się zatrzymuje)
    elevators=[
    # (2,[0,1,3]),(3,[2,3])]
    (4,[0,2,4]),(8,[0,3]),(1,[2,3]),(6,[1,3]),(2,[2,3,4])]
   
    
    n=len(elevators)
    G=[ [] for _ in range(10)]
    for ele in elevators:
        for i in range(1,len(ele[1])):
            G[ele[1][i-1]].append((ele[1][i], ele[0]))
            G[ele[1][i]].append((ele[1][i-1], ele[0]))
    i=0
    j=4
    print(Dijkstra(G,i,j))

            
