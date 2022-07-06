from zad2testy import runtests

def tower(A):
  odp=0
  n=len(A)
  T=[1 for _ in range(n)]
  for i in range(n):
    for j in range(i):
      if A[j][0]<=A[i][0] and A[j][1]>=A[i][1] and T[i]<T[j]+1:
        T[i]=T[j]+1
        odp=max(odp,T[i])
  return odp


runtests( tower )
