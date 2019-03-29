from window import Window
import numpy as np
import cv2
from cursor import Cursor
from PIL import ImageGrab
from object_finder import ObjectDetector
import json


def main():
    runelite = Window('RumbIe')
    runelite.focus()
    runelite.resize(x=0,y=0,w=1000,h=700, absolute=True)
    cursor = Cursor()
    
    with open('miningConfig.json') as json_file:
        config = json.load(json_file)
        lower = config['iron']['bgr']['lower']
        upper = config['iron']['bgr']['upper']

    image = np.array(ImageGrab.grab(runelite.bbox))
    ColourObjectFinder.inColourRange(lower,upper,image)



if __name__ == '__main__':
    main()
