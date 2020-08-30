# Python program to implement
# WebCam Motion Detector

# importing OpenCV, time and Pandas library
import cv2


video = cv2.VideoCapture(0)
#video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

print("Focus the laser light to exact center as shown in image")

# Infinite while loop to treat stack of image as video
while True:

	check, frame = video.read()
	height, width, channels = frame.shape
	cv2.line(frame, (0, 0), (width, height), (0, 0, 255), 2, 1)
	cv2.line(frame, (width, 0), (0,height), (0, 0, 255), 2, 1)
	cv2.line(frame, (int(width/2), 0), (int(width/2),height), (255, 0, 0), 2, 1)
	cv2.line(frame, (width, int(height/2)), (0,int(height/2)), (255, 0, 0), 2, 1)
	cv2.imshow("Color Frame", frame)

	key = cv2.waitKey(1) 
	# if q entered whole process will stop 
	if key == ord('q'): 
		break

video.release() 

# Destroying all the windows 
cv2.destroyAllWindows() 
