import math as m

list = input().split()
h = int(list[0])
v = int(list[1])


def shortest_ladder(h,v):
    degree_v = m.radians(v)
    sine_v = m.sin(degree_v)
    l = h/sine_v
    return m.ceil(l)

print(shortest_ladder(h,v))