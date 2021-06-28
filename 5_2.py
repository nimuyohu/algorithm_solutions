n, W = map(int,input().split())
# n = int(input())
a = list(map(int,input().split()))
# W = 10000
dp = [[False] * (W+1) for _ in range(n+1)]
# i番目まででwはできるか否か。

dp[0][0] = True
for i in range(n):
    for j in range(W+1):
        if not dp[i][j]: continue
        dp[i+1][j] = True
        if j+a[i] <= W:
            dp[i+1][j+a[i]] = True;
print(dp[n][W])
