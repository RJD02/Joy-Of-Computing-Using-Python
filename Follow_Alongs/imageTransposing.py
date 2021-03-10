#  Flipping the image
from PIL import Image

#  Opening the image
img_input = input('Enter the file name that you want to flip: ')
#  img = Image.open('kids-room.jpg')
img = Image.open(img_input)

#  Transposing the image
transposed_image = img.transpose(Image.FLIP_LEFT_RIGHT)

#  Save the image to a file in a human understandable format
#  transposed_image.save('kids-room-transposed.jpg')
#  print(img_input[:-4] + '-transposed' + img_input[-4:])

transposed_image.save(img_input[:-4] + '-transposed' + img_input[-4:])

print('Done flipping')
