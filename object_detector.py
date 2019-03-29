import cv2
import operator
import numpy as np
import random

class ObjectDetector():

    @staticmethod
    def inColourRange(image, lower, upper, boxes_to_take = 3, debug=False):
        mask = cv2.inRange(image, lower, upper)

        kernelOpen = np.ones((5,5))
        kernelClose = np.ones((20,20))

        maskOpen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        maskClose = cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

        maskFinal = maskClose
        _, conts, _ = cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        #cv2.drawContours(image,conts,-1,(255,0,0),3)

        detectedBoxes = { cv2.boundingRect(cont): cv2.boundingRect(cont)[2] * cv2.boundingRect(cont)[3]  for cont in conts }
        topNByArea = sorted(detectedBoxes.items(), key=operator.itemgetter(1), reverse=True)[:boxes_to_take]
        print(topNByArea)
        topNBoxes = [ a[0] for a in topNByArea if a[1] > 150 ]

        if debug:
            for bbox in topNBoxes:
                x,y,w,h = bbox
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255), 2)
            
            cv2.imwrite(f'./images/{random.randint(0,100000)}.png',image)

        return topNBoxes
