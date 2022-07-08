def Selection_sort(T):
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i]<T[j]:
                tmp=T[i]
                T[i]=T[j]
                T[j]=tmp



if __name__=="__main__":
    tablica=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,0,100,55,5,4]
    print(tablica)
    Selection_sort(tablica)
    print(tablica)