import time 

TEST_SPEC = [
# N (długość tablicy), k (max. liczba), hint (poprawna odpowiedź)
  (10, 20, 5),
  (10, 100, 4),
  (20, 500, 5),
  (100, 10000, 14),
  (500, 10000, 40),
  (1000, 1000, 53),
  (1000, 10000, 61),
  (2500, 10000, 94),
  (5000, 100000, 132),
  (5000, 1000000, 138),
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
        arr = []
        for j in range(el[0]):
            arr.append(MY_random()%el[1])
        
        start = time.time()
        sol = f(arr)
        end = time.time()
        total += (end-start)
        testy += 1 
        if sol == el[2]:
            print("TEST #", i, " zaliczony")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[2])
            print("Czas trwania: %.2f sek.\n" %float(end-start))
            zaliczone += 1
        else:
            print("TEST #", i, " NIEZALICZONY!")
            print("Twoja odpowiedz: ", sol, "\nPoprawna odpowiedz: ", el[2])
            print("Czas trwania: %.2f sek.\n" %float(end-start))

        i += 1
    print("Zaliczone testy: ", zaliczone, "/", testy)
    print("Orientacyjny łączny czas: %.2f sek." %float(total))

