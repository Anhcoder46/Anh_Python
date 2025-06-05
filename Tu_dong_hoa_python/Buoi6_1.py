from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#Mở chrome
driver.get("https://dau.edu.vn")
#In tiêu đề trang
print(driver.title)

a_selector = 'body > header > div > div > div:nth-child(2) > div > a:nth-child(1)'
element_a = driver.find_element(By.CSS_SELECTORS, a_selector)
element_a.click()

#Đóng trình duyệt
#print.quit()