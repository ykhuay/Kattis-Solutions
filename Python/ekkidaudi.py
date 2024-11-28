s1 = input()
s2 = input()

joins1 = s1.split('|')
joins2 = s2.split('|')

words = joins1[0] + joins2[0] + ' ' +joins1[1] + joins2[1]
print(words)