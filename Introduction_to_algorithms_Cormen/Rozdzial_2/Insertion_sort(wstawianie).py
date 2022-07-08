def Insertion_Sort(T):
    n=len(T)
    for j in range(1,n):
        klucz=T[j]
        i=j-1
        while i>=0 and klucz<T[i]:
            T[i+1]=T[i]
            i-=1
        T[i+1]=klucz
        


if __name__=="__main__":
    tablica=[12,11,10,9,8,7,6,5,4,3,2,180,1,55,76,4,2]
    print("Tablica przed posortowaniem:", tablica)
    Insertion_Sort(tablica)
    print("\n Tablica po posrotowaniu", tablica)