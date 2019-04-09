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

    # def botting_loop(self):
    #     isMining = True
    #     lastClick = self.controller.lastClick

    #     while True:
    #         if isMining:
    #             #Take a screenshot of the runelite window
    #             image = Camera.screenshot(self.window.bbox.bbox)

    #             #Detect the nearest n rocks
    #             rocks = ObjectDetector.inColourRange(image, self.lowerBound, self.upperBound, self.numberOfRocks, self.debug)

    #             print(f'I found {len(rocks)} rocks')

    #             if len(rocks) > 0:
    #                 for rock in rocks:
    #                     if rock.areCoordsInside(*lastClick):
    #                         isMining = False
    #                         break

    #                 if not isMining:
    #                     self.controller.clickInBbox(rocks[0])


    def botting_loop(self):
        isMining = False

        while True:

            image = Camera.screenshot(self.window.bbox.bbox)
            #Detect the nearest n rocks
            rocks = ObjectDetector.inColourRange(image, self.lowerBound, self.upperBound, self.numberOfRocks, self.debug)
            print(f'I found {len(rocks)} rocks')

            if not isMining:
                if len(rocks) > 0:
                    self.controller.clickInBbox(rocks[0])
                    isMining = True
                    print('Starting Mining')

            while isMining:
                isLastClickInAvailableRocks = False

                image = Camera.screenshot(self.window.bbox.bbox)
                rocks = ObjectDetector.inColourRange(image, self.lowerBound, self.upperBound, self.numberOfRocks, self.debug)
                print(f'I found {len(rocks)} rocks')

                if len(rocks) > 0:
                    for rock in rocks:
                        if rock.areCoordsInside(*self.controller.lastClick):
                            isLastClickInAvailableRocks = True
                            break

                    if not isLastClickInAvailableRocks:
                        isMining = False
                        print('Finishing Mining')




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

