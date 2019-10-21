"""
import cv2
#import time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
Video= cv2.VideoCapture("VID_20190706_151130.mp4")

while True:
    check, frame = Video.read()
    cv2.imshow("vid",frame)
    key=cv2.waitKey(25)
    if key==ord('x'):
        break

Video.release()
cv2.destroyAllWindows

"""

import cv2
#import time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
Video= cv2.VideoCapture("VID_20190706_151130.mp4") # video input goes here

while True:
    
    check, frame = Video.read()
    modif_Frame=frame
    
    gray_img=cv2.cvtColor(modif_Frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.3,minNeighbors=5)
    for x,y,w,h in faces:
            modif_Frame=cv2.rectangle(modif_Frame, (x,y),(x+w,y+h),(0,255<0),3)
    
    cv2.imshow("vid",modif_Frame)
    key=cv2.waitKey(25)
    if key==ord('x'):
        break

Video.release()
cv2.destroyAllWindows