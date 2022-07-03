from zad1testy import runtests
from queue import PriorityQueue


def chaos_index( T ):

    Q=PriorityQueue()
    for i in range(len(T)):
        Q.put((T[i], i))
    maximum=0
    for i in range(len(T)):
        number, indeks=Q.get()
        maximum=max(maximum, abs(i-indeks))

    return maximum

runtests( chaos_index )
