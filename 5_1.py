n = int(input())
dp = [[0] * 3 for i in range(n+1)]

for i in range(1,n+1):
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i-1][1]+a,dp[i-1][2]+a)
    dp[i][1] = max(dp[i-1][0]+b,dp[i-1][2]+b)
    dp[i][2] = max(dp[i-1][0]+c,dp[i-1][1]+c)
print(max(dp[n][0],dp[n][1],dp[n][2]))
# dp_a, dp_b, dp_c = [], [], []

# for i in range(n):
#     a, b, c = map(int, input().split())
#     if i != 0:
#         dp_a.append(max(dp_b[i-1] + a,dp_c[i-1] + a))
#         dp_b.append(max(dp_a[i-1] + b,dp_c[i-1] + b))
#         dp_c.append(max(dp_a[i-1] + c,dp_b[i-1] + c))
#     else:
#         dp_a.append(a)
#         dp_b.append(b)
#         dp_c.append(c)
# print(max(dp_a[-1],dp_b[-1],dp_c[-1]))