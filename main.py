import cv2
import easyocr
import matplotlib.pyplot as plt
import os

# read image
image_path = os.path.join('Data','test1.png')

img = cv2.imread(image_path)

# Instance text detector
reader = easyocr.Reader(['en'],gpu=False)

# Detect text on image
text_ = reader.readtext(img)

THRESHOLD = 0.25

for t in text_:
    bbox,text,score = t

    if score>THRESHOLD:
        cv2.rectangle(img,bbox[0],bbox[2],(0,225,0),5)
        cv2.putText(img,text,bbox[0],cv2.FONT_HERSHEY_COMPLEX,0.65,(255,0,0),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()