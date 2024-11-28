import math

N, W, H = map(int, input().split())

hyposq = W * W + H * H
hypo = math.sqrt(hyposq)


for i in range(N):
    x = int(input())
    if hypo < x:
        print('NE')
    else:
        print('DA')
