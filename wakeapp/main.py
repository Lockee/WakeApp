import tkinter as tk
from GUI.MainFrame import MainFrame


def start() -> None:
    root = tk.Tk()
    mf = MainFrame(root)

if __name__=='__main__':
    start()