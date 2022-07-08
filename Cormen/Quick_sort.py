def partition(T, p, k):
    x=T[k]      # wartosc ,,środkowa"
    l=p-1       # ile wartości jest po lewej stronie
    
    for i in range(p, k):
        if T[i]<=x:  
            l+=1
            T[i], T[l] = T[l], T[i]     #jesli element jest mniejszy od x to daje go po lewej stronie
    T[l+1], T[k] = T[k], T[l+1]     # wsadzam x w pozycje l+1, czyli tam gdzie powinien byc
    
    return l+1      #zwaracam pozycje elementu ,,środkowego"

def quick_sort(T,p,k):
    if p<k:
        q=partition(T,p,k)          # indeks elementu "środkowego"
        quick_sort(T,p,q-1)         # technika
        quick_sort(T,q+1,k)         # dziel i zwycieżaj (q-1 ponieważ q jest na odpowiedniej pozycji)


if __name__=="__main__":
    tablica=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    quick_sort(tablica, 0, len(tablica)-1)
    print(tablica)
