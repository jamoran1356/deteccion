import cv2
import winsound


cap = cv2.VideoCapture(0)

while True: 
    _, cam = cap.read()
    _, cam2 = cap.read()
    diff = cv2.absdiff(cam, cam2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(cam, contours, -1,(0,255,0), 2)
    for cnt in contours:
        if cv2.contourArea(cnt)<5000:
            continue
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(cam,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.PlaySound("alarma.wav",winsound.SND_ASYNC)
        break

    if cv2.waitKey(10) == ord("q"):
        break

    cv2.imshow("Detector de postura incorrecta", cam)
