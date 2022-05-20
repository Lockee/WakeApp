import tkinter as tk
from tkinter import ttk
from tkinter import font
from wakeapp.controller.app_controller import AppController
from wakeapp.utils.bvg_api import bvg_api

class app:
    def __init__(self) -> None:
        self.controller = AppController()
        self.root = tk.Tk()
        self.window_height = 500
        self.window_width = 700

        # basic internal values
        self.arrival_time_value = tk.StringVar(value="19:00")
        self.prep_time_value = tk.StringVar(value="00:30")
        self.start_point_value = tk.StringVar(value="")
        self.destination_value = tk.StringVar(value="")
        self.wake_time = tk.StringVar(value="00:00")

        self.init_gui()
        

    def init_gui(self) -> None:
        self.root.resizable(True, True)
        self.root.title("WakeApp")
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.configure(bg="#E5E5E5")
        default_font = font.nametofont('TkDefaultFont')
        default_font.configure(size=16)
        self.root.option_add("*Font", default_font)

        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.X, expand=True)

        self.arrival_label = ttk.Label(self.frame, text="Ankuftszeit (HH:MM): ")
        self.arrival_label.pack(fill=tk.X, expand=True)

        self.arrival_entry = ttk.Entry(self.frame, textvariable=self.arrival_time_value)
        self.arrival_entry.pack(fill="x", expand=True)


        # time to get ready input
        self.prep_label = ttk.Label(self.frame, text="Benötigte Zeit zum fertig zu machen (HH:MM): ")
        self.prep_label.pack(fill="x", expand=True)

        self.prep_entry = ttk.Entry(self.frame, textvariable=self.prep_time_value)
        self.prep_entry.pack(fill="x", expand=True)


        # origin input
        self.start_label = ttk.Label(self.frame, text="Wohnort: ")
        self.start_label.pack(fill="x", expand=True)

        self.start_entry = ttk.Entry(self.frame, textvariable=self.start_point_value)
        self.start_entry.pack(fill="x", expand=True)


        # destination input
        self.destination_label = ttk.Label(self.frame, text="Zielort: ")
        self.destination_label.pack(fill="x", expand=True)

        self.destination_input = ttk.Entry(self.frame, textvariable=self.destination_value)
        self.destination_input.pack(fill="x", expand=True)

        # display wake time
        self.wake_time_label = ttk.Label(self.frame, text="Weckzeit:")
        self.wake_time_label.pack()
        self.wake_time_display = ttk.Label(self.frame, textvariable=self.wake_time)
        self.wake_time_display.pack()

        # submit button
        self.submit_button = ttk.Button(self.frame, text="berechnen", command=self.submit_click)
        self.submit_button.pack()

    def submit_click(self):
        ...

    def run(self):
        self.root.mainloop()
