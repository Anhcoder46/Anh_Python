import schedule
import time
from Buoi_5 import send_email

# def send_email():
#     print("Gửi email báo cáo")
    
    
#1. 8h sáng
schedule.every().day.at("08:00").do(send_email)

#1. 16h40 chiều
schedule.every().day.at("16:40").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)