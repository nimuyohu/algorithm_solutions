n, W, k = map(int,input().split())
a = list(map(int,input().split()))

INF = 2**20

dp = [[INF] * (W+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(W+1):
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        if j >= a[i]:
            dp[i+1][j] = min(dp[i][j],dp[i][j-a[i]] + 1)

if dp[n][W] <= k:
    print('Yes')
else:
    print('No')