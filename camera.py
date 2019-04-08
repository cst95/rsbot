from PIL import ImageGrab
import numpy as np

class Camera():
	@staticmethod
	def screenshot(bbox):
		return np.array(ImageGrab.grab(bbox))