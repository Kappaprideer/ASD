from zad1testy import runtests

def Partition(T,p,k):
    n=len(T)
    pivot=T[k//n][k%n]
    count=p
    for i in range(p, k):
        if T[i//n][i%n]<=pivot:
            T[count//n][count%n], T[i//n][i%n] = T[i//n][i%n], T[count//n][count%n]
            count+=1
    T[count//n][count%n], T[k//n][k%n] = T[k//n][k%n], T[count//n][count%n]
    return count

def Quick_select(T,left, position):
    n=len(T)
    right=(len(T)*len(T))-1
    while True:
        q=Partition(T, left, right)
        if q==position:
           return T[q//n][q%n], q
        elif q<position:
            left=q+1
        else:
            right=q-1
    
def Under_diagonal(T, value):
    n=len(T)
    left=[1,0]
    for i in range(1,(n*n)-1):
        x=i//n
        y=i%n
        while x<y and T[x][y]<=value and left[0]<n:  # elementry pod przekotana maja pierwsza wartosc wieksza od drugiej 
            if left[0]==left[1]:
                left[0]+=1
                left[1]=0
            T[x][y], T[left[0]][left[1]] = T[left[0]][left[1]], T[x][y]
            left[1]+=1

def Above_diagonal(T, value):
    n=len(T)
    diagonal=1
    for i in range(1,(n*n)-1):
        x=i//n
        y=i%n
        while x<y and T[x][y]<value and diagonal<n-1:  # elementry pod przekotana maja pierwsza wartosc wieksza od drugiej 
             T[x][y], T[diagonal][diagonal] = T[diagonal][diagonal], T[x][y]
             diagonal+=1
             



def Median(T):
    n=len(T)
    min_diagonal, x=Quick_select(T,0, (((n*n)-n)//2))
    T[x//n][x%n] , T[0][0] = T[0][0], T[x//n][x%n]
    max_diagonal, x=Quick_select(T,1, (((n*n)-n)//2)+n-1)
    T[x//n][x%n] , T[n-1][n-1] = T[n-1][n-1], T[x//n][x%n]
    Under_diagonal(T, min_diagonal)
    Above_diagonal(T, max_diagonal)

    
    # for chuj in T:
    #     print(chuj)
    
    return 


# if __name__=="__main__":
#     tablica=[[43, 74, 53, 97],[80, 61, 61, 19],[61, 73, 89, 93],[42, 17, 89, 80]]
#     Median(tablica)


runtests( Median ) 
