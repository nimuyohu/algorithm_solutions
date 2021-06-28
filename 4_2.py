N = int(input())
memo = [-1]*(N+1)
def tori(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    if memo[n] != -1:
        return memo[n]
    
    memo[n] = tori(n-1) + tori(n-2) + tori(n-3)
    return memo[n]

ans = tori(N)
print(ans)