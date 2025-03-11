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