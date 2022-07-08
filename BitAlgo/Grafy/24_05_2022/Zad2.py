# Litery równoważne
# Trzy stringi A, B i C. Napisy A i B mają identyczną długość oraz litery na poszczególnych indeksach w A i B są sobie równoważne. 
# Równoważność jest symetryczna, oraz przechodnia. Znaleźć najmniejszy leksykograficznie napis C, zamieniając litery w C tylko 
# z literami do nich równoważnymi.

class Node:
    def __init__(self,val):
        self.val=val
        self.parent=self

def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent
        
def union(x,y):
    x=find(x)
    y=find(y)
    if x.val==y.val:
        return
    if x.val<y.val:
        y.parent=x
    else:
        x.parent=y
        
def equvilent(A,B,C):
    for i in range(len(A)):
        x=Node(ord(A[i]))
        y=Node(ord(B[i]))
        union(x,y)
        print(x.val,find(x).val)
    D=""

    for letter in C:
        x=Node(ord(letter))
        x=find(x)
        D+=chr(x.val)
    
    return D

if __name__=="__main__":
    A="GACBBD"
    B="HCDLHG"
    C="HHGAC"
    print(equvilent(A,B,C))
