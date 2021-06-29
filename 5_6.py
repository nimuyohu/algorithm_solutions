N, W = map(int,input().split())
a = list(map(int,input().split()))
m = list(map(int,input().split()))
INF = 2**29
dp = [[INF] * (W+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(W+1):
        if dp[i][j] < INF:
            dp[i+1][j] = min(dp[i+1][j],0)
        if j+a[i] <= W and dp[i+1][j] < m[i]:
            dp[i+1][j+a[i]] = min(dp[i+1][j+a[i]],dp[i+1][j]+1)

if dp[N][W] < INF:
    print("Yes")
else:
    print("No")

for i in dp:
    print(i)