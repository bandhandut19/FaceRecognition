import cv2
import numpy as np
import sqlite3

#detection
faceDetectionHelper= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webCam=cv2.VideoCapture(0)

#database insertion and updation
def insertOrUpdateIntoDatabase(Id,Name,Age):
    connection=sqlite3.connect("employeeDatabase.db")
    cmd = "SELECT * FROM EMPLOYEES WHERE ID="+str(Id)
    cursor = connection.cursor()
    cursor=connection.execute(cmd)
    isRecordExists = 0
    for row in cursor:
        isRecordExists=1
    if(isRecordExists==1):
        connection.execute("UPDATE EMPLOYEES SET Name=? WHERE Id=?",(Name,Id))
        connection.execute("UPDATE EMPLOYEES SET Age=? WHERE Id=?",(Age,Id))
    else:
        connection.execute("INSERT INTO EMPLOYEES (Id,Name,Age) values(?,?,?)",(Id,Name,Age))
    
    connection.commit()
    connection.close()
Id=input("Enter Employee ID")
Name=input("Enter Employee Name")
Age=input("Enter Employee Age")
insertOrUpdateIntoDatabase(Id,Name,Age)


#face detection in web cam using openCV
sampleNumber=0
while(True):
    ret,employeeImg=webCam.read()
    gray=cv2.cvtColor(employeeImg,cv2.COLOR_BGR2GRAY) #converting image color to gray
    faces=faceDetectionHelper.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        sampleNumber=sampleNumber+1
        cv2.imwrite("dataset/flora."+str(Name)+"."+str(Id)+"."+str(sampleNumber)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(employeeImg,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow("EmployeeFace",employeeImg)
    cv2.waitKey(100)
    if(sampleNumber>20):
        break;

webCam.release()
cv2.destroyAllWindows()
