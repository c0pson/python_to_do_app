import customtkinter as ctk

# Imported properties
from properties import Colors

class TopFrame(ctk.CTkFrame):
    def __init__(self, master, add_label) -> None:
        self.master = master
        self.add_label = add_label
        super().__init__(self.master, fg_color=Colors.BACKGROUND, 
                        corner_radius=0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER,
                    relwidth=0.6, relheight=0.6)
        self.descendants = []
        self.setup()

    def setup(self) -> None:
        self.get_all_widgets(self.master)
        self.disable_all_widgets()
        self.close_dialog_bar()

    def get_all_widgets(self, master) -> list:
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
        bar_frame.pack(side=ctk.TOP, padx=2, pady=2, fill=ctk.X)
        close_button = ctk.CTkButton(bar_frame, text='X', command=self.exit,
                                    width=20, height=20, anchor=ctk.CENTER,
                                    corner_radius=0, fg_color=Colors.RED,
                                    hover_color=Colors.RED_HOVER,
                                    text_color=Colors.TEXT_COLOR)
        close_button.pack(side=ctk.RIGHT, padx=3, pady=3)

    def exit(self):
        self.enable_all_widgets()
        self.destroy()
        self.add_label.forget_top_frame()

class AddNewEvent(ctk.CTkLabel):
    def __init__(self, master) -> None:
        self.master = master
        super().__init__(self.master, 
                        text='+', font=('Comic Sans', 41),
                        text_color=Colors.TEXT_COLOR, fg_color=Colors.BACKGROUND,
                        bg_color=Colors.MAIN_COLOR, height=50,
                        width=50, corner_radius=0)
        self.top_frame = None
        self.bind('<Button-1>', lambda event: self.ask_for_new_event(event))
        self.setup()

    def setup(self) -> None:
        pass

    def ask_for_new_event(self, event) -> None:
        if not self.top_frame:
            self.top_frame = TopFrame(self.master, self)

    def forget_top_frame(self):
        self.top_frame = None
