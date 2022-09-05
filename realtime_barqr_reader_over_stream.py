import pyscreenshot as ImageGrab
import numpy as np
import cv2
from pyzbar.pyzbar import decode

while True:


    cap = ImageGrab.grab()
    img = np.asanyarray(cap)

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
