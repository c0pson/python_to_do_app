import customtkinter as ctk

# Imported properties
from properties import Colors
from file_operations import remove_event

class EventContent(ctk.CTkFrame):
    def __init__(self, master, events: dict, event: str, key: int, event_bar) -> None:
        super().__init__(master, fg_color=Colors.MAIN_COLOR)
        self.events: dict = events
        self.event: str = event
        self.key: int = key
        self.event_bar = event_bar
        self.buttons_frame = ctk.CTkFrame(self, fg_color=Colors.MAIN_COLOR)
        self.setup()

    def setup(self) -> None:
        self.content_title()
        self.content_date()
        self.content_time()
        self.content_notes()
        self.buttons_frame.place(x=120, rely=0.93, anchor='center')
        self.remove_event_button()
        self.save_event_button()

    def content_title(self) -> None:
    # title frame
        title_frame = ctk.CTkFrame(self, fg_color=Colors.MAIN_COLOR)
        title_frame.pack(side=ctk.TOP, padx=15, pady=15, anchor=ctk.W)
    # check box
        check_box = ctk.CTkCheckBox(title_frame, text='', width=0, height=0)
        check_box.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W, fill=ctk.BOTH)
    # title
        title = ctk.CTkEntry(title_frame, fg_color=Colors.MAIN_COLOR,
                            border_color=Colors.MAIN_COLOR,
                            font=ctk.CTkFont('Comic Sans', 32))
        title.insert('0', f'{self.event.split(',',1)[0]}')
        title.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W, fill=ctk.BOTH)

    def content_date(self) -> None:
        event_date = ctk.CTkEntry(self, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND,
                                font=ctk.CTkFont('Comic Sans', 32))
        event_date.insert('0', f'{self.event.split(',',2)[1]}')
        event_date.pack(side=ctk.TOP, padx=40, pady=5, anchor=ctk.W)

    def content_time(self) -> None:
    # time frame
        time_frame = ctk.CTkFrame(self, fg_color=Colors.MAIN_COLOR)
        time_frame.pack(side=ctk.TOP, padx=40, pady=5, anchor=ctk.W)
    # hour
        event_time_hour = ctk.CTkEntry(time_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=54,
                                font=ctk.CTkFont('Comic Sans', 32), justify='right')
        time_hour = (self.event.split(',',3)[2]).split(':')[0]
        event_time_hour.insert('0', time_hour)
        event_time_hour.pack(side=ctk.LEFT, padx=5, pady=5, anchor=ctk.W)
    # separator
        separator = ctk.CTkLabel(time_frame, text=':', font=ctk.CTkFont('Comic sans', 22))
        separator.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W)
    # minute 
        event_time_minutes = ctk.CTkEntry(time_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=54,
                                font=ctk.CTkFont('Comic Sans', 32), justify='right')
        time_minutes = (self.event.split(',',3)[2]).split(':')[1]
        event_time_minutes.insert('0', time_minutes)
        event_time_minutes.pack(side=ctk.LEFT, padx=5, pady=5, anchor=ctk.W)

    def content_notes(self) -> None:
    # TODO: create separate boxes for day, month and year
        event_notes = ctk.CTkTextbox(self, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.MAIN_COLOR,
                                font=ctk.CTkFont('Comic Sans', 32))
        event_notes.insert('0.0', f'{self.event.split(',',4)[3]}', None)
        event_notes.pack(side=ctk.TOP, padx=40, pady=5, anchor=ctk.W)

    def remove_event_button(self) -> None:
        remove_button = ctk.CTkButton(self.buttons_frame, text='REMOVE',
                                        command=self.remove_event,
                                        height=50, width=50, corner_radius=10,
                                        font=('Comic Sans', 21))
        remove_button.pack(side=ctk.LEFT, padx=3, pady=3, anchor=ctk.W)

    def save_event_button(self) -> None:
        remove_button = ctk.CTkButton(self.buttons_frame, text='SAVE',
                                        command=self.edit_event,
                                        height=50, width=50, corner_radius=10,
                                        font=('Comic Sans', 21))
        remove_button.pack(side=ctk.LEFT, padx=3, pady=3, anchor=ctk.W)

    def remove_event(self) -> None:
        self.event_bar.remove_from_dictionary(self.key)
        remove_event(self.events, self.key)
        self.destroy()

    def edit_event(self) -> None:
        pass
