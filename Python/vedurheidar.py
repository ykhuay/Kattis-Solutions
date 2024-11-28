v = int(input())
n = int(input())
myDict = {}

for i in range(n):
    road, windSpeed = input().split()
    windSpeed = int(windSpeed)
    if windSpeed < v:
        windSpeed = 'lokud'
    else:
        windSpeed = 'opin'
    myDict.update({road : windSpeed})

for road, windSpeed in myDict.items():
    print(road, windSpeed)