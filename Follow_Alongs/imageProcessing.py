#  Flipping the image
from PIL import Image

#  Opening the image
img = Image.open('kids-room.jpg')

#  Transposing the image
transposed_image = img.transpose(Image.FLIP_LEFT_RIGHT)

#  Save the image to a file in a human understandable format
transposed_image.save('kids-room-transposed.jpg')

print('Done flipping')
