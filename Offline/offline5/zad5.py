from queue import PriorityQueue
from zad5testy import runtests


def plan(T):
    kolejka=PriorityQueue()
    odpowiedz=[0]
    suma=T[0]
    for i in range(1,len(T)):
        kolejka.put((-1*(T[i]), i))
        if i == suma and suma!=len(T)-1:
            punkt=kolejka.get()
            suma+=-1*(punkt[0])
            odpowiedz.append(punkt[1])
    odpowiedz.sort()            
    return odpowiedz

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )