from zad5ktesty import runtests


def garek ( A ):
    n=len(A)
    tab= [ [ 0 for _ in range(n)] for j in range(n)]
    for i in range(n):
        tab[i][i]=A[i]

    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            one=10**10
            two=10**10
            three=10**10
            four=10**10
            if i+1<n and j-1>=0:
                one=tab[i+1][j-1]+A[i]
                three=tab[i+1][j-1]+A[j]
            if i+2<n:
                two=tab[i+2][j]+A[i]
            if j-2>=0:
                four=tab[i][j-2]+A[j]
            one=min(one,two)
            three=min(three,four)
            tab[i][j]=max(one,three)    


    return tab[0][n-1]


runtests ( garek )