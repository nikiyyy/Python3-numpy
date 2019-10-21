#place all the images you want too test in the same folder as the .py file

import cv2
import glob

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
pictures=glob.glob("*.jpg")# vzema vsichko v vuv papkata

for pic in pictures:
    img=cv2.imread(pic,1)
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.15,minNeighbors=5)
    for x,y,w,h in faces:
            img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255<0),3)
            
    #resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
    
    cv2.imshow("changed image", img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()