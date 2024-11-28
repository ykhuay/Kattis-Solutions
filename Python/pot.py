N = int(input())
final_sum = 0

for i in range(N):
    P = input()
    last_num = int(P[-1])
    original_num = int(P[:-1])
    final_num = original_num ** last_num
    final_sum += final_num

print(final_sum)
    
    
    