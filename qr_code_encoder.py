import qrcode

data = input("Enter Text to convert: ")

img = qrcode.make(data)

img.save("QR Code.png")
