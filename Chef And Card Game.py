def dig_sum(num):
    return 0 if num == 0 else int(num % 10) + dig_sum(int(num / 10))


tc = int(input())
while tc > 0:
    N = int(input())
    Chef = 0
    Morty = 0
    while N > 0:
        A, B = map(int, input().split())
        sum_a = dig_sum(A)
        sum_b = dig_sum(B)
        if sum_a > sum_b:
            Chef += 1
        elif sum_a == sum_b:
            Chef += 1
            Morty += 1
        else:
            Morty += 1
        N -= 1
    if Chef > Morty:
        print(0, Chef)
    elif Chef < Morty:
        print(1, Morty)
    else:
        print(2, Chef)
    tc -= 1

