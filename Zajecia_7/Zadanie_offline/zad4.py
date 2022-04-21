from zad4testy import runtests

# f(a,b, money)
# f to funkcja która zwraca największą ilość studentów do kwoty money 
# oraz do budynku a,b zawierając go lub nie

#funkcja g(a,b,money)
# zawiera najwieksza mozliwoa ilosc studentow do kwoty "money" zawierajac 
# w niej sam budynek na pozycji a b
#czyli na poczatku dodaje do kosztu koszt(a,b) i wtedy sprawdzam kiedy 
# moge dodac f(a-i, money)  


# funkcja ktora wraca w danej kwocie po wszystkich budynkach po kolei od budynku o indeksie a do 0 sprawdzajac czy budynek zachodzi 


def g(budynek,tablica):     # funkcja w ktorej budynek zawiera sie i sumuje reszte 
    pass


# napisać funkcje ktora tylko przyjmuje wartosci i szuka nawet nachodzacych na siebie

def f(number_in_array, array, price):
    pass



def select_buildings(T,p):
    n=len(T)
    # tab - tablica zawierajaca krotki [(0_poczatek, 1_koniec, 2_ilosc_studentow, 3_koszt, 4_miejsce w normalnym ciagu )]
    # I_was_here - tablice ktora mowi ze juz sprawdzalem ten przypadek 
    tab=[[0,0,0,0,0] for _ in range(n)]
    for i in range(n):
        tab[i][0] = T[i][1]
        tab[i][1] = T[i][2]
        tab[i][2] = (T[i][2]-T[i][1])*T[i][0]
        tab[i][3] = T[i][3]
        tab[i][4] = i

    tab.sort(key=lambda pair: pair[1])
    tab.sort(key=lambda pair: pair[0])
    # tab_for_g=[[-1 for b in range(p+1)] for _ in range(n) ]
    # tab_for_f=[[0 for b in range(p+1)] for _ in range(n) ]
    

    # # Przygotowywanie tablic
    # for i in range(n):
    #     for price in range(tab[i][3], p+1):
    #         tab_for_g[i][price] = tab[i][2]
    # for i in range(min(p,tab[0][3])):  
    #     tab_for_f[0][i]=0
    #     tab_for_g[0][i]=0
    # for i in range(tab[0][3], p+1): 
    #     tab_for_f[0][i]=tab[0][2]
    # # Przygotowywanie tablic
    # for price in range(p+1):
    #     for i in range(1,n):
    #         tab_for_f[i][price] = tab_for_f[i-1][price]
    #         if price - tab[i][3] >=0 :
    #             tab_for_f[i][price]=max(tab_for_f[i][price], tab_for_f[i-1][price-tab[i][3]]+tab[i][2])
    # print("\n MOJ WYNIK: \n", tab_for_f[n-1][price], "\n")
    



    indeksy=[[] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            if tab[i][1] < tab[j][0]:
                indeksy[j].append(i)
        indeksy[i].append(i)
    
    maximum=0
    result=[]

    for x in range(n-1, -1, -1):
        lenght=len(indeksy[x])
        if lenght>1:
            tab_for_f=[[0 for b in range(p+1)] for _ in range(lenght) ]
            for i in range(tab[indeksy[x][0]][3], p+1): 
                tab_for_f[0][i]=tab[indeksy[x][0]][2]

            for price in range(p+1):
                for i in range(1,lenght):
                    tab_for_f[i][price] = tab_for_f[i-1][price]
                    if price - tab[indeksy[x][i]][3] >=0 :
                        tab_for_f[i][price]=max(tab_for_f[i-1][price], tab_for_f[i-1][price-tab[indeksy[x][i]][3]]+tab[indeksy[x][i]][2])

            if tab_for_f[lenght-1][p] > maximum:
                maximum = tab_for_f[lenght-1][p]
                result = indeksy[x]

    
    wynik=[tab[result[i]][4] for i in range(len(result))]
    print("\n MOJ WYNI: \n", maximum, "\n")
    print(indeksy)
    return wynik

runtests( select_buildings )

# Tablice indeksów na których za każdym razem jak natrafiam na indeks który juz sprawdzałem jakie 
# Rozwiązanie O(n^2 * n*p)


