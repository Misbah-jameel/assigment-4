import qrcode 


data = 'Don/t forget to connect me on linkedin'
qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'red',back_color ='white')

# img.save(img = qrcode.make(data)
img.save('C:/Users/FATTANI COMPUTERS/Desktop/PYTHON/save-it/myqrcode.png')


