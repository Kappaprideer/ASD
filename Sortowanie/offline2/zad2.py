from zad2testy import runtests

def partition_poczatki(T, p, k):
    l=p-1
    for i in range(p,k):
        if T[i][0]<=T[k][0]:
            if T[i][0]==T[k][0]:
                if T[i][1]>=T[k][1]:
                    l+=1
                    T[i],T[l]=T[l],T[i]
            else:
                l+=1
                T[i],T[l]=T[l],T[i]
    T[l+1], T[k] = T[k], T[l+1]
    return l+1

def quicksort_poczatki(T, p, k):
    while p<k:
        q=partition_poczatki(T, p, k)
        quicksort_poczatki(T,p,q-1)
        p=q+1

def partition_konce(T,p,k):
    l=p-1
    for i in range(p,k):
        if T[i][1]<=T[k][1]:
            l+=1
            T[i],T[l]=T[l],T[i]
    T[l+1], T[k] = T[k], T[l+1]
    return l+1

def quicksort_konce(T, p, k):
    while p<k:
        q=partition_konce(T, p, k)
        quicksort_konce(T, p, q-1)
        p=q+1

def depth(L):
    n=len(L)
    konce=[L[i] for i in range(n)]
    quicksort_poczatki(L, 0, n-1)
    quicksort_konce(konce, 0, n-1)
    print(L)
    print(konce)
    k=0
    p=0
    licz=0
    wynik=0
    while k<=p and k<n and p<n:
        if p+1<n and konce[p+1][1] <= L[k][1]:
            licz+=1
            p+=1
            wynik=max(wynik, licz)
        else:
            koniec=L[k][1]
            while k<n and L[k][1] <= koniec:
                licz-=1
                k+=1
    return wynik



runtests( depth ) 
