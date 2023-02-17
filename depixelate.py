
from PIL import Image
import os

def convert_8bit_color_to_image(bin_file_path):
    with open(bin_file_path, "rb") as bin_file:
        binary_data = bin_file.read()

    # Calculate the dimensions of the output image
    width = 72
    height = (len(binary_data) + width - 1) // width

    # Create an image from the binary data
    output_image = Image.new("RGB", (width, height))
    for i, b in enumerate(binary_data):
        r = (b & 0xE0)
        g = ((b & 0x1C) << 3)
        b = ((b & 0x03) << 6)
        x, y = i % width, i // width
        output_image.putpixel((x, y), (r, g, b))

    # Save the image as a new file
    output_file_path = os.path.splitext(bin_file_path)[0] + "_new.png"
    output_image.save(output_file_path, "PNG")


convert_8bit_color_to_image("./aa.bin");
