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
        title_of_the_bar = ctk.CTkLabel(self, text='Events: ', text_color=Colors.TEXT_COLOR,
                                        font=ctk.CTkFont('Comic Sans', int(Window.SIZE_x32)))
        title_of_the_bar.pack(side=ctk.TOP, padx=int(Window.PAD_X), pady=int(Window.PAD_Y),
                                anchor=ctk.W)

    def events_container(self) -> None:
        self.events: dict = self.load_events()
        self.container = ctk.CTkScrollableFrame(self, fg_color=Colors.SECOND_COLOR,
                                                scrollbar_button_color=Colors.SECOND_COLOR,
                                                scrollbar_button_hover_color=Colors.SECOND_COLOR)
        self.container.pack(side=ctk.BOTTOM, padx=0, pady=0,
                        fill=ctk.Y, expand= True)
        for key, event in self.events.items():
            self.load_button(key, event)

    def load_events(self) -> dict:
        # TODO: file handle
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
                                    text_color=Colors.TEXT_COLOR,
                                    corner_radius=0, width=160, height=40,
                                    font=ctk.CTkFont('Comic Sans', 20),
                                    command=lambda: self.load_event_content(key))
        new_button.pack(side='top', padx=5, pady=5, fill=ctk.X)
        self.button_dict[key] = new_button

    def load_event_content(self, key: int) -> None:
        if not self.current_content:
            event_content = EventContent(self.master, self.events, self.events[key], key, self)
            event_content.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)
            self.current_content = event_content
        else:
            if self.current_content.key == key:
                return
            self.current_content.destroy()
            self.current_content = None
            self.load_event_content(key)

    def remove_from_dictionary(self, key: int) -> None:
        self.button_dict[key].destroy()
        del self.button_dict[key]
        del self.events[key]

    def edit_in_dictionary(self, key: int, new_data: str) -> None:
        title = f'{new_data.split(',',1)[0]}'
        self.button_dict[key].configure(text=title)
        self.current_content.destroy()
        self.current_content = None
        self.events[key] = new_data
        self.load_event_content(key)
