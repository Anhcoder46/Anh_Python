from time import time
start = time()

word = "Tri tue nhan tao"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
thoi_gian_thuc_hien = end - start
print("Thoi gian thuc hien: ", thoi_gian_thuc_hien)