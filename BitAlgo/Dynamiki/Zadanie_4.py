def minimum_cost(T):
    answer=[[0 for _ in range(len(T[0]))] for i in range(len(T))]
    path=[[-1 for _ in range(len(T[0]))] for i in range(len(T))]
    answer[0][0]=T[0][0]
    for i in range(1,len(T[0])):
        answer[0][i]=answer[0][i-1]+T[0][i]
        path[0][i]=0
    for i in range(1, len(T)):
        answer[i][0]=answer[i-1][0]+T[i][0]
        path[i][0]=1
    
    for i in range(1,len(T)):
        for j in range(1,len(T[0])):
            if(answer[i-1][j]<answer[i][j-1]):
                answer[i][j]=answer[i-1][j]+T[i][j] # zabrane z gory
                path[i][j]=1
            else:
                answer[i][j]=answer[i][j-1]+T[i][j]
                path[i][j]=0

    x=len(T[0])-1
    y=len(T)-1
    while x>0 or y>0:
        print(T[y][x])
        if path[y][x]==1:
            y-=1
        else:
            x-=1
    return answer[len(T)-1][len(T[0])-1]


if __name__=="__main__":
    tablica=[[1,2,3,4],[1,2,3,4],[6,7,8,1],[8,8,8,8],[8,9,8,9]]
    print(minimum_cost(tablica))