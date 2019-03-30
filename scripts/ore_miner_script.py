import json
import time
from object_detector import ObjectDetector
from camera import Camera
import numpy as np

class OreMinerScript():
    def __init__(self, ore, window, cursor, numberOfRocks):
        self.window = window
        self.cursor = cursor
        self.setOreColourBounds(ore)
        self.setNumberOfRocks(numberOfRocks)

    def botting_loop(self):
        while True:
            image = Camera.screenshot(self.window.bbox)
            rocks = ObjectDetector.inColourRange(image, self.lowerBound, self.upperBound, self.numberOfRocks, debug=True)
            
            print(f'I found {len(rocks)} rocks in {end - start} seconds')


    def setOreColourBounds(self, ore):
        with open('./config/miningConfig.json') as json_file:
            config = json.load(json_file)

            try: 
                lower = config[ore]['bgr']['lower']
                upper = config[ore]['bgr']['upper']
            except KeyError:
                raise KeyError('Invalid ore has been selected.')
        
        self.lowerBound = np.array(lower)
        self.upperBound = np.array(upper)

    def setNumberOfRocks(self, numberOfRocks):
        if numberOfRocks <= 0:
            numberOfRocks = 1

        self.numberOfRocks = numberOfRocks

