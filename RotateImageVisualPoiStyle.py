from PIL import Image
import sys
import os
import math

def rotate_visual_poi_style(file, fixed_width):
    # resize
    basewidth = fixed_width
    im = Image.open(file)
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    img = im.resize((basewidth,hsize), Image.Resampling.LANCZOS)
    img_rotated = img.rotate(-90) # rotate 90 degrees clockwise 
    # start rotate image now: 
    fit = 1
    if (img_rotated.height > 360):
        fit = 1
    else:
        fit = 360 // img_rotated.height # using original width - because height doesn't change after rotate! # todo: rotate not working at all! 

    # create a blank image and rotate the input image onto it multiple times
    # to create the final spinning effect

    new_height = int(360 // fit)
    newImg = Image.new(mode="RGB", size=(400, 400)) # todo: change for different size poi? 

    # resize for rotation: 
    img_rotated = img_rotated.resize((img_rotated.width, new_height), Image.Resampling.LANCZOS)

    
    incrRotation = 0
    while incrRotation < 360:
        w, h = img_rotated.size
        for y in range(h):
            for x in range(w):
                adjacent = int((x+90) * math.sin(math.radians(-y+incrRotation)))
                opposite = int((x+90) * math.cos(math.radians(-y+incrRotation)))
                pixel_color = img_rotated.getpixel((x, y))
                set_x = adjacent + (newImg.width // 2)
                set_y = opposite + (newImg.height // 2)
                newImg.putpixel((set_x, set_y), pixel_color)
        incrRotation += new_height

    # save the resulting image with the same name as the input image
    newImg.save(file + "_VPS.jpg")
    newImg.show()

if __name__ == "__main__":
    # Get the path of the input file from the command-line arguments
    input_file_path = sys.argv[1]

    # Convert the binary file to an image
    rotate_visual_poi_style(input_file_path, 100)