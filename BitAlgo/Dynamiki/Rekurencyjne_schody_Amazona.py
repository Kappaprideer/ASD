
def Amazon_Stairs(T):
    ans=[0 for _ in range(len(T))]
    ans[0]=1
    for j in range(len(T)):
        for i in range(j+1,min(j+T[j]+1,len(T))):
            ans[i]+=ans[j]
        
    return ans[len(T)-1]


if __name__=="__main__":
    A=[2,1,3,2,2,3]
    print(Amazon_Stairs(A))