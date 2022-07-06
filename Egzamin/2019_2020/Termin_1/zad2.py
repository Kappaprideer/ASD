from zad2testy import runtests

def opt_sum(tab):
    n=len(tab)
    T=[ [0 for i in range(n)] for j in range(n)]   

    for i in range(n):
        for j in range(n):
            if i!=j:
                T[i][j]=tab[i]+tab[j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if abs(tab[i]+tab[k]+tab[j])<abs(T[i][j]):
                    T[i][j]=tab[i]+tab[k]+tab[j]
    
    odp=-1
    for i in range(n):
        for j in range(n):
            odp=max(odp,abs(T[i][j]))
    return odp
    
    
    
    
    
    # negative=[]
    # positive=[]
    # for number in tab:
    #     if number<0:
    #         negative.append(number)
    #     else:
    #         positive.append(number)
    # negative.sort()
    # positive.sort()
    # ans=-1
    # sum=0
    # np=0
    # nk=len(negative)-1
    # pp=0
    # pk=len(positive)-1

    # while np<nk or pp<pk:
    #     if np<nk and pp<pk:
    #         if abs(sum+positive[pp])<=abs(sum+positive[pk]) and abs(sum+positive[pp])<=abs(sum+negative[np]) and abs(sum+positive[pp])<=abs(sum+negative[nk]):
    #             sum+=positive[pp]
    #             pp+=1
    #         elif abs(sum+positive[pk])<=abs(sum+positive[pp]) and abs(sum+positive[pk])<=abs(sum+negative[np]) and abs(sum+positive[pk])<=abs(sum+negative[nk]):
    #             sum+=positive[pk]
    #             pk-=1
    #         elif abs(sum+negative[nk])<=abs(sum+positive[pp]) and abs(sum+negative[nk])<=abs(sum+positive[pk]) and abs(sum+negative[nk])<=abs(sum+negative[np]):
    #             sum+=negative[nk]
    #             nk-=1
    #         else:
    #             sum+=negative[np]
    #             np+=1

    #     elif np<nk:
    #         if abs(sum+negative[np])<=abs(sum+negative[nk]):
    #             sum+=negative[np]
    #             np+=1
    #         else:
    #             sum+=negative[nk]
    #             nk-=1
    #     else:
    #         if abs(sum+positive[pp])<=abs(sum+positive[pk]):
    #             sum+=positive[pp]
    #             pp+=1
    #         else:
    #             sum+=positive[pk]
    #             pk-=1
        
    #     ans=max(ans,abs(sum))

    return ans



runtests( opt_sum )
