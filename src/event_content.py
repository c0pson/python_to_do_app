import customtkinter as ctk

# Imported properties
from properties import Colors
from properties import Window, Window_
from file_operations import remove_event
from file_operations import edit_event

class EventContent(ctk.CTkFrame):
    def __init__(self, master, events: dict, event: str, key: int, event_bar) -> None:
        super().__init__(master, fg_color=Colors.MAIN_COLOR)
        self.events: dict = events
        self.event: str = event
        self.key: int = key
        self.event_bar = event_bar
        self.buttons_frame = ctk.CTkFrame(self, fg_color=Colors.MAIN_COLOR)
        self.original_info: str = ''
        self.setup()

    def setup(self) -> None:
        self.content_title()
        self.content_date()
        self.content_time()
        self.content_notes()
        self.get_original_info()
        self.buttons_frame.place(x=120, rely=Window_.REL_PAD_Y, anchor='center')
        self.remove_event_button()
        self.save_edited_event_button()

    def get_original_info(self) -> None:
        # title
        title = self.title.get()
    # date
        date_day = self.event_date_day.get()
        date_month = self.event_date_month.get()
        date_year = self.event_date_year.get()
    # time
        time_hour = self.event_time_hour.get()
        time_minutes = self.event_time_minutes.get()
    # notes
        notes = self.event_notes.get('0.0', 'end')
    # all together
        self.original_info: str = f'{title},{date_day}.{date_month}.{date_year},{time_hour}:{time_minutes},{notes[:-1]}'

    def content_title(self) -> None:
    # title frame
        title_frame = ctk.CTkFrame(self, fg_color=Colors.MAIN_COLOR)
        title_frame.pack(side=ctk.TOP, padx=15, pady=15, fill=ctk.X)
    # check box
        check_box = ctk.CTkCheckBox(title_frame, text='', width=0, height=0)
        check_box.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W, fill=ctk.X)
    # title
        self.title = ctk.CTkEntry(title_frame, fg_color=Colors.MAIN_COLOR,
                            border_color=Colors.MAIN_COLOR, corner_radius=0,
                            font=ctk.CTkFont('Comic Sans', 32),
                            text_color=Colors.TEXT_COLOR, width=9000)
        title = f'{self.event.split(',',1)[0]}'
        self.title.insert('0', title)
        self.title.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W, fill=ctk.X)

    def content_date(self) -> None:
    # date frame
        date_frame = ctk.CTkFrame(self, fg_color=Colors.MAIN_COLOR)
        date_frame.pack(side=ctk.TOP, padx=40, pady=5, anchor=ctk.W)
    # date label
        label_title = ctk.CTkLabel(date_frame, fg_color=Colors.MAIN_COLOR,
                                    text_color=Colors.TEXT_COLOR, text='Date: ',
                                    width=50, corner_radius=0,
                                    font=ctk.CTkFont('Comic Sans', 32))
        label_title.pack(side=ctk.LEFT, padx=2, pady=2)
    # day
        self.event_date_day = ctk.CTkEntry(date_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=50, corner_radius=0,
                                font=ctk.CTkFont('Comic Sans', 32), justify=ctk.RIGHT,
                                text_color=Colors.TEXT_COLOR)
        date_day = f'{self.event.split(',',2)[1].split('.',1)[0]}'
        self.event_date_day.insert('0', date_day)
        self.event_date_day.pack(side=ctk.LEFT, padx=2, pady=2)
    # separator
        separator_0 = ctk.CTkLabel(date_frame, text_color=Colors.TEXT_COLOR, text='/', font=ctk.CTkFont('Comic sans', 32))
        separator_0.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W)
    # month
        self.event_date_month = ctk.CTkEntry(date_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=50, corner_radius=0,
                                font=ctk.CTkFont('Comic Sans', 32), justify=ctk.RIGHT,
                                text_color=Colors.TEXT_COLOR)
        date_month = f'{self.event.split(',',2)[1].split('.',2)[1]}'
        self.event_date_month.insert('0', date_month)
        self.event_date_month.pack(side=ctk.LEFT, padx=2, pady=2)
    # separator
        separator_1 = ctk.CTkLabel(date_frame, text_color=Colors.TEXT_COLOR, text='/', font=ctk.CTkFont('Comic sans', 32))
        separator_1.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W)
    # year
        self.event_date_year = ctk.CTkEntry(date_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=88, corner_radius=0,
                                font=ctk.CTkFont('Comic Sans', 32), justify=ctk.RIGHT,
                                text_color=Colors.TEXT_COLOR)
        date_year = f'{self.event.split(',',2)[1].split('.',3)[2]}'
        self.event_date_year.insert('0', date_year)
        self.event_date_year.pack(side=ctk.LEFT, padx=2, pady=2)

    def content_time(self) -> None:
    # time frame
        time_frame = ctk.CTkFrame(self, fg_color=Colors.MAIN_COLOR)
        time_frame.pack(side=ctk.TOP, padx=40, pady=5, anchor=ctk.W)
    # time label
        label_title = ctk.CTkLabel(time_frame, fg_color=Colors.MAIN_COLOR,
                                    text_color=Colors.TEXT_COLOR, text='Time: ', width=50, corner_radius=0,
                                    font=ctk.CTkFont('Comic Sans', 32))
        label_title.pack(side=ctk.LEFT, padx=2, pady=2)
    # hour
        self.event_time_hour = ctk.CTkEntry(time_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=50, corner_radius=0,
                                font=ctk.CTkFont('Comic Sans', 32), justify=ctk.RIGHT,
                                text_color=Colors.TEXT_COLOR)
        time_hour = (self.event.split(',',2)[2]).split(':')[0]
        self.event_time_hour.insert('0', time_hour)
        self.event_time_hour.pack(side=ctk.LEFT, padx=5, pady=5, anchor=ctk.W)
    # separator
        separator = ctk.CTkLabel(time_frame, text_color=Colors.TEXT_COLOR, text=':',
                                font=ctk.CTkFont('Comic sans', 32))
        separator.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W)
    # minute 
        self.event_time_minutes = ctk.CTkEntry(time_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=50, corner_radius=0,
                                font=ctk.CTkFont('Comic Sans', 32), justify='right',
                                text_color=Colors.TEXT_COLOR)
        time_minutes = (self.event.split(',',3)[2]).split(':')[1]
        self.event_time_minutes.insert('0', time_minutes)
        self.event_time_minutes.pack(side=ctk.LEFT, padx=5, pady=5, anchor=ctk.W)

    def content_notes(self) -> None:
    # notes label
        spacing_0 = ctk.CTkFrame(self, width=1, height=1, corner_radius=0,
                                fg_color=Colors.MAIN_COLOR)
        spacing_0.pack(side=ctk.TOP, padx=15, pady=5, fill=ctk.X)
        notes_title = ctk.CTkLabel(spacing_0, fg_color=Colors.MAIN_COLOR,
                                    text_color=Colors.TEXT_COLOR, text='Notes: ',
                                    width=50, corner_radius=0,
                                    font=ctk.CTkFont('Comic Sans', 32))
        notes_title.pack(side=ctk.LEFT, padx=2, pady=2)
    # notes
        self.event_notes = ctk.CTkTextbox(self, fg_color=Colors.MAIN_COLOR, border_width=2,
                                        border_color=Colors.BACKGROUND, corner_radius=0,
                                        wrap='word', font=ctk.CTkFont('Comic Sans', 32),
                                        text_color=Colors.TEXT_COLOR)
        notes = f'{self.event.split(',',3)[3].replace(' /n|', '\n').replace(' /r|', '\r')}'
        self.event_notes.insert('0.0', notes)
        self.event_notes.pack(side=ctk.TOP, padx=50, anchor=ctk.N,
                            fill=ctk.BOTH, expand=True)
    # spacing
        spacing_1 = ctk.CTkFrame(self, width=1, height=1, corner_radius=0,
                                fg_color=Colors.MAIN_COLOR)
        spacing_1.pack(side=ctk.BOTTOM, padx=50, pady=100)

    def remove_event_button(self) -> None:
        remove_button = ctk.CTkButton(self.buttons_frame, text_color=Colors.TEXT_COLOR, text=' REMOVE ',
                                        command=self.remove_event,
                                        height=50, width=50, corner_radius=0,
                                        font=('Comic Sans', 21))
        remove_button.pack(side=ctk.LEFT, padx=7, pady=3, anchor=ctk.W)

    def save_edited_event_button(self) -> None:
        remove_button = ctk.CTkButton(self.buttons_frame, text_color=Colors.TEXT_COLOR, text=' SAVE ',
                                        command=self.edit_event,
                                        height=50, width=50, corner_radius=0,
                                        font=('Comic Sans', 21))
        remove_button.pack(side=ctk.LEFT, padx=7, pady=3, anchor=ctk.W)

    def remove_event(self) -> None:
        self.event_bar.remove_from_dictionary(self.key)
        remove_event(self.events, self.key)
        self.destroy()

    def edit_event(self) -> None:
    # title
        new_title: str = self.title.get()
    # date
        new_date_day: str = self.event_date_day.get()
        new_date_month: str = self.event_date_month.get()
        new_date_year: str = self.event_date_year.get()
    # time
        new_time_hour: str = self.event_time_hour.get()
        new_time_minutes: str = self.event_time_minutes.get()
    # notes
        new_notes: str = self.event_notes.get('0.0', 'end')
    # all together
        new_event_data: str = f'{new_title},{new_date_day}.{new_date_month}.{new_date_year},{new_time_hour}:{new_time_minutes},{new_notes[:-1]}'
        if self.original_info == new_event_data:
            return
        self.event_bar.edit_in_dictionary(self.key, new_event_data)
        edit_event(self.events, self.key, new_event_data)
