from zad3ktesty import runtests

def ksuma( T, k ):
    
    tab=[number for number in T]
    for i in range(k,len(T)):
        tab[i]=T[i]
        minimum=10**10
        for j in range(i-1,i-k-1,-1):
            minimum=min(minimum,tab[j])
        tab[i]+=minimum

    odp=10**10
    for i in range(len(T)-1, len(T)-1-k, -1):
        odp=min(odp,tab[i])
    return odp

    
runtests ( ksuma )