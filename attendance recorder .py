import cv2 as cv
import time
import datetime
import Functions
import Functions
#if you have more than 1 camera on your pc change the parameter of VideoCapture to change it
#note to self : TRY IT WITH DROID CAM AND SEE IF BETTER CAMERA QUALITY MAKES FOR BETTER RESULTS
person=None
video=cv.VideoCapture(0)
facedetect = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
model = cv.face.LBPHFaceRecognizer_create()
model.read("trainer.yml")
#person id list the index in the list is the person's id (for example amen's id is 1)
name_list = ["", "Amen", "Aziz","Amine"]
copy= name_list
lst=Functions.lst_of_students()
#minimum face height and width
minWidth = 0.1*video.get(3)
minHeight = 0.1*video.get(4)
#timer
start=datetime.datetime.now().second + 1
#starting detection
while True:
    #starting camera and mirroring it and flipping it since we flipped it in recording
    counter = (datetime.datetime.now().second - start) #the start of the counter
    ret,frame=video.read()
    frame=cv.flip(frame,1)
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.2, 5,minSize=(int(minWidth), int(minHeight)))
    cv.putText(frame, f'Time: {counter}s', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    #detecting faces
    for (x,y,w,h) in faces:

        serial, conf = model.predict(gray[y:y+h, x:x+w])
        #show timer
        counter+=0

        #show person name
        if conf<45:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            cv.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
            cv.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
            cv.putText(frame, name_list[serial]+str(int(conf)), (x, y-10),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
            #gets the name of the captured person and change their attendance to "Present"
            person=name_list[serial]
            print(person) #test
            for dict in lst:
                if dict["Student"] == person:
                    dict.update({"Attendance":"Present"})

        #show unknown
        else:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            cv.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
            cv.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
            cv.putText(frame, "Unknown"+str(int(conf)), (x, y-10),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
            cv.putText(frame, f'Time: {counter}s', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    frame=cv.resize(frame, (640, 480))
    cv.imshow("Frame",frame)
    # quit with ESC key
    k = cv.waitKey(10) & 0xff
    if k == 27:
        break
    if counter == 20: # when counter reaches 20 seconds it quits
        break

#set as "Absent" for the uncaptured students in the given time
for dict in lst:
    if dict["Attendance"] != "Present":
        dict.update({"Attendance":"Absent"})

video.release()
cv.destroyAllWindows()
#update the attendance_Table
Functions.update_attendance(lst)
#Displays the Menu for the teacher to check
Functions.teacher_menu()