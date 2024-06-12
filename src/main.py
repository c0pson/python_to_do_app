import customtkinter as ctk

# Imported properties
from properties import Colors
from properties import Window, Window_

# Imported elements of window
from new_event import AddNewEvent
from bar import EventsBar

class MainWindow(ctk.CTk):
    """Class handling main window and initializing all widgets in app.
    To do app can store all your events, date and time of them alongside 
    the short notes."""
    def __init__(self) -> None:
        """Initialization of window.
        """
        super().__init__(fg_color=Colors.BACKGROUND)
        self.title('Event planner')
        self.geometry(f'{int(Window.WIDTH)}x{int(Window.HEIGHT)}')
        self.minsize(Window.WIDTH, Window.HEIGHT)
        self.setup()

    def setup(self) -> None:
        """Initialization of widgets:
            - main frame
            - side panel 
            - new event button
        """
        new_frame = ctk.CTkFrame(self, corner_radius=0,
                                fg_color=Colors.MAIN_COLOR)
        new_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)
        side_panel = EventsBar(new_frame)
        side_panel.pack(side=ctk.LEFT, fill=ctk.Y)
        add_widget = AddNewEvent(self)
        add_widget.place(relx=float(Window_.REL_PAD_X), rely=float(Window_.REL_PAD_Y), anchor='center') 

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
