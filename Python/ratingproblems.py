n,k = map(int, input().split())
d = n - k
x = 0

for i in range(k):
    r = int(input())
    x += r

minimum = d * -3
maximum = d * 3

min_overall = float((minimum + x) / n) 
max_overall = float((maximum + x) / n)

print(min_overall, max_overall)