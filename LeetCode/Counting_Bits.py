def countBits(n: int):
    ans=[-1 for _ in range(n+1)]
    ans[0]=0
    def f(n):
        if ans[n]!=-1:
            return ans[n]
        return (n%2)+f(n//2)

    for i in range(n+1):
        ans[i]=f(i)
    return ans

if __name__=="__main__":
    n=int(input())
    print(countBits(n))