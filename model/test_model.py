import pytest
from .model import Player

name = "franz"
color = "red"

def test_model_creation():
	player = Player(name,color)
	assert player.name == name and player.color == color
	
def test_name_setter():
	player = Player(name,color)
	newName = "herbert"
	player.setName(newName)
	assert player.name == newName

def test_name_getter():
	player = Player(name,color)
	assert player.getName() == name

def test_color_setter():
	player = Player(name,color)
	newColor = "herbert"
	player.setColor(newColor)
	assert player.color == newColor

def test_color_getter():
	player = Player(name,color)
	assert player.getColor() == color


def test_data_storage():
	player = Player(name,color)
	player.storeData()
	player2 = Player(name,color)
	player2.readData()
	assert  player.__dict__ == player2.__dict__
