from zad2testy import runtests

def partition(tab, p, k, jak):
    l=p
    if jak==0:
        for i in range(p,k):
            if tab[i][0]<=tab[k][0]:
                tab[i], tab[l] = tab[l], tab[i]
                l+=1
    else:
        for i in range(p,k):
            if tab[i][1]<tab[k][1]:
                tab[i], tab[l] = tab[l], tab[i]
                l+=1
            elif tab[i][1]==tab[k][1] and tab[i][0]<=tab[k][0]:
                tab[i], tab[l] = tab[l], tab[i]
                l+=1
    tab[l], tab[k] = tab[k], tab[l]
    return l


def quicksort(tab,p,k, jak):
    if p<k:
        q=partition(tab, p, k, jak)
        quicksort(tab, p, q-1, jak)
        quicksort(tab, q+1, k, jak)

def znajdz_koniec(L, wartosc,poczatek, p, k):
    
    while p<=k:
        sr=(p+k)//2
        if wartosc<L[sr][1]:
            k=sr-1
        elif wartosc>L[sr][1]:
            p=sr+1
        else:
            srodek=sr
            while(srodek<len(L) and L[srodek][1]==wartosc):
                if L[srodek][0]==poczatek:
                    return srodek
                srodek+=1
            srodek=sr
            while srodek>=0 and L[srodek][1]==wartosc:
                if L[srodek][0]==poczatek:
                    return srodek
                srodek-=1
            
    
    
def depth(L):
    quicksort(L, 0, len(L)-1, 0)
    # koniec=[L[i] for i in range(len(L))]
    # quicksort(koniec, 0, len(koniec)-1, 1)
    # maks=0
    # aktualnie=0
    # for i in range(len(L)):
    #     aktualnie=znajdz_koniec(koniec,L[i][1], L[i][0], 0, len(L)-1)
    #     maks=max(maks, aktualnie-i+1)
    # #print(L)
    # #print(koniec)
    # #print(maks)
    # return maks

runtests( depth ) 
