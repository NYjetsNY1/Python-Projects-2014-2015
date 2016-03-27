# Ben Sklar
# Tic-Tac-Toe game.
# Human (X) plays the Computer (O).
# Computer has some VERY basic artificial intelligence.

from tkinter import *

# Creates the application.
class Application(Frame):
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)     
        self.grid()
        self.X = "X"
        self.O = "O"
        self.EMPTY = ""
        self.still_playing = True
        self.TURN = "X"
        self.SQUARES = []
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
                            
        # create instruction label
        self.inst_lbl = Label(self, text = "Tic-Tac-Toe: press a button. You are X.")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 3, sticky = W)

        # create button 1 button
        self.button1 = Button(self, width = 1, background = "red", command = self.click1)
        self.button1.grid(row = 3, column = 0)
        self.SQUARES.append(self.button1)

        # create button 2 button
        self.button2 = Button(self, width = 1, background = "orange", command = self.click2)
        self.button2.grid(row = 3, column = 1)
        self.SQUARES.append(self.button2)

        # create button 3 button
        self.button3 = Button(self, width = 1, background = "yellow", command = self.click3)
        self.button3.grid(row = 3, column = 2)
        self.SQUARES.append(self.button3)

        # create button 4 button
        self.button4 = Button(self, width = 1, background = "green", command = self.click4)
        self.button4.grid(row = 4, column = 0)
        self.SQUARES.append(self.button4)

        # create button 5 button
        self.button5 = Button(self, width = 1, background = "blue", command = self.click5)
        self.button5.grid(row = 4, column = 1)
        self.SQUARES.append(self.button5)

        # create button 6 button
        self.button6 = Button(self, width = 1, background = "indigo", command = self.click6)
        self.button6.grid(row = 4, column = 2)
        self.SQUARES.append(self.button6)

        # create button 7 button
        self.button7 = Button(self, width = 1, background = "magenta", command = self.click7)
        self.button7.grid(row = 5, column = 0)
        self.SQUARES.append(self.button7)

        # create button 8 button
        self.button8 = Button(self, width = 1, background = "violet", command = self.click8)
        self.button8.grid(row = 5, column = 1)
        self.SQUARES.append(self.button8)

        # create button 9 button
        self.button9 = Button(self, width = 1, background = "brown", command = self.click9)
        self.button9.grid(row = 5, column = 2)
        self.SQUARES.append(self.button9)

        # create text widget to display message at the end
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 12, column = 0, columnspan = 3, sticky = W)


    # Each click is the same thing, each checks for the winner, then has the computer move, then checks for the winner again.
    def click1(self):
        self.button1["text"] = self.TURN
        self.button1["state"] = DISABLED
        self.check_for_winner()
        self.simple_computer_move()
        self.check_for_winner()

    def click2(self):
        self.button2["text"] = self.TURN
        self.button2["state"] = DISABLED
        self.check_for_winner()
        self.simple_computer_move()
        self.check_for_winner()

    def click3(self):
        self.button3["text"] = self.TURN
        self.button3["state"] = DISABLED
        self.check_for_winner()
        self.simple_computer_move()
        self.check_for_winner()

    def click4(self):
        self.button4["text"] = self.TURN
        self.button4["state"] = DISABLED
        self.check_for_winner()
        self.simple_computer_move()
        self.check_for_winner()

    def click5(self):
        self.button5["text"] = self.TURN
        self.button5["state"] = DISABLED
        self.check_for_winner()
        self.simple_computer_move()
        self.check_for_winner()

    def click6(self):
        self.button6["text"] = self.TURN
        self.button6["state"] = DISABLED
        self.check_for_winner()
        self.simple_computer_move()
        self.check_for_winner()

    def click7(self):
        self.button7["text"] = self.TURN
        self.button7["state"] = DISABLED
        self.check_for_winner()
        self.simple_computer_move()
        self.check_for_winner()

        
    def click8(self):
        self.button8["text"] = self.TURN
        self.button8["state"] = DISABLED
        self.check_for_winner()
        self.turn()
        self.simple_computer_move()
        self.turn()
        self.check_for_winner()

        
    def click9(self):
        self.button9["text"] = self.TURN
        self.button9["state"] = DISABLED
        self.check_for_winner()
        self.simple_computer_move()
        self.check_for_winner()


    
    def check_for_winner(self):
        # Check if still playing.
        if self.still_playing == True:
            # All the ways to win.
            WAYS_TO_WIN = ((self.button1, self.button2, self.button3),
                           (self.button4, self.button5, self.button6),
                           (self.button7, self.button8, self.button9),
                           (self.button1, self.button4, self.button7),
                           (self.button2, self.button5, self.button8),
                           (self.button3, self.button6, self.button9),
                           (self.button1, self.button5, self.button9),
                           (self.button3, self.button5, self.button7))
            
            # All of the buttons.
            buttons = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]


            # This part will tell you who the winner is if someone wins. 
            TIE = True
            for row in WAYS_TO_WIN:
                if row[0]["text"] == row[1]["text"] == row[2]["text"] != self.EMPTY:
                    for button in buttons:
                        button["state"] = DISABLED
                    self.still_playing = False
                    self.secret_txt.insert(0.0, row[0]["text"] + " has won!")
                    TIE = False

            # If no one wins, and all the buttons are disabled, the game is a tie.
            for button in buttons:
                if button["state"] != DISABLED:
                    TIE = False
            if TIE == True:
                self.still_playing = False
                self.secret_txt.insert(0.0, "The game is a tie!")         


    def simple_computer_move(self):
        # All the possible ways to win.
        WAYS_TO_WIN = ((self.button1, self.button2, self.button3),
                       (self.button4, self.button5, self.button6),
                       (self.button7, self.button8, self.button9),
                       (self.button1, self.button4, self.button7),
                       (self.button2, self.button5, self.button8),
                       (self.button3, self.button6, self.button9),
                       (self.button1, self.button5, self.button9),
                       (self.button3, self.button5, self.button7))
        
        # All of the buttons.
        buttons = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]

        # When the computer has an ample opportunity to win, it will take that move.
        for row in WAYS_TO_WIN:
            textrow = [row[0]["text"], row[1]["text"], row[2]["text"]]
            count = 0
            for item in textrow:
                if item == self.O:
                    count += 1
            if self.EMPTY in textrow and count == 2:
                if textrow[0] == self.EMPTY:
                    row[0]["state"] = DISABLED
                    row[0]["text"] = self.O
                    return
                    
                elif textrow[1] == self.EMPTY:
                    row[1]["state"] = DISABLED
                    row[1]["text"] = self.O
                    return
                    
                else:
                    row[2]["state"] = DISABLED
                    row[2]["text"] = self.O
                    return

        # When human is about to win, the computer will block the human move.
        for row in WAYS_TO_WIN:
            textrow = [row[0]["text"], row[1]["text"], row[2]["text"]]
            count1 = 0
            for item in textrow:
                if item == self.X:
                    count1 += 1
            if self.EMPTY in textrow and count1 == 2:
                if textrow[0] == self.EMPTY:
                    row[0]["state"] = DISABLED
                    row[0]["text"] = self.O
                    return
                    
                elif textrow[1] == self.EMPTY:
                    row[1]["state"] = DISABLED
                    row[1]["text"] = self.O
                    return
                    
                else:
                    row[2]["state"] = DISABLED
                    row[2]["text"] = self.O
                    return
                    
        # When no one is about to win, move in order from beginning button to end.
        for button in buttons:
          if button["state"] != DISABLED:
              button["state"] = DISABLED
              button["text"] = self.O
              return


# Main function.
def main():
    root = Tk()
    root.title("Tic-Tac-Toe")
    root.geometry("250x150")

    app = Application(root)

    root.mainloop()

main()
input("\n\nPress the enter key to exit.")
