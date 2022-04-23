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

def partition(head, tail):
    poczatek=head
    i=head
    l=head
    pierwszy_element=True
    while i is not tail and i is not None:
        if i.val<tail.val:
            if pierwszy_element:
                l.val, i.val = i.val, l.val
                pierwszy_element=False
            else:
                l=l.next
                l.val, i.val = i.val, l.val
        i=i.next
        printing(poczatek)
    if not pierwszy_element:
        l.next.val, tail.val = tail.val, l.next.val
    else:
        l.val, i.val = i.val, l.val        
    return poczatek, l, tail

def quicksort(head, tail):
    glowa = head
    if head is not None and tail is not None:
        poczatek, srodek, koniec = partition(head, tail)
        quicksort(poczatek, srodek)
        if srodek.next is not None and srodek.next.next is not None and srodek.next is not tail and srodek.next.next is not tail:
            quicksort(srodek.next.next, tail)
    printing(glowa)




if __name__=="__main__":
    tablica=[1,6,8,7,2,3,4,10]
    head=make_linked_list(tablica)
    printing(head)
    koniec=head
    while koniec is not None:
        if koniec.next is None:
            quicksort(head, koniec)
        koniec=koniec.next
    printing(head)












# def merge(h1, h2):
#     head=Node(None)
#     if h1 is None and h2 is None:
#         return None
#     if h1 is None:
#         return h2
#     if h2 is None:
#         return h1
#     if h1.val<h2.val:
#         head=h1
#         h1=h1.next
#     else:
#         head=h2
#         h2=h2.next
#     first=head
#     while h1 is not None or h2 is not None:
#         if h1 is not None and h2 is not None:
#             if h1.val<h2.val:
#                 head.next=h1
#                 h1=h1.next
#                 head=head.next
#                 head.next=None
#             else:
#                 head.next=h2
#                 h2=h2.next
#                 head=head.next
#                 head.next=None
#         elif h1 is not None:
#             while h1 is not None:
#                 head.next=h1
#                 h1=h1.next
#                 head=head.next
#                 head.next=None                
#         elif h2 is not None:
#             while h2 is not None:
#                 head.next=h2
#                 h2=h2.next
#                 head=head.next
#                 head.next=None
#     return first
# def merge_sort(h1, h2, k):
#     dzielenie, dziele na mniejsze listy i coraz mniejsze
#     i=0
#     if k>0:
#         while i<k and tmp is not None:
#             if i==k-1:
#                 i=0
#         merge_sort(h1, h2, k)
#         merge_sort()
#         return merge(h1,h2)