#-------------------------------------------------------------------------------
# Name:        Character Creation Demo
# Purpose:     Demo module for creating characters.
#
# Author:      Eugene Petrie
#
# Created:     14/11/2013
# Copyright:   (c) Eugene Petrie 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from Tkinter import *
from Player import *
from random import *

class CharacterApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Here I set the header font, which is the title of the application.
        self.headerFont = ("OCR A Extended", "16", "bold")
        self.title("Character Creator Demo")

        # Here I add three functions that will run to help create the character.
        # The getplayerStats function is supposed to go into the Player module
        # and get the player stats creted their, but it does not work.
        # The setGUI function sets up all the labels, text boxes, spin boxes,
        # and buttons used in the application.
        # The createPlayer function takes the information from Player.py and
        # what is entered in this application, puts it together, then prints out
        # the character sheet.

        # Function to be added: Save Character.
        self.getplayerStats()
        self.setGUI()
        self.createPlayer()



    def getplayerStats(self):
        pass

    def setGUI(self):
        # Create a label called Character Bio and center it.
        Label(self, text = "Character Bio",
        font = self.headerFont).grid(columnspan = 2)

        # Create a label that prompts the player to make a name.
        Label(self, text ="Name:").grid(row = 2, column = 0)
        # Set up a text field to allow user to enter a name.
        self.txtName = Entry(self)
        self.txtName.grid(row = 2, column = 1)
        # Insert a default name "Player 1".
        self.txtName.insert(0, "Player 1")

        # Create a label that propmts the user to pick an initial level.
        Label(self, text ="Initial Level:").grid(row = 3, column = 0)
        # Set up a Spinbox that allows players to pick a level 1-5.
        self.levelSpin = Spinbox(self, value = range (1, 6))
        self.levelSpin.grid(row = 3, column = 1)

        # Create a label that prompts the user to pick an initial race.
        Label(self, text = "Race:").grid(row = 4, column = 0)
        # Set up a Spinbox that allows players to pick an initail race.
        self.raceSpin = Spinbox(self, values = ("Human", "Elf", "Dwarf", "Halfling"))
        self.raceSpin.grid(row = 4, column = 1)

        # Create a label called Stat Distrubution.
        Label(self, text = "Stat Distrubution",
        font = self.headerFont).grid(columnspan = 2)

        # Create a spinbox that has an additional command that manipulates
        # a point system variable depending which button is pressed (Up/Down).
        # Create a variable called statpoints, set eaqual to a random number
        # between 1 and 20, divide that number by amount of stats,
        # then add the initial level to it.

    def createPlayer(self):
        pass

# Runs application when module is ran.
def main():
    app = CharacterApp()
    app.mainloop()

# For importing purposes, tells program that is this is imported, run the main
# function on the file that this file was imported to. Otherwise, run the main
# function on this file.
if __name__ == '__main__':
    main()