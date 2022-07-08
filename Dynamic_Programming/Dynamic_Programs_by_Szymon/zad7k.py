from zad7ktesty import runtests 
from collections import deque
def ogrodnik (T, D, Z, l):
    
    litry=[0 for i in range(len(D))]
    visited=[[ 0 for i in range(len(T[0]))] for _ in range(len(T))]
    for i in range(len(D)):
        Q=deque()
        Q.appendleft((0,D[i]))
        visited[0][i]=1
        litry[i]+=T[0][i]
        while len(Q)>0:
            s=Q.pop()
            if s[0]-1>=0 and T[s[0]-1][s[1]]!=0 and visited[s[0]-1][s[1]]==0:
                Q.append((s[0]-1,s[1]))
                visited[s[0]-1][s[1]]=1
                litry[i]+=T[s[0]-1][s[1]]
            if s[0]+1<len(T) and T[s[0]+1][s[1]]!=0 and visited[s[0]+1][s[1]]==0:
                Q.append((s[0]+1,s[1]))
                visited[s[0]+1][s[1]]=1
                litry[i]+=T[s[0]+1][s[1]]

            if s[1]-1>=0 and T[s[0]][s[1]-1]!=0 and visited[s[0]][s[1]-1]==0:
                Q.append((s[0],s[1]-1))
                visited[s[0]][s[1]-1]=1
                litry[i]+=T[s[0]][s[1]-1]

            if s[1]+1<len(T[0]) and T[s[0]][s[1]+1]!=0 and visited[s[0]][s[1]+1]==0:
                Q.append((s[0],s[1]+1))
                visited[s[0]][s[1]+1]=1
                litry[i]+=T[s[0]][s[1]+1]

    n=len(D)
    G=[ [0 for _ in range(l+1)] for i in range(n)]       # maksymalny przychod do drzewa o indeksie "i" i koszcie wody "z" [i][z]
    for j in range(litry[0], l+1):
        G[0][j]=Z[0]
    
    for i in range(l+1):
        for x in range(1,n):
            G[x][i]=G[x-1][i]
            if i-litry[x]>=0:
                G[x][i]=max(G[x][i], G[x-1][i-litry[x]]+Z[x])


    return G[n-1][l]
        


runtests( ogrodnik, all_tests=False )
