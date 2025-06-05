import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup
import pandas as pd

def send_email(sender, receiver, subject, body, password):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        print(f"Email đã gửi thành công đến {receiver}")
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

def get_news():
    url = "https://genk.vn/tin-ict.chn"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        news = soup.findAll('h4', class_='knswli-title')

        data = []
        for new in news[:5]:  # Lấy 5 bài mới nhất
            title = new.text.strip()
            link = "https://genk.vn" + new.find('a')['href']
            summary = new.find_next("span", class_="knswli-sapo")
            summary_text = summary.text.strip() if summary else "Không có tóm tắt."

            data.append(f"- {title}\n{summary_text}\n{link}\n")

        return "\n".join(data)
    return "Không thể lấy dữ liệu."

if __name__ == "__main__":
    sender_email = "tranduanh045@gmail.com"
    #Bật xác thực 2 bước
    #Tao App Password
    app_password = "aihw geas ejpw lqiz"
    receiver_email = "tranthihatrang0902@gmail.com" 
    news_content = get_news()
    subject = "Tin tức công nghệ mới nhất từ Genk"
    body = f"Dưới đây là những tin tức mới nhất:\n\n{news_content}"
    send_email(sender_email, receiver_email, subject, body, app_password)