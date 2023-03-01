
from PIL import Image
  
Original_Image = Image.open("./a.jpg")
  
# rotate image 90 degrees to the right
rotated_image1 = Original_Image.rotate(-90) # that's right, positive means counter-clockwise folks. Who thought up this bright idea? 
  
rotated_image1.show()
rotated_image1.save("aRotated.png") # yes! easy with PIL
