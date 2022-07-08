from zad4ktesty import runtests

def falisz ( T ):
    tab= [ [ 0 for _ in range(len(T))] for i in range(len(T))]
    for i in range(1,len(T)):
        tab[0][i]=T[0][i]+tab[0][i-1]
        tab[i][0]=T[i][0]+tab[i-1][0]

    for i in range(1,len(T)):
        for j in range(1,len(T)):
            tab[i][j]=min(tab[i-1][j], tab[i][j-1])+T[i][j]
    
    return tab[len(T)-1][len(T)-1]

runtests ( falisz )
