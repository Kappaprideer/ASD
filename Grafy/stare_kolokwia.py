# DWUMILOEW BUTY

from queue import PriorityQueue
from math import inf

def dijkstra1(G,s,w):

    n = len(G)
    d = [[inf]*2 for _ in range(n)]
    d[s][0] = 0
    d[s][1] = 0
    K=PriorityQueue()
    K.put((0, s, 0))
    visited = [[False]*2 for _ in range(n)]
    visited[s][1] = True
    while not K.empty():
        u=K.get()
        if u[1] == w:
            return u[0]
        if visited[u[1]][u[2]] is False:
            visited[u[1]][u[2]] = True
            print(".")
            print(u)
            # isć normalnie możemy zawsze
            for i in range(n):
                if G[u[1]][i] != 0 :
                    if d[i][0] > u[0] + G[u[1]][i]:
                        d[i][0] = u[0] + G[u[1]][i]

                        K.put((d[i][0], i, 0))

            # uzywac dwumilowych butów możemy tylko jak przyszliśmy do wierzchołka normalnie
            # w tym wypadku robiłam troche inaczej niz tlumaczyłam na zajęciach (wydaje mi się że łatwiej)
            # jeżeli jestem w danym weirzchołku i moge użyć dwumilowych butów to odrazu sprawdzam wszystkie
            # możliwości gdzie mogłabym dojść używając ich zaczynając od tego wierzchołka
            if u[2] == 0:
                for i in range(n):
                    if G[u[1]][i] != 0:
                        for j in range(n):
                            if G[i][j] != 0 :
                                x = max(G[u[1]][i],G[i][j])
                                if d[j][1] > u[0] + x:
                                    d[j][1] = u[0] + x
                                    K.put((d[j][1], j, 1))
    return False

G = [
    [0,1,0,0,0],
    [1,0,1,0,0],
    [0,1,0,7,0],
    [0,0,7,0,8],
    [0,0,0,8,0],
     ]
'''G=[[0, 1, 200, 200, 200, 200],
 [1, 0, 2, 200, 200, 200],
 [200, 2, 0, 40, 200, 200],
 [200, 200, 40, 0, 40, 200],
 [200, 200, 200, 40, 0, 117],
 [200, 200, 200, 200, 117, 0]]'''
print(dijkstra1(G,0,4))

# ------------------------------------------------------------------------------
# Najktórsza trasa z tankowaniem


# '''Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
# krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
# Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
# trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
# na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
# odległość d bez tankowania).'''

from math import inf
from queue import PriorityQueue

# wrzucam do kolejki krotki (dystans, wierzchołek, ilosc paliwa z ktorym wyruszamy)
# tworze distance ktory dla kazdego wierzcholka ma tablice dlugosci d, pod kazdym indeksem jest zapisana dlugosc najkrotszej trasy takiej ze dojedzamy z inx paliwa do wietrzchołka

# szukanie rozwiania niestety jest trudne, robie tak samo tablice parentow dla kazdego wierzcholka z d miejscami,
# gdzie zapisuje parenta konkretnego jako krotke (wierzcholek i z jaka iloscia z tego wierzcholka wyruszl), jezeli
# wyruszyl z ilosc d to znaczy ze tam tankowal
# przez co musze znalezc indeks pod ktorym ma dotychasz zapisana najkrotsza trase i z tego miejsca kontynuuje
def jak_dojade(G, P, d, a ,b):
    n = len(G)
    distance = [[inf] * d for _ in range(n)]
    for i in range(d):
        distance[a][i] = 0
    K = PriorityQueue()

    K.put((0, a, d))
    #visited = [False for _ in range(n)]
    p = [[-1]*d for _ in range(n)]

    while not K.empty():
        u = K.get()

        if u[1] == b:
            path = [b]
            parent = p[b][u[2]]
            while parent[0] != a:
                path.append(parent[0])
                if parent[1] == d:
                    max = 0
                    for i in range(d):
                        if distance[parent[0]][i] < distance[parent[0]][max]:
                            max = i
                    parent = p[parent[0]][max]
                else:
                    parent = p[parent[0]][parent[1]]

            path.append(a)
            return path[::-1]

        for x in range(n):
            if G[u[1]][x] > 0 and G[u[1]][x] <= u[2]:
                if distance[x][u[2]-G[u[1]][x]] > G[u[1]][x] + u[0]:
                    distance[x][u[2] - G[u[1]][x]] = G[u[1]][x] + u[0]
                    p[x][u[2] - G[u[1]][x]] = (u[1],u[2])
                    if x in P:
                        K.put((distance[x][u[2]-G[u[1]][x]],x,d))
                    else:
                        K.put((distance[x][u[2]-G[u[1]][x]], x, u[2] - G[u[1]][x]))

    return None


G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]
print("JAK DOJADE: ")
print(jak_dojade(G, P, 6, 0, 2))

# --------------------------------------------------------------------------------------------------
# Dijkstra macierzowo 


from math import inf

def dijkstra2(G,v):

    n = len(G)
    visited = [False] * n
    distance = [inf] * n
    parent = [-1] * n
    distance[v] = 0
    inx = v

    while True:
        print(inx)
        visited[inx] = True
        next_id = -1
        min_d = inf

        # znajdowanie krawędzi kolejnej
        for i in range(n):
            if visited[i]:
                continue
            # aktualizcja minimalnje odlegosci sasiadow
            if G[inx][i] != -1 and distance[i]>distance[inx]+ G[inx][i]:
                distance[i] = distance[inx] + G[inx][i]
                parent[i] = inx
            # wybranie nastepengeo rozpatrywanego wierzcholka (takiego z min odlegloscia)
            if min_d>distance[i]:
                next_id = i
                min_d = distance[i]

        if next_id == -1: # jezeli jest -1 to wszystkie wierzcholki dostpene z v sa odwiedzone( nie sprawdza spojnosci)
            #return distance, parent
            return distance

        inx = next_id




'''G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 1,-1,-1]]'''
G = [
     [-1,4,-1,-1,6,2,-1],
     [4,-1,2,-1,-1,-1,-1],
     [-1,2,-1,2,-1,-1,-1],
     [-1,-1,2,-1,3,1,-1],
     [6,-1,-1,3,-1,5,2],
     [2,-1,-1,1,5,-1,7],
     [-1,-1,-1,2,7,-1]]
print(dijkstra2(G,0))

# ---------------------------------------------------------------------
# Zad 7
'''Pewien podróżnik chce przebyć trasę z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.'''

from queue import PriorityQueue
from math import inf

def dijkstra(G,v,s,D,T):

    n = len(G)
    d = [[inf]*D for _ in range(n)]
    d[v][0] = 0
    visited = [[False]*D for _ in range(n)]
    p = [[-1]*D for _ in range(n)]
    K = PriorityQueue()
    K.put((0, v, 0)) # krotka - (dotychczaswoy koszt, wierzchołek, ile l benzyny mam dojezdzajac do wierzchołka)
    while not K.empty():
        u=K.get()
        x = u[0]    # obecny koszt
        y = u[1]    # wierzchołek obecny
        z = u[2]    # l benzyny które mam dojeżdżając
        if y == s:
            return x
        if visited[y][z] is False:
            visited[y][z] = True
            i = 0
            while i+z <= D:
                for v in G[y]:
                    if v[1] <= i+z and d[v[0]][i+z-v[1]] > x + i*T[y]:
                        d[v[0]][i+z-v[1]] = x + i*T[y]
                        p[v[0]][i+z-v[1]] = y
                        K.put((x + i*T[y],v[0],i+z-v[1]))
                i += 1

    return d


A = [
    [(1,3),(4,2),(3,3)],    # 0
    [(0,3),(3,4),(2,5)],    # 1
    [(1,5),(3,2),(7,1)],    # 2
    [(0,3),(1,4),(2,2),(6,4)],  # 3
    [(0,2),(5,3)],      # 4
    [(4,3),(6,4),(8,3)]   ,  # 5
    [(5,4),(3,4),(8,2),(7,3)],  # 6
    [(2,1),(6,3),(8,1)], # 7
    [(5,3),(6,2),(7,1)]

]
T = [1,3,2,2,2,2,4,4,3]
print("Zadanie 7:")
print(dijkstra(A,0,8,5,T))


# ---------------------------------------------------------------------

'''Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.

Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.'''

from queue import PriorityQueue
from math import inf

def dijkstra(G,v,t):

    n = len(G)
    d = [[inf,inf,inf] for _ in range(n)]
    d[v][0] = 0
    d[v][1] = 0
    d[v][2] = 0
    K=PriorityQueue()

    for i in range(n):
        if G[v][i] != 0:
            if G[v][i] == 1:
                x = 1
                y = 0
            elif G[v][i] == 5:
                x = 5
                y = 1
            else:
                x = 8
                y = 2
            G[v][i] = 0
            G[i][v] = 0
            if d[i][y] >  x:
                d[i][y] =  x
                K.put((d[i][y], i, x))

    while not K.empty():
        u=K.get()
        if u[1] == t:
            return u[0]
        for v in range(n):
            # robie teraz tą notatke na szybko (mogę pisać głupoty)
            # x to chyba to to co dodam do dotyhchczasowego kosztu podróży
            # y to indeks pod którym zapisze ten koszt
            # (każdy wierzchołek ma tablice 3 elem. w zaleznosci czy docieram tam samolotem, promem czy mostem)
            # do kolejki przekazuje krotke (koszt, wierzchołek, jak tam dotarłam (wartosc x to okresla))
            # G[u[1]][v] != u[2] warunek zeby nie isc do nastepnego wiercholka w taki sam spsob
            if G[u[1]][v] != 0 and G[u[1]][v] != u[2]:
                if G[u[1]][v] == 1:
                    x = 1
                    y = 0
                elif G[u[1]][v] == 5:
                    x = 5
                    y = 1
                else:
                    x = 8
                    y = 2
                G[u[1]][v] = 0
                G[v][u[1]] = 0
                if d[v][y] > u[0] + x:
                    d[v][y] = u[0] + x
                    K.put((d[v][y], v, x))
    return None

G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]



# ------------------------------------------------------------------------------------------
# BLUE AND GREEN
from math import inf

def Floyd_Warshall(G):
    n = len(G)
    for t in range(n): # na wykladzie (1,n+) inna numeracja wierzchołkow
        for u in range(n):
            for w in range(n):
                G[u][w] = min(G[u][w], G[u][t] + G[t][w])

def BlueAndGreen(T, K, D):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if i!=j and T[i][j] == 0:
                T[i][j] = inf
    Floyd_Warshall(T)
    #print(T)
    for i in range(n):
        for j in range(n):
            '''if j>=n//2:
                T[i][j] = 0'''

            if T[i][j] < D:
                T[i][j] = 0

            elif K[i] == 'G' and K[j] == 'B':
                T[i][j] = 1

            else:
                T[i][j] = 0

    T.append([0]*(n+2))
    T.append([0]*(n+2))

    for i in range(n):
        T[i].append(0)
        T[i].append(0)

    for i in range(n):
        if K[i] == 'G':
            T[n][i] = 1
        else:
            T[i][n+1] = 1
    print(T)
    #return edmonds_karp(T,n,n+1)

#runtests( BlueAndGreen )
T = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]
K = ['B', 'B', 'G', 'G', 'B']
D = 2
print(BlueAndGreen(T,K,D))
