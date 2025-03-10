import cv2
import numpy as np
import sqlite3

#detection
faceDetectionHelper= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webCam=cv2.VideoCapture(0)

#database insertion and updation
def insertOrUpdateIntoDatabase(Id,Name,Age):
    connection=sqlite3.connect("initialDatabase.db")
    cmd = "SELECT * FROM STUDENTS WHERE ID="+str(Id)
    cursor=connection.execute(cmd)
    isRecordExists = 0
    for row in cursor:
        isRecordExists=1
    if(isRecordExists==1):
        connection.execute("UPDATE STUDENTS SET Name=? WHERE Id=?",(Name,Id))
        connection.execute("UPDATE STUDENTS SET Age=? WHERE Id=?",(Age,Id))
    else:
        connection.execute("INSERT INTO STUDENTS (Id,Name,Age) values(?,?,?)",(Id,Name,Age))
    
    connection.commit()
    connection.close()
Id=input("Enter Employee ID")
Name=input("Enter Employee Name")
Age=input("Enter Employee Age")
insertOrUpdateIntoDatabase(Id,Name,Age)