import pyautogui

class Cursor():

	def moveTo(self, x, y, time=0):
		pyautogui.moveTo(x,y,time)

	def __init__(self):
		pass
