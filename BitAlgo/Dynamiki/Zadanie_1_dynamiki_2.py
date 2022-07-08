# egzamin 2020, I termin 
def su(T,i,j):
    suma=0
    for x in range(i,j+1):
        suma+=T[x]
    return suma



def minimal_absolut(T):
    n=len(T)
    tab=[ [ 0 for _ in range(n)] for i in range(n)]
    for i in range(n-1):
        tab[i][i+1]=abs(T[i]+T[i+1])

    for i in range(0,n):
        for j in range(i+1,n):
            tab[i][j]=max(abs(su(T,i,j)), min( abs(tab[i+1][j]), abs(tab[i][j-1])))
    
    for line in tab:
        print(line)
    return tab[0][n-1]

    


if __name__=="__main__":
    T=[1,-5,2]
    print(minimal_absolut(T))