import cv2
import numpy as np

lower_red = np.array([160,100,100])
upper_red = np.array([180,255,255])

cap = cv2.VideoCapture(0)
canvas = None
prev_pt = None

while True:
    ret,frame = cap.read()
    
    if not ret:
        break
    
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv,lower_red,upper_red)
    
    contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    if canvas is None:
        canvas = np.zeros_like(frame)
        
    if contours and cv2.contourArea(max(contours,key = cv2.contourArea))>1000:
        c = max(contours,key = cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"]!=0:
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame,(cx,cy),7,(0,0,255),-1)
        
        if prev_pt is not None:
             cv2.line(canvas,prev_pt,(cx,cy),(0,0,255),5)
            
        prev_pt = (cx,cy)
    else:
        prev_pt = None    
    
    output = cv2.addWeighted(frame,0.6,canvas,0.4,0)
    cv2.putText(output,"q to quit| c to clear",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
    
    cv2.imshow("virtual output",output)
    cv2.imshow("mask",mask)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    if key == ord('c'):
        canvas = np.zeros_like(frame)
        prev_pt = None

cap.release()
cv2.destroyAllWindows()
    
    