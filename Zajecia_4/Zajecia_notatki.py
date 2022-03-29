# 1. Posortuj n-elementową tablicę A zawierająca wartości należace do [0, n^2-1] (Złożoność O(n k p ) ) 
# 2. n-elementowa tablica A wartości w A pochodzą ze zbioru B |B| = log(n). Posortuj 

# 1. bazą jest n w radix-sorcie 
def counting (arr, base, key):
    #zliczamy liczbe wystąpień bazy w tablicy

    c= [0 for i in range(base+1)]
    b=[0 for i in range(len(arr))]
    for i in arr:
        c[key(i)]+=1
    
    for i in range(1, len(c)):
        c[i]+=c[i-1]

    for i in range(len(arr)-1, -1, -1):
        b[c[arr[i]-1]]=arr[i]
        c[arr[i]-1]-=1
    return b

def radix(arr):
    base=len(arr)
    res=counting(arr,base, lambda x: x//base)
    #lambda przypisuje funkcje do zmiennej i można się do niej odwołać 
    #np. x=lambda x: x+1 
    res=counting(res, base, lambda x: x//base)

    return res





