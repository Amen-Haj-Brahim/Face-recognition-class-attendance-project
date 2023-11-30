import cv2 as cv
import numpy as np
from PIL import Image
import os
recognizer = cv.face.LBPHFaceRecognizer_create()
path="dataset"
def getPerson(path):
    #put recorded pictures in a list
    imagePath = [os.path.join(path, f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    #looping through images
    for imagePaths in imagePath:
        #converting the image to gray scale
        faceImage = Image.open(imagePaths).convert('L')
        #putting the image in an array
        faceNP = np.array(faceImage)
        #getting the person's id from the pictures name
        Id= (os.path.split(imagePaths)[-1].split(".")[1])
        Id=int(Id)
        faces.append(faceNP)
        ids.append(Id)
        cv.imshow("Training on recorded faces",faceNP)
        cv.waitKey(1)
    return ids, faces
ids, face = getPerson(path)
recognizer.train(face, np.array(ids))
recognizer.write("trainer.yml")
cv.destroyAllWindows()
print("")