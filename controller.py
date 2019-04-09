import pyautogui as pag
from random import randint
import scipy
import time
from scipy import interpolate

# Any duration less than this is rounded to 0.0 to instantly move the mouse.
pag.MINIMUM_DURATION = 0  # Default: 0.1
# Minimal number of seconds to sleep between mouse moves.
pag.MINIMUM_SLEEP = 0  # Default: 0.05
# The number of seconds to pause after EVERY public function call.
pag.PAUSE = 0  # Default: 0.1

class Controller():
    def __init__(self):
        self.x , self.y = pag.position()
        self.lastClick = (0,0)

    def moveCursorTo(self, x, y):
        # cp = randint(3, 5)  # Number of control points. Must be at least 2.
        # x1, y1 = pag.position()  # Starting position
        # x2, y2 = x, y  # Destination

        # # Distribute control points between start and destination evenly.
        # x = scipy.linspace(x1, x2, num=cp, dtype='int')
        # y = scipy.linspace(y1, y2, num=cp, dtype='int')

        # # Randomise inner points a bit (+-RND at most).
        # RND = 10
        # xr = scipy.random.randint(-RND, RND, size=cp)
        # yr = scipy.random.randint(-RND, RND, size=cp)
        # xr[0] = yr[0] = xr[-1] = yr[-1] = 0
        # x += xr
        # y += yr

        # # Approximate using Bezier spline.
        # degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
        #                                   # Must be less than number of control points.
        # tck, u = scipy.interpolate.splprep([x, y], k=degree)
        # u = scipy.linspace(0, 1, num=max((100,700)))
        # points = scipy.interpolate.splev(u, tck)

        # # Move mouse.
        # duration = 0.1
        # timeout = duration / len(points[0])
        # for point in zip(*(i.astype(int) for i in points)):
        #     pag.moveTo(*point)
        #     time.sleep(timeout)
        pag.moveTo(x,y)

    #Click in a random position inside the bbox
    def clickInBbox(self, bbox):
        x,y = bbox.midpoint()
        
        self.moveCursorTo(x, y)
        time.sleep(0.4)

        pag.click()
        self.lastClick = (x,y)
