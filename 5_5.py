n, W = map(int,input().split())
a = list(map(int,input().split()))

dp = [[False] * (W+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(W+1):
        if dp[i][j]:
            dp[i+1][j] = True
        if dp[i+1][j] and j+a[i] <= W:
            dp[i+1][j+a[i]] = True

if dp[n][W]:print('Yes')
else:print('No')

for i in dp:
    print(i)