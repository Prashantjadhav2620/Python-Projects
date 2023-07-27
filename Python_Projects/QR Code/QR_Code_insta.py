

# pip install PyQRCode
# pip install pypng


import pyqrcode
# import png

link ="https://www.instagram.com/pj_1610/"

# qr = pyqrcode.create(link)
# qr.png("instagram.png",scale=5)

import pyqrcode
import png
# link = "https://www.instagram.com/the.clever.programmer/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)