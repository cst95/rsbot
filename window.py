from pywinauto.findwindows import find_window
from pywinauto.win32functions import SetForegroundWindow
import win32gui
import pyautogui

#todo add sub classes for different clients?
# inherit from this class?

class Window():
    def focus(self):
        win32gui.SetForegroundWindow(find_window(title=self.name))

    def get_hWnd(self):
        return win32gui.FindWindow(None, self.name)

    def get_geometry(self):
        window = win32gui.GetWindowRect(self.hWnd)

        x = window[0]
        y = window[1]
        w = window[2] - x
        h = window[3] - y

        #bottom left, bottom right etc.
        self.top_left = (x, y)
        self.top_right = (x + w, y)
        self.bottom_left = (x, y + h)
        self.bottom_right = (x + w, y + h)
        self.width = w
        self.height = h
        self.mid_point = (x + w / 2, y + h / 2)
        self.bbox = window


    def resize(self, x=0, y=0, w=100, h=100, absolute=False):
        if absolute:
            win32gui.MoveWindow(self.hWnd, x, y, w, h, True)
        else:
            win32gui.MoveWindow(self.hWnd, x, y, self.width + w, self.height + h, True)



    def __init__(self, username):
        self.name = f'RuneLite - {username}'
        self.hWnd = self.get_hWnd()
        self.get_geometry()

