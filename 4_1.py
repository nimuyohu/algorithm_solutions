N = int(input())
def tori(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return tori(n-1) + tori(n-2) + tori(n-3)
ans = tori(N)
print(ans)