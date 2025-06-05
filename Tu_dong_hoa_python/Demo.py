x = 10
# 1_my_var = 1
my_var = 1
first_name = 'Tran Duc Anh'
First_Name = 'Tran Duc Anh'
#def = 'a'
print()


#Các kiểu dữ liệu cơ bản
#Số nguyên, số thực, số phức, bool,...

#Kiểu dữ liệu phức hợp
#list
a = (1, 2, 3)
#tuple => không thể thay đổi
b = (1, 2, 3)
#dict kiểu từ điển
s = {
    "name": "anh",
    "age": 22
    }
#set => khai trừ biến trùng lặp
a = set{1, 2, 3, 3}
print(a)
#frozenset
a = frozenset({1, 2, 3, 4})

#Kiểu dữ liệu đặc biệt
#NoneType
a = ""
a = None
#Bytes
x = bytes(12)
y = bytes("hello")

#Hàm funtion()


x = 10
def my_func():
    y =20
    print("Biến toàn cục: ", y)
    print("Biến cục bộ: ", x)
my_func()