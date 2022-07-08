# Zadanie 5: Sejf
# Dany jest kod PIN oraz liczby które można do siebie dodać aby dany kod otrzymać
# PIN jest czterocyfrowy 0000 - 9999, jeżelie suma jest większa niż 9999 to pierwsza 
# cyfra zostaje obcięta. 

from collections import deque

def minimum_path(T, number, pin):
    visited = [ 0 for _ in range(10000)]
    lenght = [ 0 for _ in range(10000)]
    q=deque()
    q.append(number)
    while len(q)>0:
        s=q.popleft()
        for i in T:
            ind = (i+s)%10000
            if visited[ind]==0:
                visited[ind]=1
                lenght[ind]=lenght[s]+1
                q.append(ind)
                if ind == pin:
                    return lenght[ind]
    return None


if __name__=='__main__':
    numbers=[ 13,223,9992,123,55,88]
    number_on_screen=0000
    pin = 339
    print(minimum_path(numbers,number_on_screen, pin))