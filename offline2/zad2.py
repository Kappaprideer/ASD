from zad2testy import runtests


def depth(L):
    n=len(L)
    current=0
    maks=0
    for i in range(n):
        current=0
        for j in range(n):
            if i!=j and L[j][0]>=L[i][0] and L[j][1]<=L[i][1]:
                current+=1
                maks=max(maks, current)
    return maks


runtests( depth ) 
