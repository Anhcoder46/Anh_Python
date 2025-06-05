import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# Vào trang web

driver.get("https://phatnguoixe.com")

# Click option xe máy
xpath_xe_may_dien = '//*[@id="frmSubmit"]/label[3]/span'  

element_xe_may_dien = driver.find_element(By.XPATH, xpath_xe_may_dien)
element_xe_may_dien.click()

# Nhập biển số xe
xpath_input = '//*[@id="bienso"]'
value_bien_so_xe = '38MD-345.45'
element_input = driver.find_element(By.XPATH, xpath_input)
element_input.send_keys(value_bien_so_xe)

# Click vào button
xpath_btn = '//*[@id="submit"]'
element_btn = driver.find_element(By.XPATH, xpath_btn)
element_btn.click()


# Cach 1 Đợi kết qua 
driver.implicitly_wait(10)
# Cách 2 Đợi kết quả
xpath_result = '//*[@id="resultValue"]'
WebDriverWait (driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath_result)))

element_result = driver.find_element(By.XPATH, xpath_result)
text_result = element_result.text
print(text_result)
if 'Không tìm thấy vi phạm phạt nguội' in text_result:
    print('Không tìm thấy vi phạm phạt nguội')
else:
    print('Tìm thấy vi phạm phạt nguội')