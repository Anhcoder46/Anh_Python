a = 5
a = a + 1
a += 1
print(a)
 
a -= 3
print(a)
 
a*= 2
print(a)
 
empty_value = None
if empty_value is None:
    print("Có")
else:
   print("Không")

a = 10
b = 20
if a > b:
    max_value = a
elif a < b:
    print("a < b")
else:
    max_value = b
    
max_value = a if (a > b) else b
print(max_value)

num1 = 10
num2 = 20
if num1 > num2:
    print("Num1 lớn hơn num2")
elif num1 < num2:
    print("Num1 nhỏ hơn num2")
else:
    print("Num1 bằng num2")
    
count = 5
while count > 0:
    print(count)
    count -= 1
    
#Bài tập
# 1. Sử dụng vòng lặp for để lặp từ 0 đến 10 và chỉ in ra các số chẵn
for i in range(11):
    if i % 2 == 0:
        print(i)

# 2. Sử dụng vòng lặp để tìm ra số lớn nhất trong danh sách không dùng hàm có sẵn
n= [15, 34, 1, 24, 87, 9, 30, 45]
max_num = n[0]
for num in n:
    if num > max_num:
        max_num = num
print("Số lớn nhất là: ", max_num)
