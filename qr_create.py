import qrcode
qr_img = qrcode.make('https://co-de.tistory.com/')
qr_img.save('/Users/hongyoolee/document/study/qrcode/test_qr.png')

