import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
data="Hello it's Me vinayak"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="balck",back_color="white")
img.save("1.png")