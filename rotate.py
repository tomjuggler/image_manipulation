# import the Python Image 
# processing Library
from PIL import Image
  
# Giving The Original image Directory 
# Specified
Original_Image = Image.open("./nnn.png")
  
# Rotate Image By 180 Degree
rotated_image1 = Original_Image.rotate(90)
  
# This Will Rotate Image By 60 Degree
  
rotated_image1.show()
rotated_image1.save("nnnRotated.png") # yes! easy with PIL
