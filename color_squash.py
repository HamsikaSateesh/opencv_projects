import cv2
import numpy as np
def track(flag):
   pass
capture=cv2.VideoCapture(0)
cv2.namedWindow('window')
cv2.createTrackbar('lower_hue','window',0,255,track)
cv2.createTrackbar('upper_hue','window',255,255,track)
cv2.createTrackbar('lower_satuaration','window',0,255,track)
cv2.createTrackbar('upper_saturation','window',255,255,track)
cv2.createTrackbar('lower_value','window',0,255,track)
cv2.createTrackbar('upper_value','window',255,255,track)
while True:
    ret,frame=capture.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos('lower_hue','window')
    u_h=cv2.getTrackbarPos('upper_hue','window')
    l_s=cv2.getTrackbarPos('lower_satuaration','window')
    u_s=cv2.getTrackbarPos('upper_saturation','window')
    l_v=cv2.getTrackbarPos('lower_value','window')
    u_v=cv2.getTrackbarPos('upper_value','window')

    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])

    range=cv2.inRange(hsv,l_b,u_b)

    res=cv2.bitwise_and(frame,frame,mask=range)

    cv2.imshow('frame',frame)
    cv2.imshow('range',range)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0XFF ==27:
        break

    cv2.imshow('image',res)
capture.release()
cv2.destroyAllWindows()