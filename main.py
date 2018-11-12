

# Basic Game Architecture
# 1 - Start Game (Initialize Values)
# 2 - Render Game Visuals
# 3 - Receive/Process Input
# 4 - Update Game Logic
# 5 - JUMP TO STEP 2

import tkinter as tk
import random

class Main_GUI(tk.Frame):
    def __init__(self, master):


        # Housekeeping for Frame and Tk() objects
        self.master = master
        self.master.title("ShibeJump - John Marrs/Enrique Berrios")
        self.master.geometry("500x500")
        self.master.focus_set()
        self.master.update()
        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()

        # Specify padding for edges
        self.padding = 50

        self.create_components()


    def create_components(self):
        #Initialize the canvas, bind keys to function handler, bind configure to on_resize method

        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height)
        self.canvas.pack(fill="both", expand=True)
        self.master.bind("<Key>", self.handle_keystroke)
        self.master.bind("<Configure>", self.on_resize)
        self.setup()
        


    def start_game(self):
        #Clear screan
        self.canvas.delete("all")

        #Launch the game
        self.setup()
        self.game_running = True

        self.update()

    def game_over(self):
        # End the game
        self.game_running = False
        self.game_ended = True


    def setup(self):
        pass
        

    def update(self):
        if (self.game_running):
            
            self.master.after(100, self.update)
        elif self.game_ended:
            #Display game over if the game has ended
            self.canvas.create_text(self.width/2 , self.height/2,fill=self.game_over_color,font="system 36", text="GAME OVER")



    #handle user inputs
    def handle_keystroke(self, event):
        i = event.char


                
    #handle resize
    def on_resize(self, event):
        self.width = event.width
        self.height = event.height
        self.master.update()
        self.setup()

                
# Actually launch the application
application = tk.Tk()
application.update()
m_gui = Main_GUI(application)
application.mainloop()


