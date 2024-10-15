import cv2
import matplotlib.pyplot as plt
import easyocr

img = cv2.imread("sign1.jpg")

reader = easyocr.Reader(['en'], gpu = False)

text_ = reader.readtext(img)

thresold = 0.25

for t in text_:
    print(t)

    bbox, text, score = t
    
    if score > thresold:
        cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 5)

        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, text, bbox[0], font, 1, (0,0,255), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
