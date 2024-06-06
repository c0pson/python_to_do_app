import customtkinter as ctk

from properties import Colors

class EventContent(ctk.CTkFrame):
    def __init__(self, master, event: str):
        super().__init__(master, fg_color=Colors.MAIN_COLOR)
        self.event: str = event
        self.setup()

    def setup(self):
        self.content_title()
        self.content_time()
        self.content_notes()

    def content_title(self):
        title = ctk.CTkLabel(self, text=f'{self.event.split(',',1)[0]}')
        title.pack(side=ctk.TOP, padx=15, pady=15)

    def content_time(self):
        pass

    def content_notes(self):
        pass
