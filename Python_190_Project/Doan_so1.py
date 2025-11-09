import random
n = random.randrange(1, 10)
doan = int(input("Nhập số bất kỳ: "))
while n != doan:
    if doan < n:
        print("Quá thấp")
        doan = int(input("Nhập lại số: "))
    elif doan > n:
        print("Quá cao")
        doan = int(input("Nhập lại số: "))
    else:
        break
print("Bạn đã đoán đúng rồi")