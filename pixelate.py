from PIL import Image
import os

def compress_image_to_8bit_color(image_path):
    # Open the input image
    input_image = Image.open(image_path)
    binary_data = []
    # bytes = bytearray()


    # Loop over each pixel in the input image and encode it
    for x in range(input_image.width):
        for y in range(input_image.height):
            r, g, b = input_image.getpixel((x, y))
            encoded = ((r & 0xE0) | ((g & 0xE0) >> 3) | (b >> 6))
            print(encoded)
            binary_data.append(encoded)
            # bytes.append(encoded)

    # Convert the PNG file to a binary file
    with open(os.path.splitext(image_path)[0] + ".bin", "wb") as binary_file:
        binary_file.write(bytearray(binary_data))
        # binary_file.write(bytes)



compress_image_to_8bit_color("./nnn.png")


