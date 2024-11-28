n, k = map(int, input().split())
list = list(map(int,input().split()))
y = 0

for i in range(n):
    if list[y] != k:
        y += 1
        
    if list[0] == k:
        print('fyrst')
        break
    
    elif list[1] == k:
        print('naestfyrst')
        break
    
    if list[y] == k:
        print((list.index(k)+1), 'fyrst')
        break