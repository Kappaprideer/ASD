#zabieram do heap-a k+1 elementów, ponieważ musi się w nim znajdować minimum, następnie zabieram pierwszy element, tylko czy przenosic wskaźnik 
#do tablicy przez referencje gdzie trzymać tą tablice ze stosem

import random
import time


class Node():
    def __init__(self, val):
        self.val=val
        self.next=None
def printing(first):
    p=first
    while p is not None:
        print("-->", p.val, end=" ")
        p=p.next
    print("\n")
def make_linked_list(tab):
    n=len(tab)
    head=None
    for i in range(n-1, -1, -1):
        tmp=Node(tab[i])
        tmp.next=head
        head=tmp
    return head



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
    k+=1        #kopiec zaczyna się od 1 i ma k+1 elementów
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
            #if first:
             #   first=False
            #else:
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
    



    



if __name__=="__main__":
    n=int(input("Podaj dlugosc tablicy: "))
    k=int(input("Podaj k: "))
    tablica=[]
    for i in range(n):
        tablica.append(random.randint(i, i+k))
    
    head=make_linked_list(tablica)

    #printing(head)
    start=time.time()

    head=SortH(head, k)

    end=time.time()
    print("Czas dzialania algorytmu: ",end-start)
    
    #printing(head)

