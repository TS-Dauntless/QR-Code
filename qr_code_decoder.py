from pyzbar.pyzbar import decode
from PIL import Image

location = input("Enter QR code location or You can Drag and Drop the file(Without Quotes): ")

img = Image.open(location)

result = decode(img)[0].data

try:
    print(result.decode('ascii'))
except:
    print("Error Occured while decoding the QR with ASCII codec Format.")
    print("This QR may contain Non ASCII Character, only QR with ASCII value are Supported.")
