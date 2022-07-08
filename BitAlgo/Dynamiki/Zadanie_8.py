def palindrom(T):
    n=len(T)
    F =  [[0 for _ in range(n)] for q in range(n)]
    for i in range(n):
        F[i][i]=1
    for i in range(1,n):
        if T[i-1]==T[i]:
            F[i-1][i]=1
    ind_1=0
    ind_2=0
    maximum=-1000
    for x in range(1,n):
        for y in range(x,n):
            i=y-x
            j=y
            if T[i]==T[j] and F[i+1][j-1]==1:
                F[i][j]=1
                if j-i+1>maximum:
                    maximum=j-i+1
                    ind_1=i
                    ind_2=j

    return T[ind_1:ind_2+1]

if __name__=='__main__':
    napis='aaaccaababa'
    print(palindrom(napis))