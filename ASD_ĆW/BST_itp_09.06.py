# Tworzenie drzewa BST i wstawianie nowych elementów do drzewa BST 

class Node:
    def __init__(self,val):
        self.val=val
        self.parent=None
        self.left=None
        self.right=None


def add_element(root,x):
    if root is None:
        root=x
    else:
        u=root
        while u is not None:
            if u.val<x.val:
                prev = u
                u=u.right
            elif u.val>x.val:
                prev=u
                u=u.left
        if prev.val < x.val:
            prev.right=x
        else:
            prev.left=x
        x.parent=prev
    return root

# Wyszukiwanie następnika 
def maximum(root):
    r=root
    while r.right is not None:
        r=r.right
    return r.val

def minimum(root):
    r=root
    while r.left is not None:
        r=r.left
    return r.val


def succ(root, x):
    if x.right is not None:
        return minimum(x.right)
    v=x
    while v.parent is not None and v!=v.parent.left:
        v=v.parent
    return v.parent

# -------------------------------------------------
# Sekwencja symboli z kodu DNA, sprawdzamy czy wszystkie kody DNA są parami różne
# Symbole: GATC
# ACTAC
# TAG
# ACT
# TAG 
# Drzewa Trie
# Korzeń który sam w sobie nic nie przechowuje, mozę mieć do 4 dzieci. Każde z potencjalnych dzieci odpowieada jednej z liter
# alfabetu. Napis jest ścieżką od korzenia do liścia. Jeśli słowa miałyby takie same prefiksy to ścieżki byłby "łączone", wszystko wstawiamy w czasie liniowym.
# Jeżeli wstawiając dojdziemy do liścia w których to się już znajduje to znaczy że jakiś podciąg już się powtarza.
# W każdym wierzchołku trzymać 0 albo 1 aby wiedzieć zcy taki prefiks już był. 

# ----------------------------------------------------------
# Mamy dwa drzewa BST, interesuje nas ile takich samych kluczy znajduje się w obu drzewach.
# Zaczynamy w obydwu drzewach w elementach minimalnych, jeśli wartości są takie same to zwiększamy wynik, a w przeciwnym wypadku
# przechodzimy do następnego elementu funkcją succ (implementacja: next u góry). 

# ----------------------------------------------------------
# Jak uzupełnić drzewa aby wiedzieć który element jes i-ty w kolejności. 

# Zaczynamy od minimum i chodzimy do przodu nextem, aż dojdziemy do szukanego elementu. (Mniej optymalne rozwiązanie)
# |||||||||||||||||||
# W każdym wierzchołku drzewa trzymamy za razem informacje ile elementów znajduje się po lewej a ile po prawej stronie drzewa. 
# Jeśli i jest mniejsze od liczby elementów po lewej to idziemy w lewo, jeżeli i jest większe od ilośći elementóœ po lewej stronie idziemy w prawo
# odejmując (lewastrona+1). 