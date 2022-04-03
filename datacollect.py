import cv2
import os
video=cv2.VideoCapture(0)
# facedetect = cv2.CascadeClassifier("C:/Users/HP/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_eye.xml")
facedetect = cv2.CascadeClassifier("D:/facial_recognition/images/hnad1.xml")
count = 0
nameID=str(input("ENTER YOU NAME: ")).lower()
path="D:/facial_recognition/images/"+nameID
isExist = os.path.exists(path)
if isExist:
    print("name Already Taken")
    nameID=str(input("ENter Your Name Again: "))
else:
    os.makedirs(path)

while True:
    ret, frame=video.read()
    faces=facedetect.detectMultiScale(frame, 1.3, 8)
    for x,y,w,h in faces:
        count = count+1
        name='./images/'+nameID+'/'+str(count)+'.jpg'
        print("creating image.........................."+name)
        cv2.imwrite(name, frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    cv2.imshow("windowFrame",frame)
    cv2.waitKey(1)
    if count>100:
        break
video.release()
cv2.destroyAllWindows()
