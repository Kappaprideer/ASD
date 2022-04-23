 # Algorytm otrzymuje wskaźnik na pierwszy element linked listy, lista jest k-chaotyczna, czyli pierwszy najmniejszy element może być
# na właściwym miejscu, czyli na pierwszym lub oddalony o co najwyżej k pozycji, czyli zabierając z linked listy k pierwszych elementów najmniejszy element będzie
# już zabrany lub będzie następnym elementem w liście k-chaotycznej. Z zabranych elementów wpisnaych do tablicy tworzy się kopiec minimum, w którym najmniejszy
# element z kopca jest w korzeniu. W kazdym następnym ruchu następuje porównanie czy kolejny najmniejszy element znajduje się w korzeniu kopca, czy jest
# następnym elementem lisy k-chaotycznej. Jeśli jest w liście k-chaotycznej, element zostaje ,,podpięty" do finalnej listy, jeśli zaś znajduje sie w
# korzeniu kopca zostaje on zdjęty a na jego miejsce zostaje wstawiony element z ktorym był porównaywany a następnie ,,zepchnięty" w dół jeśli jest
# większy od swoich synów w kopcu. Na samym końcu przy dojściu do końca listy wejściowej pozostaje wstawić do listy wyjściowej elementy pozostałe w kopcu.
# Algorytm podpina do finalnej listy elementy z korzenia kopca, a następnie zamienia pierwszy element z ostatnim zmeniejszając przy tym wielkość kopca o 1, 
# trochę podobnie jak przy sortowaniu przez kopcowanie.

#złożoność czasowa dla k=1 to O(n)
#złożoność czasowa dla k=logn to O(log(log(n))*n)
#złożoność czasowa dla k=n to O(n*log(k))

from zad1testy import Node, runtests

def min_heap(T, i, n):
    
    lewy=i*2
    prawy=i*2+1
    najmniejszy=i   
    if lewy<n and T[lewy].val<T[i].val:
        najmniejszy=lewy
    if prawy<n and T[prawy].val<T[najmniejszy].val:
        najmniejszy=prawy
    if najmniejszy != i:
        T[i], T[najmniejszy] = T[najmniejszy], T[i]
        min_heap(T, najmniejszy, n)

def SortH(p,k):
    k+=1
    dlugosc=1
    stos=[0 for i in range(k+1)]
    while dlugosc<k and p is not None:
        stos[dlugosc]=p
        p=p.next
        stos[dlugosc].next=None
        dlugosc+=1

    for i in range(dlugosc//2, 0, -1):
        min_heap(stos, i, dlugosc)

    first=True
    if p is not None:
        if stos[1].val<p.val:
            head=stos[1]
            res_current=stos[1]
        else:
            head=p
            res_current=p
            p=p.next
            res_current.next=None
    else:
        head=stos[1]
        res_current=stos[1]

    while p is not None:
        if p.val<stos[1].val:
            res_current.next=p
            res_current=res_current.next
            p=p.next
            res_current.next=None
        else:
            res_current.next=stos[1]
            res_current=res_current.next
            stos[1]=p
            p=p.next
            stos[1].next=None
            min_heap(stos, 1, dlugosc)

    for i in range(1, dlugosc):
        res_current.next=stos[1]
        res_current=res_current.next
        stos[1]=stos[dlugosc-i]
        min_heap(stos, 1, dlugosc-i)

    res_current.next=None
    return head
    

runtests( SortH ) 
