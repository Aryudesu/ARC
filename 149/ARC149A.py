import math

N, M = [int(l) for l in input().split()]
t = int('1'*N)
nlen = N
Num = [9, 8, 7, 6, 5, 4, 3, 2, 1]
while t > 0:
    g = math.gcd(t, M)
    tmp = M // g
    if tmp < 10:
        for n in Num:
            if tmp * n < 10:
                print(t * tmp * n)
                exit()
    t = t // 10
print(-1)
