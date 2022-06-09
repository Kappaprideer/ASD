# Andrzej Zaborniak 
# Program na początku tworzy nową tablice zwierającą elementy z tablicy P z dopisanymi indeksami pierwotnymi, następnie tablica ,,punkty" jest sortowana względem 
# punktów na tracie. Tablica "przesiadki" zaiwera przesiadki[i]=[element na trasie][ilepunktw kontrolnych do elementu ,,i,,][indeks pierwotny]
# funkcja f[i] zwraca ile najmniej punktow kontrolnych moze przejechać marcin do elementu na trasie w odleglosci ,,i,, od początku 


from kol2atesty import runtests

def drivers( P, B ):
    punkty=[ (P[i][0], P[i][1], i) for i in range(len(P))]
    punkty.sort(key=lambda x: x[0])
    przesiadki=[]
    ile=0
    for i in range(len(punkty)):
        if punkty[i][1]==True:
            przesiadki.append([i,ile, punkty[i][2]])
            ile=0
        else:
            ile+=1

    zmiany=[ -1 for i in range(len(przesiadki))]

    # przesiadki[i][ odległość, ile punktowkontrolnych, numer w tablicy]
    f=[0 for _ in range(len(przesiadki))]

    for i in range(1,len(przesiadki)):
        q=10**10
        for j in range(i-1,max(-1,i-5),-1):
            if f[j]<=q:
                q=f[j]
                zmiany[i]=j
        f[i]=q+przesiadki[i][1]

    y=0
    while y<len(przesiadki) and przesiadki[y][0]<=B :
        y+=1
    y-=1

    for i in range(y-1,max(-1,y-5),-1):
        if f[i]<f[y]:
            y=i

    odp=[]

    while y-1>=0:
        odp.append(przesiadki[y][2])
        odp.append(przesiadki[y-1][2])
        y=zmiany[y]
        
    print(f)
    print(zmiany)

    

    return odp

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )