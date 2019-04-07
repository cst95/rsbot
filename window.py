from pywinauto.findwindows import find_window
from pywinauto.win32functions import SetForegroundWindow
from bbox import Bbox
import win32gui
import pyautogui

#todo add sub classes for different clients?
# inherit from this class?

class Window():
    def __init__(self, username):
        self.name = f'RuneLite - {username}'
        self.hWnd = self.gethWnd()
        self.bbox = self.getBbox()

    def focus(self):
        win32gui.SetForegroundWindow(find_window(title=self.name))

    def gethWnd(self):
        return win32gui.FindWindow(None, self.name)

    def getBbox(self):
        window = win32gui.GetWindowRect(self.hWnd)
        print(window)
        return Bbox(window[0], window[1], window[2] - 50, window[3] - 50)

    def resize(self, x=0, y=0, w=100, h=100, absolute=False):
        if absolute:
            win32gui.MoveWindow(self.hWnd, x, y, w, h, True)
        else:
            win32gui.MoveWindow(self.hWnd, x, y, self.bbox.width + w, self.bbox.height + h, True)
