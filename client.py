import socket
import threading
import base64
import cv2
import os
import time

def videocapture():
    s = socket.socket()
    ip = "13.126.100.58"
    port = 2027
    s.connect((ip,port))
    i=0
    while True:
        time.sleep(1)
        try:
            data = s.recv(100000000)
            imgdata = base64.b64decode(data)
            filename = "{}.jpg".format(i)
            with open(filename, 'wb') as f:
                f.write(imgdata)
                
            image = "image"+"{}".format(i)
            try:
                image=cv2.imread(filename)
                #print(image)
                cv2.imshow('video app',image)
                os.remove("{}.jpg".format(i))
                i=i+1
                print(i)
                if cv2.waitKey(10)==13:
                    break
            except:
                pass
        except:
            pass
    cv2.destroyAllWindows()
    
def videosender():
    s = socket.socket()
    ip = "13.126.100.58"
    port = 2025
    s.connect((ip,port))
    cap = cv2.VideoCapture(0)
    while True:
        time.sleep(1)
        ret, photo = cap.read()
        cv2.imwrite("videocall.jpg",photo)
        with open("videocall.jpg",'rb') as f:
            image_encoded = base64.b64encode(f.read())
        #print(image_encoded)
        s.send(image_encoded)
x1 = threading.Thread(target=videosender)
x2 = threading.Thread(target=videocapture)

x1.start()
x2.start()
