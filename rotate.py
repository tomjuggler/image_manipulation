
from PIL import Image
  
Original_Image = Image.open("./nnn.png")
  
# rotate image 90 degrees to the right
rotated_image1 = Original_Image.rotate(90)
  
rotated_image1.show()
rotated_image1.save("nnnRotated.png") # yes! easy with PIL
