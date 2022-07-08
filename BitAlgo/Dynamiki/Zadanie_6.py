def number_of_binary_strings(n):
    tab=[0 for i in range(n+1)]
    tab[1]=2
    tab[2]=3
    for i in range(3,n+1):
        tab[i]=tab[i-1]+tab[i-2]
    return tab[n]


if __name__=="__main__":
    n = 20
    print(number_of_binary_strings(n))