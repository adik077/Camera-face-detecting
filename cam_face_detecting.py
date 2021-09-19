import cv2

classifier="face_cascade.xml"
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)       
cascade=cv2.CascadeClassifier(classifier)

while True:
    ret,frame=video.read()
    frame=cv2.flip(frame,1) 
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(image=gray,minNeighbors=5,minSize=(50,50),scaleFactor=1.1)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & (0xFF==ord('q')):
         break
video.release()
cv2.destroyAllWindows()

