#  Image enhancement code using CLAHE
import cv2

#  Read the image
file_name = input('Enter the file name that you want to enhance: ')
#  img = cv2.imread('kids-room.jpg')
img = cv2.imread(file_name)

#  Preparation for applying CLAHE
clahe = cv2.createCLAHE()

#  Converting the image into Grey-scale image
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#  Apply enhancement process
enh_image = clahe.apply(gray_image)

#  Save it in a file
#  cv2.imwrite('kids-room-enhanced.jpg', enh_image)
cv2.imwrite(file_name[:-4] + '-enhanced' + file_name[-4:])

print('Done enhancing')
