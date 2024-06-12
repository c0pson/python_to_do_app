import customtkinter as ctk

# Imported properties
from properties import Colors

class TopFrame(ctk.CTkFrame):
    """In app frame asking for details of new event."""
    def __init__(self, master, add_label) -> None:
        self.master = master
        self.add_label = add_label
        super().__init__(self.master, fg_color=Colors.BACKGROUND, 
                        corner_radius=0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER,
                    relwidth=1.01, relheight=1.01)
        self.descendants: list = []
        self.setup()

    def setup(self) -> None:
        self.get_all_widgets(self.master)
        self.disable_all_widgets()
        self.close_dialog_bar()
        self.new_event_name()
        self.new_event_date()
        self.new_event_time()
        self.new_event_note()

    def get_all_widgets(self, master) -> None:
        for child in master.winfo_children():
            if not isinstance(child, AddNewEvent):
                self.get_all_widgets(child)
                self.descendants.append(child)

    def disable_all_widgets(self) -> None:
        for widget in self.descendants:
            try:
                widget.configure(state='disabled')
            except Exception:
                pass

    def enable_all_widgets(self) -> None:
        for widget in self.descendants:
            try:
                widget.configure(state='normal')
            except Exception:
                pass

    def close_dialog_bar(self):
        bar_frame = ctk.CTkFrame(self, fg_color=Colors.BACKGROUND,
                                corner_radius=0)
        bar_frame.pack(side=ctk.TOP, padx=4, pady=4, fill=ctk.X)
        close_button = ctk.CTkButton(bar_frame, text='✕', command=self.exit,
                                    width=25, height=25, anchor=ctk.CENTER,
                                    corner_radius=0, fg_color=Colors.RED,
                                    hover_color=Colors.RED_HOVER,
                                    text_color=Colors.TEXT_COLOR)
        close_button.pack(side=ctk.RIGHT, padx=3, pady=3)
        accept_button = ctk.CTkButton(bar_frame, text='✓', command=self.exit,
                                    width=25, height=25, anchor=ctk.CENTER,
                                    corner_radius=0, fg_color=Colors.GREEN,
                                    hover_color=Colors.GREEN_HOVER,
                                    text_color=Colors.TEXT_COLOR)
        accept_button.pack(side=ctk.RIGHT, padx=3, pady=3)

    def exit(self) -> None:
        self.enable_all_widgets()
        self.destroy()
        self.add_label.forget_top_frame()

    def add_event(self) -> None:
        # TODO: appending file logic here
        self.enable_all_widgets()
        self.destroy()
        self.add_label.forget_top_frame()

    def new_event_name(self) -> None:
    # title frame
        name_frame = ctk.CTkFrame(self, fg_color=Colors.MAIN_COLOR)
        name_frame.pack(side=ctk.TOP, padx=15, pady=15, fill=ctk.X)
    # title
        self.title = ctk.CTkEntry(name_frame, fg_color=Colors.MAIN_COLOR,
                            border_color=Colors.MAIN_COLOR, corner_radius=0,
                            font=ctk.CTkFont('Comic Sans', 32),
                            text_color=Colors.TEXT_COLOR, width=9000)
        self.title.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W, fill=ctk.X)

    def new_event_date(self) -> None:
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
        self.event_date_day.pack(side=ctk.LEFT, padx=2, pady=2)
    # separator
        separator_0 = ctk.CTkLabel(date_frame, text_color=Colors.TEXT_COLOR, text='/', font=ctk.CTkFont('Comic sans', 32))
        separator_0.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W)
    # month
        self.event_date_month = ctk.CTkEntry(date_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=50, corner_radius=0,
                                font=ctk.CTkFont('Comic Sans', 32), justify=ctk.RIGHT,
                                text_color=Colors.TEXT_COLOR)
        self.event_date_month.pack(side=ctk.LEFT, padx=2, pady=2)
    # separator
        separator_1 = ctk.CTkLabel(date_frame, text_color=Colors.TEXT_COLOR, text='/', font=ctk.CTkFont('Comic sans', 32))
        separator_1.pack(side=ctk.LEFT, padx=0, pady=0, anchor=ctk.W)
    # year
        self.event_date_year = ctk.CTkEntry(date_frame, fg_color=Colors.MAIN_COLOR,
                                border_color=Colors.BACKGROUND, width=88, corner_radius=0,
                                font=ctk.CTkFont('Comic Sans', 32), justify=ctk.RIGHT,
                                text_color=Colors.TEXT_COLOR)
        self.event_date_year.pack(side=ctk.LEFT, padx=2, pady=2)

    def new_event_time(self) -> None:
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
        self.event_time_minutes.pack(side=ctk.LEFT, padx=5, pady=5, anchor=ctk.W)

    def new_event_note(self) -> None:
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
        self.event_notes.pack(side=ctk.TOP, padx=50, anchor=ctk.N,
                            fill=ctk.BOTH, expand=True)
    # spacing
        spacing_1 = ctk.CTkFrame(self, width=1, height=1, corner_radius=0,
                                fg_color=Colors.MAIN_COLOR)
        spacing_1.pack(side=ctk.BOTTOM, padx=50, pady=100)

class AddNewEvent(ctk.CTkLabel):
    def __init__(self, master) -> None:
        self.master = master
        super().__init__(self.master, 
                        text='+', font=('Comic Sans', 41),
                        text_color=Colors.TEXT_COLOR, fg_color=Colors.BACKGROUND,
                        bg_color=Colors.MAIN_COLOR, height=50,
                        width=50, corner_radius=0)
        self.top_frame: TopFrame | None= None
        self.bind('<Button-1>', lambda event: self.ask_for_new_event(event))
        self.setup()

    def setup(self) -> None:
        pass

    def ask_for_new_event(self, event) -> None:
        if not self.top_frame:
            self.top_frame = TopFrame(self.master, self)

    def forget_top_frame(self):
        self.top_frame = None
