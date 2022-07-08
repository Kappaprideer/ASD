
def Cut_road(T, n):
    count=[0 for _ in range(n+1)]
    wybrane=[-1 for _ in range(n+1)]
    count[0]=0
    for i in range(1,n+1):
        q=-1000000
        for j in range(min(i+1,len(T))):
            if count[i-j]+T[j]>q:
                q=count[i-j]+T[j]
                wybrane[i]=j

        count[i]=q
    g=n
    while g>0:
        print(wybrane[g], end=' ')
        g-=wybrane[g]
    return count[n]



if __name__=="__main__":
    tablica_cen=[0,1,5,8,9,10,17,17,20,24,30]
    dlugosc_preta=4
    print('\n',Cut_road(tablica_cen, dlugosc_preta), sep='')