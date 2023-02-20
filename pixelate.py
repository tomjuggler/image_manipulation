from PIL import Image
import os
import sys

def compress_image_to_8bit_color(image_path):
    # Open the input image
    input_image = Image.open(image_path)
    binary_data = []

    # todo: resize image to pre-defined poi size
    # todo: rotate image 90 degrees for viewing on the poi 
    
    # Loop over each pixel in the input image and encode it
    for x in range(input_image.height):
        for y in range(input_image.width):
            r, g, b = input_image.getpixel((y, x))
            encoded = ((r & 0xE0) | ((g & 0xE0) >> 3) | (b >> 6))
            print(encoded)
            binary_data.append(encoded)
            
    # Convert the PNG file to a binary file
    with open(os.path.splitext(image_path)[0] + ".bin", "wb") as binary_file:
        binary_file.write(bytearray(binary_data))
        
if __name__ == "__main__":
    # Get the path of the input file from the command-line arguments
    input_file_path = sys.argv[1]

    # Convert the binary file to an image
    compress_image_to_8bit_color(input_file_path)

