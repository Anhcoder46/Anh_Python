import pyqrcode
import png
link = "https://github.com/Anhcoder46/"
qr_code = pyqrcode.create(link)
qr_code.png("git.png", scale = 5)