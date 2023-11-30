import cv2 as cv 
#if you have more than 1 camera on your pc change the parameter of VideoCapture to change it
#note to self : TRY IT WITH DROID CAM AND SEE IF BETTER CAMERA QUALITY MAKES FOR BETTER RESULTS
video=cv.VideoCapture(0)
facedetect = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
model = cv.face.LBPHFaceRecognizer_create()
model.read("trainer.yml")
#person id list the index in the list is the person's id (for example amen's id is 1)
name_list = ["", "amen", "aziz","Chouaieb"] 
#minimum face height and width
minWidth = 0.1*video.get(3)
minHeight = 0.1*video.get(4)
#starting detection
while True:
    #starting camera and mirroring it and flipping it since we flipped it in recording
    ret,frame=video.read()
    frame=cv.flip(frame,1)
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.2, 5,minSize=(int(minWidth), int(minHeight)))
    #detecting faces
    for (x,y,w,h) in faces:
        serial, conf = model.predict(gray[y:y+h, x:x+w])
        #show person name
        if conf<40:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            cv.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
            cv.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
            cv.putText(frame, name_list[serial]+str(int(conf)), (x, y-10),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
        #show unknown
        else:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            cv.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
            cv.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
            cv.putText(frame, "Unknown"+str(int(conf)), (x, y-10),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
    frame=cv.resize(frame, (640, 480))
    cv.imshow("Frame",frame)
    # quit with ESC key
    k = cv.waitKey(10) & 0xff
    if k == 27:
        break
video.release()
cv.destroyAllWindows()