# Simple Program to read and show an image

import cv2

img = cv2.imread('../Images/dog.png')
gray = cv2.imread('../Images/dog.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Dog Image',img)
cv2.imshow('Gray Dog Image',gray)

#cv2.waitKey(0) # Infinite Waiting # Program will stop when any key is pressed
cv2.waitKey(2500) # 2.5 seconds
cv2.destroyAllWindows() 
