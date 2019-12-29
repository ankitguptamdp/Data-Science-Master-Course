# Read a Video Stream from Camera (Frame by Frame)
import cv2

cap=cv2.VideoCapture(0)
# 0 stands for default camera
face_cascade=cv2.CascadeClassifier('../Xml Files/haarcascade_frontalface_alt.xml')

while True:
	ret,frame=cap.read()
	# ret is boolean and symbol of frame captured properly or not
	print(ret)
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret==False:
		continue

	faces=face_cascade.detectMultiScale(frame,1.3,5)
	# 1.3 is Scaling factor
	# 5 is Number of neighbors

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		# it shows a rectangle detecting the face

	cv2.imshow('Video Frame',frame)
	#cv2.imshow('Gray Frame',gray_frame)

	#Wait for user input q then you will stop the loop
	key_pressed=cv2.waitKey(1)&0xFF
	# 1 means wait for 1 ms
	# cv2.waitKey will return 32 bit value
	# and operation will 1111 1111
	# ord() will give ascii value of q
	if key_pressed==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


"""
scaleFactor – Parameter specifying how much the image size is reduced at each image scale.

Basically the scale factor is used to create your scale pyramid. More explanation can be found here. In short, as described here, your model has a fixed size defined during training, which is visible in the xml. This means that this size of face is detected in the image if present. However, by rescaling the input image, you can resize a larger face to a smaller one, making it detectable by the algorithm.

1.05 is a good possible value for this, which means you use a small step for resizing, i.e. reduce size by 5%, you increase the chance of a matching size with the model for detection is found. This also means that the algorithm works slower since it is more thorough. You may increase it to as much as 1.4 for faster detection, with the risk of missing some faces altogether.



minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.

This parameter will affect the quality of the detected faces. Higher value results in less detections but with higher quality. 3~6 is a good value for it.

"""