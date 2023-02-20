from PIL import Image
import sys
import os

# todo: remember this needs to be done after rotate! 

def resize_image(file, fixed_width):
    basewidth = fixed_width
    im = Image.open(file)
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    img = im.resize((basewidth,hsize), Image.Resampling.LANCZOS)

    # Save the image as a new file
    output_file_path = os.path.splitext(file)[0] + "_resized.png"
    img.save(output_file_path, "PNG")
    img.show() # todo: not for server version!

if __name__ == "__main__":
    # Get the path of the input file from the command-line arguments
    input_file_path = sys.argv[1]

    # Convert the binary file to an image
    resize_image(input_file_path, 72)