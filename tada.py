from PIL import Image, ImageDraw, ImageFont
import shutil

# Créer une nouvelle image
image = Image.new('RGB', (800, 800), color='white')
draw = ImageDraw.Draw(image)

# Ajouter du texte à l'image
font = ImageFont.truetype('arial.ttf', size=50)
text = "Mon NFT"
text_width, text_height = draw.textsize(text, font=font)
text_position = ((800 - text_width) // 2, (800 - text_height) // 2)
draw.text(text_position, text, font=font, fill='black')

# Enregistrer l'image en tant que fichier NFT
image.save('mon_nft.png')
# Encrypt the colorimetry
encrypted_colorimetry = encrypt_colorimetry(colorimetry)

# Add the encrypted colorimetry to the image metadata
image.info['colorimetry'] = encrypted_colorimetry
# Encrypt the color spectrums
encrypted_red_spectrum = encrypt_spectrum(red_spectrum)
encrypted_green_spectrum = encrypt_spectrum(green_spectrum)
encrypted_blue_spectrum = encrypt_spectrum(blue_spectrum)

# Add the encrypted color spectrums to the image metadata
image.info['red_spectrum'] = encrypted_red_spectrum
image.info['green_spectrum'] = encrypted_green_spectrum
image.info['blue_spectrum'] = encrypted_blue_spectrum

# Get the colorimetry from the image metadata
encrypted_colorimetry = image.info['colorimetry']
# Decrypt the colorimetry
colorimetry = decrypt_colorimetry(encrypted_colorimetry)
# Get the red, green, and blue spectrums from the image metadata
encrypted_red_spectrum = image.info['red_spectrum']
encrypted_green_spectrum = image.info['green_spectrum']
encrypted_blue_spectrum = image.info['blue_spectrum']
# Decrypt the red, green, and blue spectrums
red_spectrum = decrypt_spectrum(encrypted_red_spectrum)
green_spectrum = decrypt_spectrum(encrypted_green_spectrum)
blue_spectrum = decrypt_spectrum(encrypted_blue_spectrum)

# Assign colors to each shade in the NFT
color_palette = {}
for shade in colorimetry:
    red = red_spectrum[shade]
    green = green_spectrum[shade]
    blue = blue_spectrum[shade]
    color_palette[shade] = (red, green, blue)

# Use the color palette to assign colors to the image pixels
pixels = image.load()
for x in range(image.width):
    for y in range(image.height):
        pixel_color = color_palette[colorimetry[x, y]]
        pixels[x, y] = pixel_color
        # Generate a key for color mapping
        key = {}
        for shade, color in color_palette.items():
            key[color] = shade

        # Save the key as a JPEG file
        key_image = Image.new('RGB', (200, 200))
        key_draw = ImageDraw.Draw(key_image)
        key_font = ImageFont.truetype('arial.ttf', size=20)
        key_text_position = (10, 10)
        for color, shade in key.items():
            key_draw.rectangle([(10, key_text_position[1]), (30, key_text_position[1] + 20)], fill=color)
            key_draw.text((40, key_text_position[1]), shade, font=key_font, fill='black')
            key_text_position = (key_text_position[0], key_text_position[1] + 30)
        key_image.save('color_key.jpeg')
        
        # Save the image as an NFT file without encrypted data
        image.save('mon_nft.png')

        # Create a compressed folder for the encrypted NFT data
        shutil.make_archive('encrypted_nft_data', 'zip', '.', 'encrypted_data')
# Save the image as an NFT file
image.save('mon_nft.png')
# Compare the size of each folder
original_size = shutil.disk_usage('.').used
compressed_size = shutil.disk_usage('encrypted_nft_data.zip').used

# Calculate the reduction in size
reduction_percentage = (original_size - compressed_size) / original_size * 100

# Print the reduction percentage
print(f"The compressed folder is {reduction_percentage:.2f}% smaller than the original folder.")
# Generate a key for color mapping
key = {}
for shade, color in color_palette.items():
    key[color] = shade
    
