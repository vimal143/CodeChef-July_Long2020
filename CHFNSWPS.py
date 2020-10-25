from sys import stdin
from math import ceil, gcd
from collections import Counter

# Input data
#stdin = open("input", "r")

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    d1 = Counter(a)
    d2 = Counter(b)
    d = Counter(a + b)
    x, y = [], []
    cond = True
    for ele in d:
        if d[ele] % 2 == 0:
            m = d[ele] // 2
            if ele in d1:
                if d1[ele] > m:
                    for q in range(d1[ele] - m):
                        x.append(ele)
            if ele in d2:
                if d2[ele] > m:
                    for q in range(d2[ele] - m):
                        y.append(ele)
        else:
            cond = False
            break
    if cond == False:
        print(-1)
    else:
        x.sort()
        y.sort()
        if len(x) != len(y):
            print(-1)
            continue
        cost = 0
        i, j = 0, 0
        w = min(min(a), min(b))
        while(i < len(x) and j < len(y)):
            if x[i] <= y[j]:
                if w * 2 < x[i]:
                    cost += (2 * w)
                else:
                    cost += x[i]
                del(y[-1])
                i += 1
            else:
                if 2 * w < y[j]:
                    cost += (2 * w)
                else:
                    cost += y[j]
                del(x[-1])
                j += 1
        print(cost)
