from zad3testy import runtests

def lamps( n,T ):
    counter=0
    ans=0
    A=[0 for _ in range(n+1)]
    for tab in T:
        if len(tab)==1:
            A[tab]=(A[tab]+1)%3
            if A[tab]==2:
                counter+=1
            if A[tab]==0:
                counter-=1    
            ans=max(ans,counter)
        else:
            x,y=tab
            ans=max(ans,counter)
            for i in range(x,y+1):
                A[i]=(A[i]+1)%3
                if A[i]==2:
                    counter+=1
                elif A[i]==0:
                    counter-=1
            ans=max(ans,counter)
    return ans

runtests( lamps )


