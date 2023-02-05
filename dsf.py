pixel_encrypt = lambda pixel, key: (pixel ^ ((key + 5) % 6))

pixel = int(input("Enter the value of the pixel (0-255): "))
key = int(input("Enter the encryption key (0-255): "))

for i in range(5):
    pixel = pixel_encrypt(pixel, key)

print("The encrypted pixel value is:", pixel)
