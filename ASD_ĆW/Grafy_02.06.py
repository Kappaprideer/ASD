# Poruszanie się po grafie tylko po malejących wagach i znaleźć najkrótsztszą ściezke do wierzchołków. 
# (wszystkie wagi są różne)

# Algorytm podobny do Bellmana Forda, sortujemy krawędzie malejąco a następnie dla każdej krawędzi wykonujemy relaksacje 
# tylko że bez odtwarzania ścieżek, zapamiętując jedynie wartość najmniejszej odległości idąc po krawędziach malejących

# ----------------------------------

# Graf skierowany w którym jeśli jest połączona trójka wierzchołków to chcemy dodać krawędź tak aby był połączone bezpośrednio usuwając stare 
# połączenie. 
# Graf może zawierać cykle. 
# Algorytm Florda Warshalla tylko zamiast przechowywania wag to trzymamy czy między wierzchołkami 

def foo(G):
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if G[i][k]==1 and G[k][j]==1:
                    G[i][j]=1

# ------------------------------------------

# Mamy dużo walut i mamy dla każdej waluty mamy rózny kurs, 
# W tabeli jest wpisane że jeśli sprzedamy dolara to zyskamy tyle funktów, dla sprzedania złotego zdobędziemy tyle euro . 
# Istnieje taka kombinacja że możemy na sprzedarzy i kupnie zarobić 

# Znajdujemy ujemny cykl, krawędzie przedstawiamy jako transakcja
# Bierzemy lograytmy z liczb, zmieniamy znak a następnie szukamy ujemnego cyklu. Ujemny cykle znajdujemy Bellmanem Fordem. 

# -----------------------------------------

# Jest Graf skieowany z wagami od A do B 
# Drogę na zmianę prowadzi Bob i Alice, zmieniają się na każdym wierzchołku. 

# Alice chce prowadzic jak najmniej, jak powinni jechać i kto powinien zaczynać 

# Z Grafu tworzymy kompletnie nowy graf za kazdym razem dublując wierzchołki od Alice do Boba i od Boba do Alice, wpisując w wierzchołkach od Alice do Boba
# wage krawędzi a od Boba do Alice dając zero.
# Natępsnie na takim grafie znaleźć najkrótszą ścieżkę Dijkstrą. 
#
# -----------------------------------------------------------------------

# Graf nieskierowany ważony bez pętli, czyli drzewo z wagami. 
# Każdy wierzchołek ma stopień nie większy niż trzy. 
# 
# Taki wierzchołek aby maksymalna odległość do najdalszego liścia była najmniejsza ze wszystkich wierzchołków. 

