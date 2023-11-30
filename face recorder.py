import cv2 as cv
video=cv.VideoCapture(0)
facedetect = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
id = input("Student ID ?")
count=0
while True:
    #camera and saving setup    
    ret,frame=video.read()
    frame=cv.flip(frame,1)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.1, 3)
    for (x,y,w,h) in faces:
        count=count+1
        #save face and put square on it
        cv.imwrite('dataset/User.'+str(id)+"."+str(count)+".jpg", gray[y:y+h, x:x+w])
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
        #show how many images left
        cv.putText(frame,str(500-count),(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
    #window name
    cv.imshow("Face recorder",frame)
    #exit with ESC key
    k = cv.waitKey(10) & 0xff
    if k == 27:
        break
    if count>500:
        break
video.release()
cv.destroyAllWindows()
print("Person recording complete")
