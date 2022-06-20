# Andrzej Zaborniak 410704

# Program dostaje wyrazy, nastepnie segreguje wyrazy do osobnych bucketow, jeden bucket to dlugosc wyrazu, nastepnie funkcja przechodzi
# po bucketach posiadajacych wiecej niz jeden wyraz, w nich litery w wyrazie sa sortowane, lecz nie sa ponownie zapisane w postaci slow 
# tylko wartosci z tablicy ascii, nastepnie wyrazy sa sortowane leksykograficznie za pomoca radix sort
# czyli jesli wyrazy byly anagramami to wartosci w tablicach w poszczegolnych polach beda takie same, a dzieki sortowaniu 
# leksykograficznemu wyrazy beda obok siebie. Nastpenie przechodze po posortowanych wyrazach zapisanych w liczbach ascii sprawdzajac czy 
# tablice sa rozne, jesli sa takie same to znaczy ze wyrazy sa popularno anagramowe. Zwracam najwieksza liczbe takich samych tablich. 
# Program sortuje do poszczegolnych bucketow wyrazy w czasie O(k) z czego k to liczba wyrazow w T, nastpenie counting sort sortuje poszczegolne
# wyrazy w tablicy w czasie O(d) z czego d jest dlugoscia wyrazow, sortowanie radix sortem odbywa sie w zlozonosci O(kd) oraz na samym koncu 
# przechodze po kazdym elemencie dwukrotnie badajac czy sa takie same. Finalnie alogrytm zajmuje czas O(n) 
# Nie zdążyłem napisać radix sort



from kol1btesty import runtests



# def radix_sort(tablica):
#     liczby=[ 0 for _ in range(27)]
#     n=len(tablica[0])

#     for x in range(len(n-1)):
#         for i in range(len(tablica)-1, -1, -1):
#             for j in range(n-1):

def radix_sort(tablica):
    n=len(tablica[0])
    odp=[ [] for _ in range(len(tablica))]
    for key in range(n-1,-1,-1):
        A=[0 for _ in range(27)]
        for i in range(len(tablica)):
            A[tablica[i][key]]+=1
        for i in range(1,27):
            A[i]+=A[i-1]
        for i in range(len(tablica)-1,-1,-1):
            odp[A[tablica[i][key]]-1]=tablica[i]
            A[tablica[i][key]]-=1
        tablica=odp
    return odp


def sortowanie_wyrazow(tablica):
    result=[]
    # wynik=[ 0 for _ in range(len(tablica[0]))]
    for wyraz in tablica:

        alfabet=[0 for i in range(27)]
        for znak in range(len(wyraz)):
            alfabet[ord(wyraz[znak])-ord('a')]+=1


        for i in range(1, 27):
            alfabet[i]+=alfabet[i-1]

        
        wynik=[ 0 for _ in range(len(tablica[0]))]
        for i in range(len(wyraz)-1, -1, -1):
            wynik[alfabet[ord(wyraz[i])-ord('a')]-1]=ord(wyraz[i])-ord('a')            
            alfabet[ord(wyraz[i])-ord('a')]-=1
        result.append(wynik)

    tmp=0
    count=0
    inny=False
    result=radix_sort(result)
    for i in range(1, len(result)):
        inny=False
        for j in range(len(result[i])):
            if result[i][j]!=result[i-1][j]:
                inny=True
        
        if not inny:
            tmp+=1
        else:
            tmp=0

        count=max(count, tmp)
        
    return count+1



def f(T):
    najdluzszy=0
    odpowiedz=0

    for i in range(len(T)):
        najdluzszy=max(najdluzszy, len(T[i]))

    dlugosci=[ [] for _ in range(najdluzszy+1)]

    for i in range(len(T)):
        indeks=len(T[i])
        dlugosci[indeks].append(T[i])
    
    for i in range(najdluzszy+1):
        if len(dlugosci[i])>1:
            tmp=sortowanie_wyrazow(dlugosci[i])
            odpowiedz=max(tmp,odpowiedz)

    return odpowiedz


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
