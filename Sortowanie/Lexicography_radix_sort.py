def Bucket_sort(tab, key, T):
    alfabet=[0 for _ in range(26)]
    result=[ 0 for _ in range(len(tab))]

    for i in range(len(tab)):
        ind=int(T[tab[i]][key]-'a')
        alfabet[ind]+=1
    for i in range(1, 26):
        alfabet[i]+=alfabet[i-1]

    for i in range(len(tab)-1, -1, -1):
        result[alfabet[T[tab[i]]]-1] = tab[i]
        alfabet[T[tab[i]]]-=1
    return result


def Radix_sort(sortowana, T):
    for i in range(len(T[sortowana[0]])-1, -1, -1):
        sortowana = Bucket_sort(sortowana, i, T)




def Buckets(T):
    maximum=0
    for i in range(len(T)):
        maximum=max(len(T[i]), maximum)

    B=[[] for i in range(maximum+1)]

    for i in range(len(T)):
        ind=len(T[i])
        B[ind].append(i)

    #buckety mają indeksy napisów 

    for i in range(maximum+1):
        print(B[i], "\n")
        if len(B[i])>1:
            Radix_sort(B[i], T)

    result=[ 0 for _ in range(len(T))]
    j=0
    for i in range(len(T)):
        for x in range(len(T[i])):
            result[j]=B[i][x]
            j+=1
    print(result)




if __name__=="__main__":
    tablica=["ala", "andrzej", "cio", "ccccc", "barbara", "deee", "eddd", "eded"]
    Buckets(tablica)