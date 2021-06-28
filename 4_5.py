import itertools
n = int(input())
ans = 0
for i in range(3,10):
    l = list(itertools.product([7,5,3], repeat=i))
    if len(str(n)) < i:
        break
    for j in l:
        res = ''
        for k in j:
            res = res + str(k)

        if int(res) <= n:
            if '7' in res and '5' in res and '3' in res:
                ans += 1
print(ans)