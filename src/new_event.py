import customtkinter as ctk

# Imported properties
from properties import Colors

class AddNewEvent(ctk.CTkLabel):
    def __init__(self, master):
        super().__init__(master, 
                        text='+', font=('Comic Sans', 41),
                        fg_color=Colors.BACKGROUND, bg_color=Colors.MAIN_COLOR,
                        height=50, width=50, corner_radius=10)
        self.setup()

    def setup(self):
        pass
