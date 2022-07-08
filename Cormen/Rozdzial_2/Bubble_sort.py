def Bubble_sort(T):
    for i in range(len(T)):
        for j in range(len(T)-1, i, -1):
            if T[j]<T[j-1]:
                temp=T[j-1]
                T[j-1]=T[j]
                T[j]=temp
                print(T)


if __name__=="__main__":
    tablica=[10,9,8,7,6,5,4,3,2,1,0,5,1,5]
    print(tablica, "\n")
    Bubble_sort(tablica)
    print(tablica)