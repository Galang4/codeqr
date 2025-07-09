import qrcode

website_link = input("Enter the YouTube channel link: ")


qr = qrcode.QRCode(version = 10, box_size = 5, border = 3)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')

img.show()