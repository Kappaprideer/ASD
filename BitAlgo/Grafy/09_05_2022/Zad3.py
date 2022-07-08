# Dana tablica z literami "W" jeśli w danej kratce znajduje się woda, oraz "L" jeśli ląd.
# a) Policz ile jezior jest w tablicy
# b) Policz ile komórek zawiera największe jezioro
# c) Czy istnieje ścieżka od (0,0) do (n-1,m-1)
# d) Wypisz najkrótszą ściężke od (0,0) do (n-1,m-1)

from collections import deque

def array_modifier(G):
    tab=[ [ 0 for _ in range(len(G[0]))] for i in range(len(G))]
    return tab

def DFS_filler(G,K,i,j):
    K[i][j]=1
    if i>0 and G[i-1][j]==5 and K[i-1][j]==0:
        DFS_filler(G,K,i-1,j)
    if j>0 and G[i][j-1]==5 and K[i][j-1]==0:
        DFS_filler(G,K,i,j-1)
    if i<len(G)-1 and G[i+1][j]==5 and K[i+1][j]==0:
        DFS_filler(G,K,i+1,j)
    if j<len(G[0])-1 and G[i][j+1]==5 and K[i][j+1]==0:
        DFS_filler(G,K,i,j+1)

def a(G):
    K=array_modifier(G)
    number_of_lakes=0
    for i in range(len(G)):
        for j in range(len(G[0])):
            if K[i][j]==0 and G[i][j]==5:
                number_of_lakes+=1
                DFS_filler(G,K,i,j)
    return number_of_lakes

def b(G):
    visited=array_modifier(G)
    Q=deque()
    answer=0
    for i in range(len(G)):
        for j in range(len(G[0])):
            if visited[i][j]==0 and G[i][j]==5:
                Q.append((i,j))
                count=0
                visited[i][j]=1
                while len(Q)>0:
                    x,y = Q.popleft()
                    count+=1
                    if x>0 and G[x-1][y]==5 and visited[x-1][y]==0:
                        Q.append((x-1,y))
                        visited[x-1][y]=1
                    if y>0 and G[x][y-1]==5 and visited[x][y-1]==0:
                        Q.append((x,y-1))
                        visited[x][y-1]=1
                    if x<len(G)-1 and G[x+1][y]==5 and visited[x+1][y]==0:
                        Q.append((x+1,y))
                        visited[x+1][y]=1
                    if y<len(G[0])-1 and G[x][y+1]==5 and visited[x][y+1]==0:
                        Q.append((x,y+1))
                        visited[x][y+1]=1
                
                answer=max(answer,count)

    return answer

def c(G):
    exist=False
    visited=array_modifier(G)
    parent = [ [ [0,0] for _ in range(len(G[0]))] for x in range(len(G))]
    def path(G,i,j):
        nonlocal exist
        nonlocal visited
        nonlocal parent
        if exist==False:
            if i==len(G)-1 and j==len(G[0])-1:
                exist=True
            else:
                if i>0 and G[i-1][j]==7 and visited[i-1][j]==0 and not exist:
                    visited[i-1][j]=1
                    parent[i-1][j]=[i,j]
                    path(G,i-1,j)

                if j>0 and G[i][j-1]==7 and visited[i][j-1]==0 and not exist:
                    visited[i][j-1]=1
                    parent[i][j-1]=[i,j]
                    path(G,i,j-1)

                if i<len(G)-1 and G[i+1][j]==7 and visited[i+1][j]==0 and not exist:
                    visited[i+1][j]=1
                    parent[i+1][j]=[i,j]
                    path(G,i+1,j)

                if j<len(G[0])-1 and G[i][j+1]==7 and visited[i][j+1]==0 and not exist:
                    visited[i][j+1]=1
                    parent[i][j+1]=[i,j]
                    path(G,i,j+1)

            visited[i][j]=0

        
    visited[0][0]=1
    path(G,0,0)
    
    P=[[len(G)-1,len(G[0])-1]]
    x=len(G)-1
    y=len(G[0])-1

    if exist:
        while x!=0 or y!=0:
            P.append(parent[x][y])
            x, y = parent[x][y]
    P=P[::-1]
    return exist, P



if __name__=="__main__":
    # "W" 5 
    # "L" 7
    G = [ 
    [7,5,7,7,7,7,7,7,7],
    [7,5,7,5,5,7,7,7,7],
    [7,7,7,5,5,7,7,7,7],
    [7,5,5,5,5,7,5,7,7],
    [7,7,5,5,7,7,5,7,7],
    [7,5,7,7,7,7,5,5,7],
    [5,5,7,5,5,7,7,7,7],
    [7,7,7,5,7,7,7,7,7]]
    print("a:", a(G))
    print()
    print("b:", b(G))
    print()
    istnieje , path = c(G)
    print("Czy istnieje sciezka po ladzie od (0,0) do (n-1,m-1):", istnieje)
    print("Ścieżka do pola n-1,m-1:")
    for line in path:
        print(line)