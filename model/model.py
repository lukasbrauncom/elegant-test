import pickle

class Player:

	def __init__(self,name="player 1",color="red"):
		self.name = name
		self.color = color

	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name

	def setColor(self,color):
		self.color = color

	def getColor(self):
		return self.color
		
	def storeData(self):
		pickle.dump(self, open( "save.p", "wb" ) )

	def readData(self):
		loaded = pickle.load(open( "save.p", "rb" ) )
		self.__dict__ = loaded.__dict__

m = Player()