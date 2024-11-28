n,m = map(int, input().split())
bomb_count = 0
bomb_location = []

for i in range(n):
    cell = input()
    bomb_count += cell.count('*')
    for j in range(len(cell)):
        if cell[j] == '*':
            bomb_location.append((i+1, j+1))

print(bomb_count)
for location in bomb_location:
    print(location[0], location[1])