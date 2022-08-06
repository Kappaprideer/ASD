# Andrzej Zaborniak 
# Program na samym poczatku przechodzi drzewo w czasie O(n) szukając momentu w którym wierzchołki tworzą największą szerokosc orazy wysokosć.
# Następnie w następnym puszczeniu bfs-a program zapisuje wszystkie wierzchołki które po usunieciu odpowiednich krawędzi zostaną liściami. Każdy wierzchołek posiada pod 
# self.x swojego rodzica, dzięki temu wracając od wierzchołka do korzenia zamienia wartosci self.x na None, czyli te wierzchołki zostały wykorzystane. 
# Następnie program przechodzi po całym drzewie od korzenia i jesli wartosc wierzchołka self.x jest różna od None, znaczy że krawędź pomiędzy nim a wierzchołkiem należy usunąć.
# Całośc działania programu to O(3n) czyli O(n)



from egz1btesty import runtests
from collections import deque

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow


def wideentall( T ):
  max_width=0
  width=0
  max_lenght=0
  current=0
  liscie=[]
  Q=deque()
  Q.append((T,0)) # wierzchołek i odległość od korzenia
  
  while len(Q)>0:
    s,w=Q.popleft()
    if current!=w:
      current=w
      width=0
    width+=1
    if s.left is not None:
      s.left.x=s
      Q.append((s.left,w+1))
    if s.right is not None:
      s.right.x=s
      Q.append((s.right,w+1))

    if width>=max_width:
      # if current>max_lenght:
      max_width=width
      max_lenght=current

  Q.append((T,0))
  while len(Q)>0:
    s,w=Q.popleft()
    if w==max_lenght:
      liscie.append(s)
    if s.right is not None:
      Q.append((s.right,w+1))
    if s.left is not None:
      Q.append((s.left,w+1))
  
  Q=deque()
  for u in liscie:
    Q.append(u)

  while len(Q)>0:
    s=Q.popleft()
    if s is not None:
      if s.x is not None:
        Q.append(s.x)
        s.x=None
  
  ans=0
  Q=deque()
  Q.append(T)
  while len(Q)>0:
    s=Q.popleft()
    if s.x is not None:
      ans+=1
    if s.right is not None:
      if s.right.x!=None:
        ans+=1
      else:
        Q.append(s.right)
    if s.left is not None:
      if s.left.x!=None:
        ans+=1
      else:
        Q.append(s.left)
  print("Szerokosc:", max_width)
  return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )