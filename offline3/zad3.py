from zad3testy import runtests

def Insertion_sort(W):
    n=len(W)
    for i in range(1, n):
        klucz=W[i]
        j=i-1
        while j>=0 and W[j]>klucz:
            W[j+1]=W[j]
            j-=1
        W[j+1]=klucz
    return W


def Bucket(A):
    B=[[] for _ in range(10)]

    for x in A:
        ind=int(x*10)%10
        B[ind].append(x)

    for i in range(10):
        if len(B[i])>1:
            B[i]=Insertion_sort(B[i])
    k=0
    for x in B:
        for y in x:
            A[k]=y
            k+=1
    return A   



def Bucket_sort(T):
    n=len(T)
    B=[[] for _ in range(n+1)]

    for i in range(n):
        ind=int(T[i])
        B[ind].append(T[i])
    
    for i in range(1, n+1):
        B[i]=Bucket(B[i])

    z=0
    for i in range(n+1):
        for j in range(len(B[i])):
            T[z]=B[i][j]
            z+=1
    return T


def SortTab(T,P):
    T=Bucket_sort(T)
    return T


# if __name__=="__main__":
#     T=[1.5, 6.1, 1.2, 3.9, 4.5, 2.5, 3.5, 7.8]
#     T = SortTab(T, [])

runtests( SortTab )