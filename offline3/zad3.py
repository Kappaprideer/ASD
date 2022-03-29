from zad3testy import runtests

def SortTab(T,P):
    n = len(T)

    distr = [0]*(n+2)
    for a, b, p in P:
        f = p/(b-a+1)
        distr[a] += f
        distr[b+1] -= f

    for i in range(1, n+2):
        distr[i] += distr[i-1]

    for i in range(1, n+2):
        distr[i] += distr[i-1]

    FACTOR = 7
    buckets = [[] for _ in range(n//FACTOR+1)]

    nfac = n/FACTOR
    for x in T:
        xint = int(x)
        buckets[int( nfac*(distr[xint] + (distr[xint+1]-distr[xint])*(x-xint)) )].append(x)

    for bucket in buckets:
        n = len(bucket)
        
        if n < 2: continue
        if n < 3:
            if bucket[1] < bucket[0]:
                bucket[0], bucket[1] = bucket[1], bucket[0]
            continue

        for i in range(1, n):
            key = bucket[i]
            j = i-1
            while j >= 0 and key < bucket[j]:
                    bucket[j+1] = bucket[j]
                    j -= 1
            bucket[j+1] = key

    return [_ for _ in buckets for _ in _] # Suma wszystkich bucketow




def Insertion_Sort(A):
    n=len(A)
    for i in range(1,n):
        j=i-1
        klucz=A[i]
        while j>=0 and A[j]>klucz:
            A[j+1]=A[j]
            j-=1
        A[j+1]=klucz
    return A


def SortTab(T,P):
    n=len(T)
    B=[[] for _ in range(n+1)]

    for i in range(n):
        ind=int(T[i])
        B[ind].append(T[i])
    
    print(B[1])
    for i in range(1, n+1):
        B[i]=Insertion_Sort(B[i])

    
    k=0
    for i in range(n+1):
        for j in range(len(B[i])):
            T[k]=B[i][j]
            k+=1

    return T

# if __name__=="__main__":
#     T=[1.5, 6.1, 1.2, 3.9, 4.5, 2.5, 3.5, 7.8]
#     T = SortTab(T, [])

runtests( SortTab )