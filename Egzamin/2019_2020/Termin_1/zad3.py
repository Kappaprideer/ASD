from zad3testy import runtests
import math

def insertion_sort(A):
    for j in range(1,len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
    return A
    
def fast_sort(tab, a):
    T=[[] for _ in range((a*100)+1)]
    for number in tab:
        index=int(number*100)
        T[index].append(number)
    for l in T:
        if len(l)>0:
            insertion_sort(l)
    ans=[]
    for l in T:
        for n in l:
            ans.append(n)
    return ans

runtests( fast_sort )
