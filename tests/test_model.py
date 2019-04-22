import pytest
from elegant.model import Player

name = "franz"
color = "red"

def test_model_creation():
	player = Player(name,color)
	assert player.name == name and player.color == color
	
def test_name_setter():
	player = Player(name,color)
	newName = "herbert"
	player.set_name(newName)
	assert player.name == newName

def test_name_getter():
	player = Player(name,color)
	assert player.get_name() == name

def test_color_setter():
	player = Player(name,color)
	newColor = "red"
	player.set_color(52, 52)
	assert player.color == newColor

def test_color_getter():
	player = Player(name,color)
	assert player.get_color() == color


def test_data_storage():
	player = Player(name,color)
	player.store_data()
	player2 = Player(name,color)
	player2.read_data()
	assert  player.__dict__ == player2.__dict__
