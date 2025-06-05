#def handle_data():
#    print("Xử lý dữ liệu")
#    
#def send_email():
#    print("Gửi email")
#   
#def update_status():
#    print("Cập nhật trạng thái")
#    
#while True:
#   handle_data()
#
#   send_email()
#
#    update_status()

import datetime
from Buoi6_PhatNguoi import crawl_genk
from Buoi5 import crawl_genk

while True:
    #1. Lấy số giờ hiện tại so sánh với 8h
    current_time = datetime.datetime.now()
    print("Giờ hiện tại: ", current_time)
    int_hour = current_time.hour
    
    if int_hour == 7:
        #2. Lấy dữ liệu tin tức mới
        crawl_genk()