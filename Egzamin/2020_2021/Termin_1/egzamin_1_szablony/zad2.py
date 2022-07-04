from zad2testy import runtests
from queue import PriorityQueue

def robot( L, A, B ):
#   0- robocik po obrocie, 1- robocik przejechał pierwszy raz w przod, 2- robocik jedzie drugi raz w przod lub wiecej, ---- roz (rozpędzenie robocika)
#   czas, y, x ,kierunek, rozpędzenie, wartosc z ktorej wyjezdza      ---- wartości wkładane do kolejki piorytetowej
#   0 - prawo, 1 - dół, 2 - lewo, 3 - góra                            ---- kierunek 
    Q=PriorityQueue()
    T=[[[10**10 for _ in range(len(L[0]))] for i in range(len(L))]for ha in range(4)]
    T[0][A[1]][A[0]]=0
    Q.put((0,A[1],A[0],0,0,0))
    for i in range(1,3):
        Q.put((45*i,A[1],A[0],i,0,0))
    Q.put((45,A[1],A[0],3,0,0))
    
    while not Q.empty():
        time, y, x, kierunek, roz, beginning = Q.get()
        if time+beginning<=T[kierunek][y][x]:
            T[kierunek][y][x]=time+beginning

            if kierunek==0 and L[y][x+1]!='X':
                if roz==0 and T[kierunek][y][x+1]>T[kierunek][y][x]+60:
                    Q.put((60,y,x+1,kierunek,1,T[kierunek][y][x]))
                elif roz==1 and T[kierunek][y][x+1]>T[kierunek][y][x]+40:
                    Q.put((40,y,x+1,kierunek,2,T[kierunek][y][x]))
                elif roz==2 and T[kierunek][y][x+1]>T[kierunek][y][x]+30:
                    Q.put((30,y,x+1,kierunek,2,T[kierunek][y][x]))

            if kierunek==1 and L[y+1][x]!='X':
                if roz==0 and T[kierunek][y+1][x]>T[kierunek][y][x]+60:
                    Q.put((60,y+1,x,kierunek,1,T[kierunek][y][x]))
                elif roz==1 and T[kierunek][y+1][x]>T[kierunek][y][x]+40:
                    Q.put((40,y+1,x,kierunek,2,T[kierunek][y][x]))
                elif roz==2 and T[kierunek][y+1][x]>T[kierunek][y][x]+30:
                    Q.put((30,y+1,x,kierunek,2,T[kierunek][y][x]))

            if kierunek==2 and L[y][x-1]!='X':
                if roz==0 and T[kierunek][y][x-1]>T[kierunek][y][x]+60:
                    Q.put((60,y,x-1,kierunek,1,T[kierunek][y][x]))
                elif roz==1 and T[kierunek][y][x-1]>T[kierunek][y][x]+40:
                    Q.put((40,y,x-1,kierunek,2,T[kierunek][y][x]))
                elif roz==2 and T[kierunek][y][x-1]>T[kierunek][y][x]+30:
                    Q.put((30,y,x-1,kierunek,2,T[kierunek][y][x]))

            if kierunek==3 and L[y-1][x]!='X':
                if roz==0 and T[kierunek][y-1][x]>T[kierunek][y][x]+60:
                    Q.put((60,y-1,x,kierunek,1,T[kierunek][y][x]))
                elif roz==1 and T[kierunek][y-1][x]>T[kierunek][y][x]+40:
                    Q.put((40,y-1,x,kierunek,2,T[kierunek][y][x]))
                elif roz==2 and T[kierunek][y-1][x]>T[kierunek][y][x]+30:
                    Q.put((30,y-1,x,kierunek,2,T[kierunek][y][x]))

            if roz!=0:
                for i in range(1,3):
                    Q.put((45*i,y,x,(kierunek+i)%4,0,T[kierunek][y][x]))
                Q.put((45,y,x,(kierunek+3)%4,0,T[kierunek][y][x]))

    odp=10**10
    for i in range(4):
        odp=min(odp,T[i][B[1]][B[0]])
    if odp<10**10:
        return odp
    return None
    
runtests( robot )


