import numpy as np
import cv2

class ObjectDetector():
    def detect_colourshape(lower, upper, image):
        lower_bound = np.array(lower)
        upper_bound = np.array(upper)

        mask = cv2.inRange(image, lower_bound, upper_bound)

        kernelOpen=np.ones((5,5))
        kernelClose=np.ones((20,20))

        maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

        maskFinal=maskClose
        _,conts,_=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(image,conts,-1,(255,0,0),3)
        for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            print(cv2.boundingRect(conts[i]))
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255), 2)

        cv2.imwrite('./images/01.png',image)