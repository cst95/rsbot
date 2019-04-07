from PIL import ImageGrab
import numpy as np

class Camera():
	@staticmethod
	def screenshot(bbox):
		print(bbox)
		print(type(bbox))
		return np.array(ImageGrab.grab(bbox))