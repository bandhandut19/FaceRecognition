import cv2
import numpy as np
import sqlite3

#detection
faceDetectionHelper= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webCam=cv2.VideoCapture(0)

#database
def insertOrUpdate(Id,Name,Age):
    connection=sqlite3.connect("initialDatabase.db")
    cmd = "SELECT * FROM STUDENTS WHERE ID="+str(Id)
    cursor=connection.execute(cmd)
    

