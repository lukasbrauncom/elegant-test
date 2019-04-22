import pickle

class Player:
	def __init__(self, name="Player 1", color=None):
		self.name = name
		self.color = color                

	def set_name(self,name):
		self.name = name

	def get_name(self):
		return self.name

	def set_color(self, x, y):
                is_red_clicked = (
                    x >= 50 and
                    x <= 100 and
                    y >= 50 and
                    y <= 100
                )

                is_green_clicked = (
                    x >= 150 and
                    x <= 200 and
                    y >= 50 and
                    y <= 100
                )

                is_blue_clicked = (
                    x >= 250 and
                    x <= 300 and
                    y >= 50 and
                    y <= 100
                )

                if any([is_red_clicked, is_blue_clicked, is_green_clicked]):
                    if is_red_clicked:
                        self.color = 'red'
                    elif is_blue_clicked:
                        self.color = 'blue'
                    elif is_green_clicked:
                        self.color = 'green'


	def get_color(self):
		return self.color

	def store_data(self):
		pickle.dump(self, open( "save.p", "wb" ) )

	def read_data(self):
		loaded = pickle.load(open( "save.p", "rb" ) )
		self.__dict__ = loaded.__dict__

