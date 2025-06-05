import requests
# pip install requests


from bs4 import BeautifulSoup

# pip install BeautifulSoup

import pandas as pd

# pip install pandas

# 1gửi HTTP requests đến trang web 
response = requests.get("https://www.24h.com.vn")

# 2. Kiểm tra  nếu requests thành công

if response.status_code == 200:
    # 3. Kiểm tra BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.content, "html.parser")
    # 4. Tìm kiếm các bài váo có thẻ h4 và class="knswli-title"
    news = soup.findAll('h4', class_='cate-24h-car-news-rand_info')
    print(news)

    links = [link.find('a').attrs["href"] for link in news]
    print(links)

    data = []
    #5. Đối với mỗi bài báo , lấy tiêu đề , tóm tắt, nội dung, link ảnh bài
    #list_new = [1, 2, 3]

    for link in links:
        news = requests.get("https://www.24h.com.vn/" + link)
        soup = BeautifulSoup(news.content, "html.parser")
        title = soup.find("h1", class_="kbwc-title clearfix").text
        summary = soup.find("h2", class_="knc-sapo").text
        body = soup.find("div", id="ContentDetail")
        try:
            content = body.decode_contents()
        except:
            content = ""
        
        try:
            image = body.find("img").arrts["src"]
        except:
            image = ""

        item = [title, summary, content, image]
        data.append(item)