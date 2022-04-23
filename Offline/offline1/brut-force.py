class Node():
    def __init__(self, val):
        self.val=val
        self.next=None

def printing(first):
    p=first
    while p is not None:
        print("-->", p.val, end=" ")
        p=p.next
    print("\n")

def make_linked_list(tab):
    n=len(tab)
    head=None
    for i in range(n-1, -1, -1):
        tmp=Node(tab[i])
        tmp.next=head
        head=tmp
    return head

def sortH(p,k):
    if p is None:
        return None

    #ustawianie pierwszego najmniejszego elementu
    head=p
    i=0
    minimum=None
    m=head.val
    while p is not None and i<=k:
        if p.val<m:
            minimum=p
            poprzednik=tmp
            m=p.val
        tmp=p
        p=p.next
        i+=1
    if minimum is not None:
        chwilowa=minimum
        poprzednik.next=minimum.next
        chwilowa.next=head
        head=chwilowa
    

    #sortowanie reszty tablicy
    p=head.next
    before=head
    while p is not None:
        i=0
        current=p
        tmp=None
        minimum=None
        m=p.val
        while current is not None and i<=k:
            if current.val<m:
                r=tmp
                minimum=current
                m=current.val
            tmp=current
            current=current.next
            i+=1
            
        if minimum is not None:
            najmniejsza=minimum
            r.next=minimum.next
            najmniejsza.next=p
            before.next=najmniejsza
            before=najmniejsza
        else:    
            before=p
            p=p.next

        
    return head


if __name__=="__main__":
    tablica=[1, 0, 3, 2, 4, 6, 5]
    head=make_linked_list(tablica)
    printing(head)
    head=sortH(head,1)
    printing(head)
