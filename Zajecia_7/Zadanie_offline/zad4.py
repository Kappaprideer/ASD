from zad4testy import runtests

# f(a,b, money)
# f to funkcja która zwraca największą ilość studentów do kwoty money 
# oraz do budynku a,b zawierając go lub nie

#funkcja g(a,b,money)
# zawiera najwieksza mozliwoa ilosc studentow do kwoty "money" zawierajac 
# w niej sam budynek na pozycji a b
#czyli na poczatku dodaje do kosztu koszt(a,b) i wtedy sprawdzam kiedy 
# moge dodac f(a-i, money)  




def select_buildings(T,p):
    n=len(T)
    T.sort(key=lambda pair: pair[2])
    T.sort(key=lambda pair: pair[1])
    tab_for_g=[[0 for b in range(p+1)] for _ in range(n) ]
    tab_for_f=[[0 for b in range(p+1)] for _ in range(n) ]

    
    
    
    
    



    return [0]

runtests( select_buildings )