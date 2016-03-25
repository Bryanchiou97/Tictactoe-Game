# -----------------------------------------------------------------------------
# Name:       ticTacToe
# Purpose:    Implement a game of Tic Tac Toe
#
# Author: Bryan Chiou
# Date: 3/19/2015
# -----------------------------------------------------------------------------
'''
Play a game of tic tac toe with the computer
'''
import tkinter
import random


class Game(object):
    '''
    Represents the game tic tac toe. the user plays against the computer

    Argument:
    none

    Attributes: counter: to count the amount of squares

    '''

    # Add your class variables if needed here


    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent
        # Add your instance variables if needed here
        self.counter = 0

        # Create the restart button widget
        start_button = tkinter.Button(self.parent, text='RESTART',
                                        width=20,
                                        command=self.restart)
        start_button.pack()
        # Create a canvas widget
        self.canvas = tkinter.Canvas(self.parent, width=300, height=300)
        self.canvas.pack()

        # Create a label widget for the win/lose message
        self.display = tkinter.Label(self.parent, text = '')
        self.display.pack()

        self.initialize_game()

    def initialize_game(self):
        """
        Starts the tic tac toe game by drawing the squares

        Parameters:  none
        Returns:  none
        """
        # These are the initializations that need to happen
        # at the beginning and after restarts
        self.board = [[0,0,0],[0,0,0],[0,0,0]]   #tic tac toe board. helps to select which part of tic tac toe
        for row in range(3):                      #drawing tic tac toe
            for column in range(3):

                self.canvas.create_rectangle(100 * column, 100 * row, 100 * (column + 1), 100 * (row + 1), fill='white')
        self.canvas.bind("<Button-1>", self.play)     #Let user play


    def restart(self):
        """
        Restarts a finished or unfinished game of tic tac toe

        Parameters:  none
        Returns:  none
        """
        # This method is invoked when the user clicks on the RESTART button.
        # Erase the canvas
        # invoke initialize_game
        self.canvas.delete("all")
        self.counter = 0
        self.display.configure(text = '')
        self.initialize_game()


    def play(self, event):
        """
        This will play tic tac toe with user and allow user to play

        Parameters:  event
        Returns:  none
        """
        # This method is invoked when the user clicks on a square.
        # If the square is already taken, do nothing.
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        position_x = int(x//100)   #filling the user's spot
        position_y = int(y//100)

        if self.board[position_x][position_y] == 0 and self.counter != 9:
            self.board[position_x][position_y] = 1
            self.canvas.create_rectangle(position_x*100, position_y*100,
                                         position_x*100 + 100, position_y*100 + 100, fill = 'blue')
            self.counter += 1

            if self.counter == 9:
                self.check_game_at_full()   # check if won/lost
            else:
                self.check_game()  #check if won/lost



            player_2_x = random.randint(0,2)
            player_2_y = random.randint(0,2)

            while self.board[player_2_x][player_2_y] != 0 and self.counter != 9:
                player_2_x = random.randint(0,2)
                player_2_y = random.randint(0,2)

            # opponents turn

            if self.board[player_2_x][player_2_y] == 0:
                self.canvas.create_rectangle(player_2_x*100, player_2_y*100,
                                             player_2_x*100 + 100, player_2_y*100 + 100, fill = 'red') #computers turn
                self.board[player_2_x][player_2_y] = 2
                self.counter += 1 # counting the squares
                self.check_game() #check if won also


        else:
            return None


    def check_game(self):
        """
        This will check game for winner / loser

        Parameters:  none
        Returns:  none
        """
        # Check if the game is won or lost
        # Return True or False
        if self.board[0][0] == 1 and self.board[0][1] == 1 and self.board[0][2] == 1: #checking each combination
            self.display.configure(text = 'You win!')                                 #display message
            self.counter = 9                                                          #prevent user from clicking after
        if self.board[1][0] == 1 and self.board[1][1] == 1 and self.board[1][2] == 1:
            self.display.configure(text = 'You win!')
            self.counter = 9
        if self.board[2][0] == 1 and self.board[2][1] == 1 and self.board[2][2] == 1:
            self.display.configure(text = 'You win!')
            self.counter = 9
        if self.board[0][0] == 1 and self.board[1][0] == 1 and self.board[2][0] == 1:
            self.display.configure(text = 'You win!')
            self.counter = 9
        if self.board[0][1] == 1 and self.board[1][1] == 1 and self.board[2][1] == 1:
            self.display.configure(text = 'You win!')
            self.counter = 9
        if self.board[0][2] == 1 and self.board[1][2] == 1 and self.board[2][2] == 1:
            self.display.configure(text = 'You win!')
            self.counter = 9
        if self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1:
            self.display.configure(text = 'You win!')
            self.counter = 9
        if self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1:
            self.display.configure(text = 'You win!')
            self.counter = 9
        if self.board[0][0] == 2 and self.board[0][1] == 2 and self.board[0][2] == 2:
            self.display.configure(text = 'You Lose')
            self.counter = 9
        if self.board[1][0] == 2 and self.board[1][1] == 2 and self.board[1][2] == 2:
            self.display.configure(text = 'You Lose')
            self.counter = 9
        if self.board[2][0] == 2 and self.board[2][1] == 2 and self.board[2][2] == 2:
            self.display.configure(text = 'You Lose')
            self.counter = 9
        if self.board[0][0] == 2 and self.board[1][0] == 2 and self.board[2][0] == 2:
            self.display.configure(text = 'You Lose')
            self.counter = 9
        if self.board[0][1] == 2 and self.board[1][1] == 2 and self.board[2][1] == 2:
            self.display.configure(text = 'You Lose')
            self.counter = 9
        if self.board[0][2] == 2 and self.board[1][2] == 2 and self.board[2][2] == 2:
            self.display.configure(text = 'You Lose')
            self.counter = 9
        if self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2:
            self.display.configure(text = 'You Lose')
            self.counter = 9
        if self.board[0][2] == 2 and self.board[1][1] == 2 and self.board[2][0] == 2:
            self.display.configure(text = 'You Lose')
            self.counter = 9

    def check_game_at_full(self):
        """
        check game if user won or lost

        Parameters:  none
        Returns:  none
        """
        if self.board[0][0] == 1 and self.board[0][1] == 1 and self.board[0][2] == 1: #checking if user won
            self.display.configure(text = 'You win!')                                 #if not, it's a tie
        if self.board[1][0] == 1 and self.board[1][1] == 1 and self.board[1][2] == 1:
            self.display.configure(text = 'You win!')
        if self.board[2][0] == 1 and self.board[2][1] == 1 and self.board[2][2] == 1:
            self.display.configure(text = 'You win!')
        if self.board[0][0] == 1 and self.board[1][0] == 1 and self.board[2][0] == 1:
            self.display.configure(text = 'You win!')
        if self.board[0][1] == 1 and self.board[1][1] == 1 and self.board[2][1] == 1:
            self.display.configure(text = 'You win!')
        if self.board[0][2] == 1 and self.board[1][2] == 1 and self.board[2][2] == 1:
            self.display.configure(text = 'You win!')
        if self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1:
            self.display.configure(text = 'You win!')
        if self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1:
            self.display.configure(text = 'You win!')
        else:
            self.display.configure(text = "It's a tie!")
    # Add your method definitions here


def main():
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    play = Game(root)
    # Enter the main event loop
    root.mainloop()

if __name__ == '__main__':
    main()