# Jak znaleźć ile jest cykli dokładnie 4 wierzchołkowych w grafie reprezentowanym macierzą sąsiedztwa

def how_many_cycle(G):
    n=len(G)
    result=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                if G[i][k]==1 and G[j][k]==1:
                    for z in range(k+1,n):
                        if G[i][z]==1 and G[j][z]==1:
                            result+=1
    return result//2






if __name__=="__main__":
    G=[
    [0,1,0,0,1,0,1],
    [1,0,1,0,0,0,0],
    [0,1,0,0,1,0,1],
    [0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0]
    ]
    print(how_many_cycle(G))