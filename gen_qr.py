# pip install qrcode pillow in terminal (if you have a python3.14 use "pip3")
import qrcode

answer = input("Enter the data to encode in the QR code:  ")

img = qrcode.make(answer)

img.save("qrcode.png")

img.show()

print("QR code generated and saved as 'qrcode.png")
