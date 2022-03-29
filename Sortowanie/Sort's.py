import random
HOW_MANY=25

def Selection_sort(T):      #sortowanie przez wybieranie
    n=len(T)
    




def Insertion_sort(T):      #sortowanie przez wstawianie 
    n=len(T)
    for i in range(1,n):    #przegladam po elementy
        klucz=T[i]
        j=i-1
        while j>=0 and T[j]>klucz:
            T[j+1]=T[j]
            j-=1
        T[j+1]=klucz




if __name__=="__main__":
    tablica=[random.randint(0,150) for _ in range(HOW_MANY)]
    print("\n",tablica, "\n")


    #Insertion_sort(tablica)
    
    
    
    
    print(tablica, "\n")

