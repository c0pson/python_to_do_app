import customtkinter as ctk

# Imported properties
from properties import Colors

class TopFrame(ctk.CTkFrame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, fg_color=Colors.ACCENT_COLOR_2,
                        corner_radius=0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER,
                    relwidth=1.01, relheight=1.01)
        self.setup()

    def setup(self):
        pass

class AddNewEvent(ctk.CTkLabel):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, 
                        text='+', font=('Comic Sans', 41),
                        fg_color=Colors.BACKGROUND, bg_color=Colors.MAIN_COLOR,
                        height=50, width=50, corner_radius=10)
        self.bind('<Button-1>', lambda event: self.ask_for_new_event(event))
        self.setup()

    def setup(self):
        pass

    def ask_for_new_event(self, event):
        TopFrame(self.master)
