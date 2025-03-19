import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path="dataset"

def getImagesWithID(path):
    imagesPaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces= []
    ids= []
    for single_employee_image in imagesPaths:
        faceImg = Image.open(single_employee_image).convert('L')
        faceNp = np.array(faceImg,np.uint8)
        id = int(os.path.split(single_employee_image)[-1].split(".")[2])
        print(id)
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow("Traingin Employee Data",faceNp)
        cv2.waitKey(10)

    return np.array(ids),faces

ids,faces = getImagesWithID(path)



recognizer.train(faces,ids)
recognizer.save("train/trainingDataOfEmployees.yml")
cv2.destroyAllWindows()