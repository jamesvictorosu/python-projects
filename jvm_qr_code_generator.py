# JVM Generate QR Code program
# This program leverages the Python qrcode module to generate a QR Code image with an embedded URL or text
import qrcode

# Get user inputs
data = input("Enter the website URL or text: ").strip()
filename = input('Enter the filename (without extension): ').strip()


# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border width (4 is the minimum)
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
image = qr.make_image(fill='black', back_color='white')

# Save the image as a .png file with the given filename
image.save(f"{filename}.png")

print(f"QR code saved as {filename}.png")
