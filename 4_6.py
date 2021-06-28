
# 0：false、1: true
def func(i,w,a):
    if i == 0:
        if w == 0:
            return True
        else:
            return False

    if memo[i][w] != -1:
        return memo[i][w]
    
    if func(i-1, w, a):
        memo[i][w] = 1;
        return memo[i][w];
    
    if func(i-1, w-a[i-1], a):
        memo[i][w] = 1;
        return memo[i][w];
    
    memo[i][w] = 0;
    return memo[i][w];


n, w = map(int,input().split())
a = list(map(int,input().split()))
memo = [[-1] * (w+1) for i in range(n+1)]

if func(n,w,a):
    print('Yes')
else:
    print('No')

print(memo)