"""
#Biến
print("Hello")

a = 6
print(a)

game = "Liên minh huyền thoại"
print("I like", game)

ticket_price = 15000
print("The ticket price is", ticket_price, "won")
print("The total price for 3 people is", ticket_price * 3, "won")
print("The total price for 5 people is", ticket_price * 5, "won")

#Ký tự thoát
name = "Duc Anh"
age ="21"
print("My name is", name, "\nI am", age, "years old")
print("\"I am 21 years old\"")

#Kiêu dữ liệu
x = 10
y = 3.14
z = "Đà Nẵng"

#Hàm type()
print(type(x))
print(type(y))
print(type(z))

#Kiểu dữ liệu số
#Kiểu số nguyên
a = 100
print(type(a))

b = 0
print(type(b))

c = -5
print(type(c))

#Kiểu số thực
pi = 3.14
print(type(pi))

height = 175.3
print(type(height))

#Kiểu dữ liệu chuỗi
#Kiểu Sting
name = "Duc Anh"
print(type(name))

#Kiểu dữ liệu boolean
student = True
print(type(student))

#Kiểu dữ liệu list
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
print(fruits)
print(numbers)

fruits = ["apple", "banana", "orange"]
print(fruits[0:2])

#Thay đổi giá trị trong list
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[0] = 100
print(numbers)

#Thêm giá trị vào list
fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("mango")
print(fruits)

#Chuyển đổi kiểu dữ liệu này sang kiểu dữ liệu khác
s = "100"
n = int(s)
f = float(s)
print(n, type(n))
print(f, type(f))
"""

#Toán tử
#Toán tử số học
a = 9
b = 4
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)

#Toán tử số học
print("a // b = ", a // b)
print("a ** b = ", a ** b)
print("a % b = ", a % b)

#Toán tử chuỗi
s1 = "Hello"
s2 = "World"
print(s1 + s2)
print(s1 * 3)

#Toán tử so sánh
print("a > b = ", a > b)
print("a < b = ", a < b)
print("a >= b = ", a >= b)
print("a <= b = ", a <= b)
print("a == b = ", a == b)
print("a != b = ", a != b)

#Toán tử logic(And, Or, Not)
#Toán tử gán kết hợp(+=, -=, *=, /=)
#Toán tử ba ngôi
age = 18
result = "Adult" if age >= 18 else "Minor"
print(result)