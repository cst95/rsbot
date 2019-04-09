import json
import time
from object_detector import ObjectDetector
from camera import Camera
import numpy as np

class OreMinerScript():
    def __init__(self, ore, window, controller, numberOfRocks, debug=False):
        self.window = window
        self.controller = controller
        self.setOreColourBounds(ore)
        self.setNumberOfRocks(numberOfRocks)
        self.debug = debug

    def botting_loop(self):

        while True:
            image = Camera.screenshot(self.window.bbox.bbox)
            rocks = ObjectDetector.inColourRange(image, self.lowerBound, self.upperBound, self.numberOfRocks, self.debug)
            print(f'I found {len(rocks)} rocks')

            if len(rocks) > 0:
                lastClick = self.controller.clickInBbox(rocks[0])
                time.sleep(4)
                print('Mining')

                while not self.hasFinishedMining(lastClick):
                    time.sleep(0.6)
                #Just need a way here to determine if rock is finished mining
                print('Finished mining')

    def hasFinishedMining(self, lastClick):
        x,y = lastClick
        image = Camera.screenshot(self.window.bbox.bbox)
        rocks = ObjectDetector.inColourRange(image, self.lowerBound, self.upperBound, self.numberOfRocks, self.debug)

        finishedMining = False

        for rock in rocks:
            if rock.areCoordsInside(x,y):
                return finishedMining

        return not finishedMining





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

