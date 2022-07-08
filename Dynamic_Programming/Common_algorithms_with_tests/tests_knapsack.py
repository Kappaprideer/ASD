import time 

TEST_SPEC = [
# N (długość tablicy), k (max. wartosci), w (max. waga), hint (poprawna odpowiedź)
  (10, 100, 500, 396),
  (10, 1000, 500, 1148),
  (100, 1000, 500, 6170),
  (100, 10000, 1000, 19708),
  (100, 10000, 5000, 43598),
  (150, 1000, 1000, 5312),
  (150, 5000, 2500, 27000),
  (150, 5000, 5000, 41030),
  (250, 1000, 1000, 14202),
  (250, 5000, 5000, 63192),
]

MY_seed    = 42
MY_a       = 134775813
MY_c       = 1
MY_modulus = 2**32

def MY_random():
   global MY_seed, MY_a, MY_c, MY_modulus
   MY_seed = (MY_a * MY_seed + MY_c) % MY_modulus
   return MY_seed

def runtests( f ):
    total = 0 
    zaliczone = 0 
    testy = 0
    i = 0
    for el in TEST_SPEC:
        W = []
        P = []
        for j in range(el[0]):
            W.append(MY_random()%el[1])
            P.append(MY_random()%el[1])
        
        start = time.time()
        sol = f(W, P, el[2])
        end = time.time()
        total += (end-start)
        testy += 1 
        if sol == el[3]:
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[3])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

