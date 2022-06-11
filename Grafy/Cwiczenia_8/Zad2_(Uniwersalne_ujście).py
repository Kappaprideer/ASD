def uniwersalne_ujście(G):
    n=len(G)
    i=0
    j=0
    while i<n:
        if G[j][i]==0:
            i+=1
        else:
            j+=1
    for x in range(n):
        if G[j][x]==1:
            return None
        if G[x][j]==0 and x!=j:
            return None
    return j

if __name__=="__main__":
    G=[
    [0,0,1,1,0],
    [1,0,1,0,0],
    [0,0,0,0,0],
    [0,0,1,0,1],
    [1,1,1,0,0]
    ]

    print(uniwersalne_ujście(G))