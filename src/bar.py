import customtkinter as ctk
import os

# Imported properties
from properties import Colors
from properties import Window
from properties import Paths

from event_content import EventContent

class EventsBar(ctk.CTkFrame):
    def __init__(self, master) -> None:
        self.master = master
        super().__init__(self.master, fg_color=Colors.SECOND_COLOR)
        self.button_dict: dict = {}
        self.setup()
        self.current_content = None

    def setup(self) -> None:
        self.title()
        self.configure(corner_radius=0)
        self.events_container()

    def title(self) -> None:
        title_of_the_bar = ctk.CTkLabel(self, text='Events: ', 
                                        font=ctk.CTkFont('Comic Sans', int(Window.SIZE_x32)))
        title_of_the_bar.pack(side=ctk.TOP, padx=int(Window.PAD_X), pady=int(Window.PAD_Y),
                                anchor=ctk.W)

    def events_container(self) -> None:
        self.events: dict = self.load_events()
        self.container = ctk.CTkScrollableFrame(self, fg_color=Colors.SECOND_COLOR,
                                            )
        self.container.pack(side=ctk.BOTTOM, padx=Window.PAD_X, pady=Window.PAD_Y,
                        fill=ctk.Y, expand= True)
        for key, event in self.events.items():
            self.load_button(key, event)

    def load_events(self) -> dict:
        file_name: str = f'{os.path.join(os.path.dirname(__file__), '..') + Paths.EVENTS}'
        events: dict = {}
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file):
                line: str = line.strip()
                events[line_number] = line
        return events

    def load_button(self, key: int, name: str) -> None:
        name: list = name.split(',', 1)
        new_button = ctk.CTkButton(master=self.container, text=name[0],
                                    width=160, height=40, font=ctk.CTkFont('Comic Sans', 20),
                                    command=lambda: self.load_event_content(key))
        new_button.pack(side='top', padx=5, pady=5, fill=ctk.X)
        self.button_dict[key] = new_button

    def load_event_content(self, key: int) -> None:
        if not self.current_content:
            event_content = EventContent(self.master, self.events[key])
            event_content.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)
            self.current_content = event_content
        else:
            self.current_content.destroy()
            self.current_content = None
            self.load_event_content(key)