def sorting(tab):
    n=len(tab)
    for j in range(n):
        swapped=False
        for i in range(n-1-j):
            if tab[i]>tab[i+1]:
                tab[i+1], tab[i] = tab[i], tab[i+1]
                swapped=True
        if not swapped:
            break
    return tab


if __name__=="__main__":
    tablica=[10,9,8,7,6,5,4,2,2,2,5,5,1,1]
    print(tablica)
    sorting(tablica)
    print(tablica)