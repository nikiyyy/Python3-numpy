import cv2  #pip install opencv-python
#import time
#face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
Video= cv2.VideoCapture("VID_20190706_193858.mp4") # video input goes here

background=None

while True:
    check, frame = Video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if background is None:
        background=gray
        continue
    
    key=cv2.waitKey(30)
    
    frame_AD=cv2.absdiff(background,gray)
    frame_threshold=cv2.threshold(frame_AD, 30, 255, cv2.THRESH_BINARY)[1]
    if key==ord('x'):
        break
    
    (cnts,_)=cv2.findContours(frame_threshold.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour)<2500:
            continue
    (x,y,w,h)=cv2.boundingRect(contour)
    cv2.rectangle(frame, (x,y),(x+w, y+h),(0,255,0),3)
    
    cv2.imshow("vid",frame)
    cv2.imshow("vid2",frame_threshold)
Video.release()
cv2.destroyAllWindows