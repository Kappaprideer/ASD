# Andrzej Zaborniak

# buildings - tablica zawierajaca 5-cio elementowe tablice [ (0_poczatek, 1_koniec, 2_ilosc_studentow, 3_koszt, 4_miejsce w tablicy T )]
# posortowana względem początków przedziałów, a w przypadku identycznych początków, posortowana po końcach przedziałów

# funkcja g(i,x,G,buildings) zwraca największą liczbę studentów jaka może mieszkać w akademikach o indeksach mniejszych od i, zawsze wliczając do tego
# akademik na indeksie i; łączny koszt tych akedemików jest mniejszy lub równy x. 
# Dla wartości skrajnych: jeśli x jest większy lub równy cenie akademika to w tablicy wpisywana jest liczba studentów mogąych zamieszkać w tym akademiku, w przeciwnym
# wypadku do komórek wpisywane jest zero

# Po znalezieniu indeksu "xyz" akademika którego łączna liczba studentów jest największa symuluje się dodwawanie kolejnych akdemików. Cofając się w tył od znalezionego indeksu
# "xyz" sprawdzając czy liczba_studentów - liczba_studentów_w_akademiku_xyz oraz budżet-cena_akademika_xyz są takie same w tablicy G oraz czy budynek kończy się przed
# początkiem budynku xyz.

# G[i][j] - tablica w której przechowywane są wartości zwracane przez g dla danego akademika na pozycji i oraz łacznym maksymalnym koszcie j

from zad4testy import runtests

def g(i,x,G, tab):
    if G[i][x] != -1:
        return G[i][x]
    maksymalne=0
    if tab[i][3]<=x:
        maksymalne=tab[i][2]
    for j in range(i-1,-1,-1):
        if x-tab[i][3]>=0 and tab[j][1]<tab[i][0]:
            maksymalne=max(maksymalne,tab[i][2]+g(j,x-tab[i][3], G, tab))
    G[i][x]=maksymalne
    return maksymalne


def select_buildings(T,p):
    n=len(T)
    buildings=[[0,0,0,0,0] for _ in range(n)]
    for i in range(n):
        buildings[i][0] = T[i][1]
        buildings[i][1] = T[i][2]
        buildings[i][2] = (T[i][2]-T[i][1])*T[i][0]
        buildings[i][3] = T[i][3]
        buildings[i][4] = i        
    buildings.sort(key=lambda pair: pair[1])
    buildings.sort(key=lambda pair: pair[0])

    G=[[-1 for q in range(p+1)] for _ in range(n)]
    for i in range(p+1):
        G[0][i]=0
    for i in range(buildings[0][3], p+1):
        G[0][i]=buildings[0][2]
    
    maksymalnie=0
    odpowiedz=0

    for j in range(n-1,-1,-1):
        G[j][p]=g(j,i,G,buildings)
        if G[j][p]>maksymalnie:
            maksymalnie = G[j][p]
            odpowiedz=j
    
    
    result=[]
    ostatni=odpowiedz
    result.append(buildings[odpowiedz][4])
    maksymalnie-=buildings[odpowiedz][2]
    price=p-buildings[odpowiedz][3]
    for indeks in range(odpowiedz, -1, -1):
        if maksymalnie==G[indeks][price] and price>=0 and maksymalnie-buildings[indeks][2]>=0 and buildings[indeks][1]<buildings[ostatni][0]:
            ostatni=indeks
            result.append(buildings[indeks][4])
            maksymalnie-=buildings[indeks][2]
            price-=buildings[indeks][3]
    

    return result

runtests( select_buildings )
