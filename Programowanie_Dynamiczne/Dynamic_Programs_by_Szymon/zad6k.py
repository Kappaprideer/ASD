from zad6ktesty import runtests 

def haslo ( S ):
    
    odp=[0 for _ in range(len(S)+1)]
    odp[0]=1
    odp[1]=1
    for i in range(2,len(S)+1):
        if S[i-2]>'2' and S[i-1]=='0':
            return 0

        if S[i-2]>'0' and S[i-1]=='0':
            odp[i]=odp[i-2]

        elif S[i-2]=='2' and S[i-1]<='6':
            odp[i]=odp[i-2]+odp[i-1]

        elif S[i-2]=='1':
            odp[i]=odp[i-1]+odp[i-2]

        elif S[i-2]=='0' and S[i-1]=='0':
            return 0

        else:
            odp[i]=odp[i-1]

    return odp[len(S)]

runtests ( haslo )