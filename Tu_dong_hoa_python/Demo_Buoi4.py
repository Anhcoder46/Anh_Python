import pandas as pd
import requests
df = pd.read_excel(r"C:\Users\\ACER\Downloads\exercise_data.xlsx")
print(df)
print("-------------------------------------")
#cach 1 : Dien bang gia tri trung binh cua cot 
#mean_calories = df['Lượng calo'].mean()
#df ["Lượng calo"] = df['Lượng calo'].fillna(mean_calories);
#print(df)
#cách 2 là gán trực tiếp cho nó
df.loc[16,'Lượng calo'] = '301'
df.loc[26,'Lượng calo'] = '201'
print(df)
print("-------------------------------------")
#Sửa ngày của '20201226' thành 2020/12/24'
df.loc[24, 'Ngày'] = '2020/12/24'
print(df)
print("-------------------------------------")
#Sửa hàng thứ 7 (index 5) thành 45
df.loc[5, 'Thời lượng'] = 45
print(df)
print("-------------------------------------")
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame sau khi loại bỏ các hàng trùng lặp: ")
print(df_no_duplicates)
print("-------------------------------------")
