import qrcode
from PIL import Image
data=input('Enter the text or URL: ').strip()
filename=input('Enter the filename to save the QR code:').strip()
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
qr.make_image(fill_color="pink", back_color="black").save(filename + '.png')