N = int(input())

def reverseBinary(N):
    N = f"{N:b}"
    N = str(N)[::-1]
    N = int(N,2)
    return N

print(reverseBinary(N))
    