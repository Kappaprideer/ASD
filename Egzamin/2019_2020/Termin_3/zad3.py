from re import I
from zad3testy import runtests

class Node:
    def __init__( self, val ):
        self.next = None
        self.val = val

def tasks(T):
    minimum=10**10
    place=None
    for i in range(len(T)):
        if T[i].val<minimum:
            minimum=T[i].val
            head=T[i]
            place=i
            
    T[place]=T[place].next
    head.next=None           
    curr=head
    wszystko=False
    while not wszystko:
        wszystko=True
        minimum=10**10
        for i in range(len(T)):
            if T[i] is not None and T[i].val<minimum:
                minimum=T[i].val
                place=i
                wszystko=False
        if not wszystko:
            curr.next=T[place]
            curr=curr.next
            T[place]=T[place].next
            curr.next=None

    return head

runtests( tasks )
