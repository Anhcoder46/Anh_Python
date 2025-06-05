#. Bán kính của một hình tròn là 30 mét
#    - Tính diện tích của một hình tròn và gán giá trị cho một biến có tên area_of_circle
#    - Tính chu vi của một hình tròn và gán giá trị cho một biến có tên circum_of_circle
Ban_kinh = 30
area_of_circle = Ban_kinh * Ban_kinh * 3.141592653589793
circum_of_circle = 2 * Ban_kinh * 3.141592653589793

print("Diện tích hình tròn là:", area_of_circle)
print("Chu vi hình tròn là:", circum_of_circle)
#    - Lấy bán kính làm đầu vào của người dùng và tính diện tích hình tròn
Ban_kinh = float(input("Nhập bán kính hình tròn: "))
area_of_circle = Ban_kinh * Ban_kinh * 3.141592653589793
print("Diện tích hình tròn là: ", area_of_circle)

#2. Tìm phần tử lớn nhất trong một danh sách (list)
lst = [10, 5, 20, 8, 30]
a = max(lst)
print("Phần tử lớn nhất: ", a)

#3. Tìm phần tử nhỏ nhất trong một danh sách (list)
lst = [10, 5, 20, 8, 30]
b = min(lst)
print("Phần tử nhỏ nhất: ", b)

#4. Tìm độ dài của của câu “Tôi là một sinh viên DAU”
a = "Tôi là một sinh viên DAU"
Do_dai = len(a)
print("Độ dài của câu: ", Do_dai)

#5. Có bao nhiêu từ trong câu “Tôi là một sinh viên DAU”
a = "Tôi là một sinh viên DAU"
Dem_phan_tu = len(a.split())
print("Số từ trong câu: ", Dem_phan_tu)
