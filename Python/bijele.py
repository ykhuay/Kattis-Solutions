k,q,r,b,n,p = map(int, input().split())

list1 = [k,q,r,b,n,p]
list2 = [1,1,2,2,2,8]
result = []

result = [list2[i] - list1[i] for i in range(len(list2))]

print(*result)
    
    