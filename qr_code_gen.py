import qrcode

print("Type whatever you want to generate a QR Code (Text, URL, ...):")
txt_to_qr = input()

qr = qrcode.QRCode(border=1)
qr.add_data(txt_to_qr)
qr.make(fit=True)

qr.print_ascii(invert=True)

img = qr.make_image()
img.save(f"QR_Codes/{txt_to_qr[:10]}{'...' if len(txt_to_qr) > 10 else ''}_QRcode.png")
