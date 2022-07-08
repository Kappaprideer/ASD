def Merge(T,poczatek, srodek, koniec):

    n1=srodek-poczatek+1
    n2=koniec-srodek
    
    lewa=[0 for i in range(n1+1)]
    prawa=[0 for i in range(n2+1)]

    for i in range(n1):
        lewa[i]=T[poczatek+i]

    for i in range(n2):
        prawa[i]=T[srodek+i+1]
    
    lewa[n1]=1000000
    prawa[n2]=1000000
    i=0
    j=0
    for k in range(poczatek, koniec+1):
        if lewa[i]<=prawa[j]:
            T[k]=lewa[i]
            i+=1
        else:
            T[k]=prawa[j]
            j+=1
    



def Merge_sort(T,poczatek,koniec):
    if poczatek<koniec:
        srodek=(poczatek+koniec)//2
        Merge_sort(T,poczatek , srodek)
        Merge_sort(T, srodek+1, koniec)
        Merge(T, poczatek, srodek, koniec)



if __name__=="__main__":
    tablica=[10,9,8,7,6,5,4,3,2,1]
    Merge_sort(tablica, 0, len(tablica)-1)
    print(tablica)