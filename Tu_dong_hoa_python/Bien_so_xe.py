from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Mở trình duyệt
driver = webdriver.Chrome()
driver.get("https://phatnguoixe.com")
time.sleep(3)  # Chờ trang tải xong

# Chọn xe máy
xpath_xe_may = '//*[@id="frmSubmit"]/label[2]/input'
driver.find_element(By.XPATH, xpath_xe_may).click()
time.sleep(1)

# Nhập biển số xe
input_id = "bienso"
text_bien_so = "38MD-34545"
driver.find_element(By.ID, input_id).send_keys(text_bien_so)

# Click vào nút kiểm tra
xpath_btn = '//*[@id="submit"]'
driver.find_element(By.XPATH, xpath_btn).click()
time.sleep(5)  # Chờ kết quả hiển thị

# Lấy kết quả
try:
    result_id = "resultValue"  # Kiểm tra lại ID này xem có đúng không
    element_result = driver.find_element(By.ID, result_id)
    text_result = element_result.text
    print(text_result)

    if "không tìm thấy vi phạm phạt nguội" in text_result.lower():
        print("Không tìm thấy vi phạm phạt nguội")
    else:
        print("Tìm thấy vi phạm phạt nguội")
except Exception as e:
    print("Lỗi khi tìm kết quả:", e)

# Đóng trình duyệt
driver.quit()