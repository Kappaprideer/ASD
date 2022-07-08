
def game(T):
    tab=[[ number for number in T] for i in range(len(T))]
    for i in range(len(T)-2,-1,-1):
        for j in range(i+1,len(T)):
            tab[i][j] = max(T[i] + min( tab[i+2][j], tab[i+1][j-1]), T[j]+ min(tab[i+1][j-1], tab[i][j-2]))
    
    # for line in tab:
    #     print(line)
    return tab[0][len(T)-1]


if __name__=="__main__":
    tablica=[9,5,1,2,3,5]
    print(game(tablica))
