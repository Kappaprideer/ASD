from zad1testy import runtests
from queue import PriorityQueue
from math import inf

def merge(T,p,m,k):
    L=T[p:m+1]
    R=T[m+1:k+1]
    L.append((inf,inf))
    R.append((inf,inf))
    i=j=0
    for k in range(p,k+1):
        if L[i][0]<=R[j][0]:
            T[k]=L[i]
            i+=1
        else:
            T[k]=R[j]
            j+=1

def merge_sort(T,p,k):
    if len(T)<=1:
        return T
    if p<k:
        m=(p+k)//2
        merge_sort(T,p,m)
        merge_sort(T,m+1,k)
        merge(T,p,m,k)



def chaos_index( T ):
    for i in range(len(T)):
        T[i]=(T[i],i)
    merge_sort(T,0,len(T)-1)
    ans=-1
    for i in range(len(T)):
        ans=max(ans,abs(i-T[i][1]))
    return ans

runtests( chaos_index )
