#1. Sử dụng vòng lặp for để lặp từ 0 đến 10 và chỉ in ra các số chẵn
for i in range(11):
    if i % 2 == 0:
        print(i)
#2. Sử dụng vòng lặp để tìm ra số lớn nhất trong danh sách (list) không dùng hàm có sẵn
n = [15, 34, 1, 24, 87, 9, 30, 45]
max_num = n[0]
for num in n:
    if num > max_num:
        max_num = num
print("Số lớn nhất là: ", max_num)