from queue import Queue

def longest_path(T,s):
    tab= [[-1 for _ in range(len(T[0]))] for i in range(len(T))]
    path=[[ (0,0) for _ in range(len(T[0]))] for i in range(len(T))]
    tab[s[0]][s[1]]=1
    Q=Queue()
    Q.put((s[0],s[1]))
    while not Q.empty():
        p=Q.get()
        x=p[0]
        y=p[1]
        if x-1>=0 and T[x-1][y]>T[x][y] and tab[x-1][y]<tab[x][y]+1:
            tab[x-1][y]=tab[x][y]+1
            path[x][y]=(x-1,y)
            Q.put((x-1,y))

        if x+1<len(T) and T[x+1][y]>T[x][y] and tab[x+1][y]<tab[x][y]+1:
            tab[x+1][y]=tab[x][y]+1
            path[x][y]=(x+1, y)
            Q.put((x+1,y))      

        if y-1>=0 and T[x][y-1]>T[x][y] and tab[x][y-1]<tab[x][y]+1:
            tab[x][y-1]=tab[x][y]+1
            path[x][y]=(x, y-1)
            Q.put((x,y-1))   

        if y+1<len(T[0]) and T[x][y+1]>T[x][y] and tab[x][y+1]<tab[x][y]+1:
            tab[x][y+1]=tab[x][y]+1
            path[x][y]=(x, y+1)
            Q.put((x,y+1))

    i=s[0]
    j=s[1]
    print("Wartości:")
    while i!=x or j!=y:
        print(T[i][j], end=' ')
        i, j = path[i][j]
    print(T[x][y])
    return tab[x][y]


if __name__=="__main__":
    tablica=[[5,4,3,1],[-1,1,2,2],[3,2,0,3]]
    n=longest_path(tablica,[1,1])
    print()
    print("Odpowiedź: ", n)
    