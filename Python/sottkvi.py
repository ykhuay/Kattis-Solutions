n,k,d = map(int, input().split()) 
# friends, no. of days to bd, today
x = 0

for i in range(n):
    z = int(input()) # day in Q
    if (z + 14) <= (k + d):
        x += 1

print(x)
        