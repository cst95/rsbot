from random import randint

class Bbox():
	def __init__(self, x_min, y_min, x_max, y_max, ):
		self.x_min = x_min
		self.x_max = x_max
		self.y_min = y_min
		self.y_max = y_max

	@property
	def width(self):
		return self.x_max - self.x_min
	
	@property
	def height(self):
		return self.y_max - self.y_min

	@property
	def bbox(self):
		return self.x_min, self.y_min, self.x_max, self.y_max

	def midpoint(self):
		midpoint = self.calculateMidPoint()
		return midpoint
	
	def areCoordsInside(self, x, y):
		print(self.x_min,self.x_max,self.y_min,self.y_max)
		print(x,y)
		isInXRange = self.x_min < x < self.x_max
		isInYRange = self.y_min < y < self.y_max
		return isInXRange and isInYRange

	def randomCoordsInBbox(self):
		randomX = randint(self.x_min, self.x_max)
		randomY = randint(self.y_min, self.y_max)
		return randomX, randomY

	def calculateMidPoint(self):
		xmid = self.x_min + (self.width / 2)
		ymid = self.y_min + (self.height / 2)
		return xmid, ymid