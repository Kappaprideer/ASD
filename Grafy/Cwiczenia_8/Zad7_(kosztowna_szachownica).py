from collections import deque

def kingpath(G):
    n=len(G)
    visited=[[0 for _ in range(n)] for i in range(n)]
    c=[[10**10 for _ in range(n)] for i in range(n)]

    visited[0][0]=0
    c[0][0]=G[0][0]
    Q=deque()
    Q.append((0,0))
    move=[ (1,1),(1,0),(0,1),(1,-1),(-1,1),(-1,-1),(-1,0),(0,-1)]

    while len(Q)>0:
        s=Q.popleft()
        for m in move:
            x=s[0]+m[0]
            y=s[1]+m[1]
            if x>=0 and x<n and y>=0 and y<n:
                if visited[x][y]==1 and c[x][y]>c[x-m[0]][y-m[1]]+G[x][y]:
                    c[x][y]=c[x-m[0]][y-m[1]]+G[x][y]
                    Q.append((x,y))
                elif visited[x][y]==0:
                    c[x][y]=c[x-m[0]][y-m[1]]+G[x][y]
                    visited[x][y]=1
                    Q.append((x,y))    
    
    for line in c:
        print(line)
    print()
    return c[n-1][n-1]
        

if __name__=="__main__":
    G=[
    [1,1,7,10,0,0],
    [5,6,1,2,11,5],
    [2,20,1,1,7,7],
    [5,3, 1,4,3,6],
    [1,1,10,10,10,1],
    [1,1,1,1,1,1]
    ]    
    print(kingpath(G))