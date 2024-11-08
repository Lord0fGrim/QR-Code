import qrcode

# Data to encode
data = "https://www.example.com"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,            # controls the size of the QR code (1 is a small box)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,          # controls how many pixels each "box" of the QR code is
    border=4,             # controls the thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")
