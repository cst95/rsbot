import pyautogui as pag
from random import randint

class Controller():
    def __init__(self):
        self.x , self.y = pag.position()

    @property 
    def lastClick():
        return self.x, self.y

    @lastClick.setter
    def lastClick(self, value):
        return None

    def moveCursorTo(self, x, y, time=0):
        pyautogui.moveTo(x,y,time)

    #Click in a random position inside the bbox
    def clickInBbox(self, bbox):
        pass

        self.moveCursorTo()


