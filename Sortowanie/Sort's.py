from heapq import heapify
import random
from termios import NL1
HOW_MANY=15
HOW_MUCH=100

def Insertion_sort(T):      #sortowanie przez wstawianie 
    n=len(T)
    for i in range(1,n):
        klucz=T[i]
        j=i-1
        while j>=0 and T[j]>klucz:
            T[j+1]=T[j]
            j-=1
        T[j+1]=klucz

def Selection_sort(T):      #sortowanie przez wybieranie
    n=len(T)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if T[j]<T[min_index]:
                min_index=j
        T[min_index], T[i] = T[i], T[min_index]

def Bubble_sort(T):         #sortowanie bombelkowe
    n=len(T)
    for i in range(n):
        for j in range(n-1-i):  
            if T[j]>T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]

def Merge(T, p, q, k):
    n1=q-p+1
    n2=k-q
    lewa=[T[p+i] for i in range(n1)]
    prawa=[T[q+i+1] for i in range(n2)]
    i=0
    j=0
    for x in range(p, k+1):
        if i<n1 and j<n2:
            if lewa[i]<prawa[j]:
                T[x]=lewa[i]
                i+=1
            else:
                T[x]=prawa[j]
                j+=1
        elif i<n1:
            T[x]=lewa[i]
            i+=1
        elif j<n2:
            T[x]=prawa[j]
            j+=1

def Merge_sort(T, p, k):    #sortowanie przez scalanie
    if p<k:
        q=(p+k)//2
        Merge_sort(T, p, q)
        Merge_sort(T, q+1, k)
        Merge(T,p,q,k)

def Partition(T, p, k):
    left=p
    for i in range(p,k):
        if T[i]<T[k]:
            T[i], T[left] = T[left], T[i]
            left+=1

    T[left], T[k] = T[k], T[left]
    return left

def Quick_sort(T, p, k):    #sortowanie Quicksortem
    if p<k:
        q=Partition(T, p, k)
        Quick_sort(T,p, q-1)
        Quick_sort(T,q+1, k)

def Counting_sort(T, k):    #sortowanie przez zliczanie
    n=len(T)
    A=[0 for _ in range(k)]
    B=[0 for _ in range(n)]
    for i in range(n):
        A[T[i]]+=1
    for i in range(1,k):
        A[i]+=A[i-1]
    for i in range(n-1, -1, -1):
        B[A[T[i]]-1]=T[i]
        A[T[i]]-=1
    for i in range(n):
        T[i]=B[i]

def Heapify(T,el,dl):
    maximum=el
    if (el*2)+1<=dl and T[(el*2)+1]>T[maximum]:
        maximum=(el*2)+1
    if (el*2)+2<=dl and T[(el*2)+2]>T[maximum]:
        maximum=(el*2)+2
    if maximum!=el:
        T[maximum], T[el] = T[el], T[maximum]
        Heapify(T,maximum,dl)

def Make_heap(T):
    n=len(T)
    for i in range(n//2, -1, -1):
        Heapify(T,i,n-1)

def Heap_sort(T):           #sortowanie kopcowe 
    Make_heap(T)
    n=len(T)
    for i in range(n-1, -1, -1):
        T[0], T[i] = T[i], T[0]
        Heapify(T,0,i-1)
    






if __name__=="__main__":
    tab=[random.randint(0,HOW_MUCH) for _ in range(HOW_MANY)]
    print("\n",tab, "\n")
    n=len(tab)
    # Insertion_sort(tab)
    # Selection_sort(tab)
    # Bubble_sort(tab)
    # Merge_sort(tab, 0, n-1)
    # Quick_sort(tab, 0, n-1)
    # Counting_sort(tab, HOW_MUCH+1)
    # Heap_sort(tab)

    print(tab, "\n")

