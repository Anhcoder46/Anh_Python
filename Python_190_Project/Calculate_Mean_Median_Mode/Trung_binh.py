#Median
list = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list.sort()

if len(list) % 2 == 0:
    m1 = list[len(list) // 2]
    m2 = list[len(list) // 2 - 1]
    median = (m1 + m2) / 2
else:
    median = list[len(list) // 2]
print(median)