from Tkinter import *
from Player import *

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		
		self.getplayerStats()
		self.setGUI()
		self.createCharacter()
		
	def getplayerStats():
		return playerStats
	
	def setGUI():
		pass
		
	def createCharacter():
		pass
		
def main()
	print self.playerStats
	