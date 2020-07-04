tc = int(input())
while tc > 0:
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(0, N-1):
        first = S[i]
        Sec = S[i+1]
        pluck = abs(first-Sec)-1
        count += pluck
    tc -= 1
    print(count)


