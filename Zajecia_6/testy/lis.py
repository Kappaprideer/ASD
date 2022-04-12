from tests_lis import runtests

def lis(T):
    n=len(T)
    max_indeks=0
    count=[1 for _ in range(n)]
    parent=[ -1 for _ in range(n)]

    for i in range(1,n):
        for j in range(i):
            if T[j]<T[i] and count[j]+1>count[i]:
                count[i]=count[j]+1
                parent[i]=j
        if count[i]>count[max_indeks]:
            max_indeks=i
    return count[max_indeks]

runtests ( lis )