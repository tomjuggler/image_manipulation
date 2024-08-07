
from PIL import Image
  
Original_Image = Image.open("./c.jpg")
Original_Image.show()
# rotate image 90 degrees to the right
# TODO: use transpose here
# rotated_image1 = Original_Image.rotate(-90) # that's right, positive means counter-clockwise folks. Who thought up this bright idea? 
# rotated_image1 = Original_Image.transpose(Image.ROTATE_270)
rotated_image1 = Original_Image.rotate(-90, expand=True)
rotated_image1.show()
rotated_image1.save("aRotated.png") # yes! easy with PIL
