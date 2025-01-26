import qrcode

print("Type whatever you want to generate a QR Code (Text, URL, ...):")
txt_to_qr = input()


qr = qrcode.QRCode(border=1)
qr.add_data(txt_to_qr)
qr.make(fit=True)

qr.print_ascii(invert=True)

if '/' in txt_to_qr:
    txt_to_qr = txt_to_qr.replace('/', '|')
if 'http' in txt_to_qr:
    txt_to_qr = txt_to_qr[txt_to_qr.find('www')+4:]

img = qr.make_image()
img.save(f"QR_Codes/{txt_to_qr[:10]}{'...' if len(txt_to_qr) > 10 else ''}_QRcode.png")
