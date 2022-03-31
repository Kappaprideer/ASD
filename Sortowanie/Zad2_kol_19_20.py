def partition(T,p,k):
    l=p
    for i in range(p, k):
        if T[i]<T[k]:
            T[i], T[l] = T[l], T[i]
            l+=1
    T[k], T[l] = T[l], T[k]
    return l

def select(T,left, right, k):
    while True:
        q=partition(T,left, right)
        if q==k:
            return 
        if q<k:
            left=q+1
        else:
            right=q-1
    
def quicksort(T, l, p):
    if l<p:
        q=partition(T, l, p)
        quicksort(T,l,q-1)
        quicksort(T,q+1, p)






def section(T,p,q):
    select(T, 0, len(T)-1, p)
    select(T, 0, len(T)-1, q)
    quicksort(T,p,q)



if __name__=="__main__":
    tablica=[8,19,24,5,10,1,15,26,14,3,5,123,33,22,17]
    tab=[12,11,10,9,8,7,6,5,4,3,2,1]
    section(tablica, 0, len(tablica)-5)
    print(tablica)