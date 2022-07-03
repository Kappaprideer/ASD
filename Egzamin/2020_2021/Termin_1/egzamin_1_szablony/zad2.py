from zad2testy import runtests
from queue import PriorityQueue


def robot( L, A, B ):
#   0- robocik po obrocie, 1- robocik jedzie y raz w przod, 2- robocik jedzie drugi raz w przod, 
#   czas, y, x ,kierunek, rozpędzenie, wartosc z ktorej wxjezdza
    # kierunek = 0 - prawo, 1 - dół, 2 - lewo, 3 - góra 
    # T=[[[10**10 for _ in range(len(L[0]))] for i in range(len(L))] for y in range(4)]
    Q=PriorityQueue()
    T=[[[10**10 for _ in range(len(L[0]))] for i in range(len(L))]for ha in range(4)]
    Q.put((0,A[1],A[0],0,0,0))
    T[0][A[1]][A[0]]=0
    while not Q.empty():
        time, y, x, kierunek, roz, beginning= Q.get()
        if y==B[1] and x==B[0]:
            return beginning+time
        # if T[kierunek][y][x]>beginning+time:
        #     T[kierunek][y][x]=beginning+time
        if kierunek==0 and L[y][x+1]!='X':
            if roz==0 and T[kierunek][y][x+1]>T[kierunek][y][x]+60:
                T[kierunek][y][x+1]+=60
                Q.put((60,y,x+1,kierunek,1,T[y][x]))
            elif roz==1 and T[kierunek][y][x+1]>T[kierunek][y][x]+40:
                Q.put((40,y,x+1,kierunek,2,T[kierunek][y][x]))
            elif roz==2 and T[kierunek][y][x+1]>T[kierunek][y][x]+30:
                Q.put((30,y,x+1,kierunek,2,T[kierunek][y][x]))

        if kierunek==1 and L[y+1][x]!='X':
            if roz==0 and T[kierunek][y][x]>T[kierunek][y][x]+60:
                T[kierunek][y+1][x]+=60
                Q.put((60,y,x+1,kierunek,1,T[kierunek][y][x]))
            elif roz==1 and T[kierunek][y][x+1]>T[kierunek][y][x]+40:
                Q.put((40,y,x+1,kierunek,2,T[y][x]))
            elif roz==2 and T[kierunek][y][x+1]>T[kierunek][y][x]+30:
                Q.put((30,y,x+1,kierunek,2,T[kierunek][y][x]))

        if kierunek==2 and L[y-1][x]!='X':
            if roz==0 and T[kierunek][y-1][x]>T[kierunek][y][x]+60:
                T[kierunek][y-1][x]+=60
                Q.put((60,y-1,x,kierunek,1,T[kierunek][y][x]))
            elif roz==1 and T[kierunek][y-1][x]>T[kierunek][y][x]+40:
                Q.put((40,y-1,x,kierunek,2,T[kierunek][y][x]))
            elif roz==2 and T[kierunek][y-1][x]>T[kierunek][y][x]+30:
                Q.put((30,y-1,x,kierunek,2,T[kierunek][y][x]))

        if kierunek==3 and L[y][x-1]!='X':
            if roz==0 and T[kierunek][y][x-1]>T[kierunek][y][x]+60:
                T[y][x-1]+=60
                Q.put((60,y,x-1,kierunek,1,T[kierunek][y][x]))
            elif roz==1 and T[kierunek][y][x-1]>T[kierunek][y][x]+40:
                Q.put((40,y,x-1,kierunek,2,T[kierunek][y][x]))
            elif roz==2 and T[kierunek][y][x-1]>T[kierunek][y][x]+30:
                Q.put((30,y,x-1,kierunek,2,T[kierunek][y][x]))
        
        for i in range(1,4):
            Q.put((45*i,y,x,(kierunek+i)%4,0,T[kierunek][y][x]))

    return None
    
runtests( robot )


