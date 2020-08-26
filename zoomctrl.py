#!/usr/bin/env python3
import cv2

scale = 2

cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
x = 640
y = 480

while True:

    ret_val, image = cam.read()
    # get the webcam size
    height, width, channels = image.shape
    #print("height is ",height)
    #print("width is",width)
    # prepare the crop
    #centerX, centerY = int(height/2), int(width/2)
    #radiusX, radiusY = int(scale*height/100), int(scale*width/100)

    #minX, maxX = centerX-radiusX, centerX+radiusX
    #minY, maxY = centerY-radiusY, centerY+radiusY
    cv2.imshow("original", image)
    minX = int(x/scale)
    maxX = int((x/scale)+(width-(width/scale)))
    minY = int(y/scale)
    maxY = int((y/scale)+(height-(height/scale)))
    #cropped = image[minY:maxY, minX:maxX]
    #resized_cropped = cv2.resize(cropped, (width, height))

    #cv2.imshow('Zoomed', resized_cropped)

    key = cv2.waitKey(1)

    # if q entered whole process will stop
    if key == ord('q'):
        break

    if key == ord('-'):
        if scale > 1.1:
            scale -= 0.1  # 
    if  key == ord('+'):
        if scale <10:
            scale += 0.1

    # add + or - 5 % to zoom

    #print("scale is ", scale)

cv2.destroyAllWindows()
