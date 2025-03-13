import os
import cv2
import numpy as np
import sqlite3


faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)


recognizer= cv2.face.LBPHFaceRecognizer_create()
recognizer.read("train/trainingDataOfEmployees.yml")

def getProfile(id):
    connection= sqlite3.connect("employeeDatabase.db")
    cursor= connection.execute("SELECT * FROM EMPLOYEES WHERE id=?",(id,))
    profile= None
    for row in cursor:
        profile=row
    connection.close()
    return profile

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetector.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf= recognizer.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        print(profile)
        if(profile!=None):
            cv2.putText(img, "Name: " + str(profile[1]), (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
            cv2.putText(img, "Id: " + str(profile[2]), (x, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
            # cv2.putText(img, "Age: " + str(profile[3]), (x, y + h + 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
          
    cv2.imshow("Recognize Employee of Flora Systems",img)
    if(cv2.waitKey(1)==ord('q')):
        break;

cam.release()
cv2.destroyAllWindows()