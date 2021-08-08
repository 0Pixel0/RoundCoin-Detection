import numpy as np
import cv2 as cv 
img=cv.imread('Photos/coins.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
mblur=cv.medianBlur(gray,5)
canny=cv.Canny(mblur,100,175)
cv.imshow('coins',canny)
circ=cv.HoughCircles(mblur,cv.HOUGH_GRADIENT,1.1,20,param1=60,param2=30,minRadius=20,maxRadius=40)#dp is inverse ratio of accumalatorresolution to image resolution

if circ is not None:
    circ=np.round(circ[0,:]).astype('int')

for (x,y,r) in circ:
    cv.circle(img,(x,y),r,(0,255,0),4)
    cv.imshow("detected coin",img)

cv.waitKey(0)