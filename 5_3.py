n, W = map(int,input().split())
# n = int(input())
a = list(map(int,input().split()))
# W = 10000
dp = [[False] * (W+10) for _ in range(n+10)]

dp[0][0] = True

for i in range(n):
    for j in range(W+1):
        dp[i + 1][j] = dp[i + 1][j] or dp[i][j]
        if j >= a[i]:
            dp[i + 1][j] = dp[i + 1][j] or dp[i][j - a[i]]

print(dp[n][W])
# print(dp)
res = 0
for i in range(W+1):
    if dp[n][i]:
        res += 1
print(res)
