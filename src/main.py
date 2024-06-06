import customtkinter as ctk

# Imported properties
from properties import Colors
from properties import Window

# Imported elements of window
from new_event import AddNewEvent
from bar import EventsBar

class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__(fg_color=Colors.BACKGROUND)
        self.title('Event planner')
        self.geometry(f'{int(Window.WIDTH)}x{int(Window.HEIGHT)}') # int() necessary idk why
        self.setup()

    def setup(self) -> None:
        new_frame = ctk.CTkFrame(self, corner_radius=0,
                                fg_color=Colors.MAIN_COLOR)
        new_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)
        side_panel = EventsBar(new_frame)
        side_panel.pack(side=ctk.LEFT, fill=ctk.Y)
        add_widget = AddNewEvent(self)
        add_widget.place(relx=0.95, rely=0.93, anchor='center')

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
