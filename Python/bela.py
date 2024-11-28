N, B = input().split()
N = int(N)

scoreTable = {
    'A': [11, 11],
    'K': [4, 4],
    'Q': [3, 3],
    'J': [20, 2],
    'T': [10, 10],
    '9': [14, 0],
    '8': [0, 0],
    '7': [0, 0]
}

total_score = 0

for i in range(4*N):
    card, suit = map(str, input())
    dom_score, not_dom_score = scoreTable[card]
    
    if suit == B:
        total_score += dom_score
    else:
        total_score += not_dom_score
        
print(total_score)





