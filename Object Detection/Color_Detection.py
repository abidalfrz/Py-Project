import cv2
from PIL import Image
from util import get_limits

yellow = [0,255,255]
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(yellow)

    mask = cv2.inRange(hsvImage,lowerLimit,upperLimit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    print(bbox)

    if bbox is not None:
        x1,y1,x2,y2 = bbox

        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 5)

        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, 'yellow', (x1,y1 - 10), font, 1, (0,0,255), 2)
        

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
