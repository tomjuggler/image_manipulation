import sys
from PIL import Image
import os

def compress_image_to_8bit_color(image_path):
    # Open the input image
    input_image = Image.open(image_path)

    binary_data = []

    # Loop over each pixel in the input image and encode it
    for x in range(input_image.width):
        for y in range(input_image.height):
            r, g, b = input_image.getpixel((x, y))
            encoded = ((r & 0xE0) | ((g & 0xE0) >> 3) | (b >> 6))
            binary_data.append(encoded)

    # Calculate the output file path
    output_file_path = os.path.splitext(image_path)[0] + ".bin"

    # Convert the binary data to a binary file
    with open(output_file_path, "wb") as binary_file:
        binary_file.write(bytearray(binary_data))

    return output_file_path


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
    output_image.show() # todo: delete for server version!


if __name__ == "__main__":
    # Get the path of the input file from the command-line arguments
    input_file_path = sys.argv[1]

    # Convert the binary file to an image
    convert_8bit_color_to_image(input_file_path)
