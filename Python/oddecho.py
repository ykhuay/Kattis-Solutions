N = int(input())
myList = []

for i in range(N):
    word = input()
    myList.append(word)

echoList = myList[::2]
echo = ("\n".join(echoList))
print(echo)

    