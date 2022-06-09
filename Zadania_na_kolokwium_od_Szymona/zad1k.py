from zad1ktesty import runtests

def roznica( S ):
    odp=0
    sum=0
    for number in S:
        if number=='0':
            sum+=1
        else:
            sum-=1
        if sum<0:
            sum=0
        odp=max(odp,sum)
    if odp==0: return -1
    return odp

runtests ( roznica )