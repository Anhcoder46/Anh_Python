import pandas as pd
# a = [7, 5, 9]
# myvar = pd.Series(a)
# print(myvar)

# calories = {"day1": 420, "day2": 380, "day3":390}
# myvar = pd.Series(calories)
# print(myvar)

# calories = {"day1": 420, "day2": 380, "day3":390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
#     }
# #load dữ liệu vào đối tượng DataFrame
# df = pd.DataFrame(data)
# print(df)

# data = {
#     "Tên cột 1": [4, 5, 7, 8 , 6, 9, 1, 2, 3],
#     "Tên cột 2": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     "Tên cột 3": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     "Tên cột 4": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     "Tên cột 5": [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     }
# df = pd.DataFrame(data)
# print(df)

# print(df.loc[0])
# print("_________________________________")
# print(df.loc[1])
# print("_________________________________")
# print(df.loc[[0, 1]])
# print("_________________________________")

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
#     }
# #load dữ liệu vào đối tượng DataFrame
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)


data_csv = pd.read_csv(r"C:\Users\ACER\Desktop\data.csv")
print(data_csv)

data_excel = pd.read_excel(r"C:\Users\ACER\Desktop\test.xlsx")
print(data_excel)