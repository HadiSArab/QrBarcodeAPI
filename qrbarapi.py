from crypt import methods

import requests
from flask import Flask, request, redirect, url_for
from flask import render_template
import json
import cv2
import numpy as np
from pyzbar.pyzbar import decode

app = Flask(__name__)


@app.route('/qrbarcode')
def code():
    url = request.args['url']
    url = str(url)

    # perform request ..... sample url : 'https://i.stack.imgur.com/Mspmr.png'
    response =  requests.get(url).content
    # convert to array of ints
    nparr = np.frombuffer(response, np.uint8)
    # convert to image array
    img = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
    
    # img = cv2.imread('/home/hadi/Projects/QRBarcodeAPI/QrBarcodeAPI/QrCodeBarCode/Images/Vitamin.png')
    
    # cap = cv2.VideoCapture(0)
    # cap.set(3,640)
    # cap.set(4,480)

    with open('/home/hadi/Projects/QRBarcodeAPI/QrBarcodeAPI/QrCodeBarCode/myDataFile.text') as f:
        myDataList = f.read().splitlines()



    # success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        # print(myData)

        # if myData in myDataList:
        #     myOutput = 'Authorized'
        #     myColor = (0,255,0)
        # else:
        #     myOutput = 'Un-Authorized'
        #     myColor = (0, 0, 255)

        # pts = np.array([barcode.polygon],np.int32)
        # pts = pts.reshape((-1,1,2))
        # cv2.polylines(img,[pts],True,myColor,5)
        # pts2 = barcode.rect
        # cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
        #             0.9,myColor,2)
        
    return myData
    # cv2.imshow('Result',img)
    # cv2.waitKey(1)

    
