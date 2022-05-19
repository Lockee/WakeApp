import tkinter as tk
from utils.bvg_api import bvg_api


class MainFrame():
    def __init__(self, parent: tk.Tk) -> None:
        bvg = bvg_api('https://v5.bvg.transport.rest')
        id1 = bvg.fetch_location_id('Rathaus Neukölln')
        id2 = bvg.fetch_location_id('Mehringdamm')
        print(bvg.fetch_depature_arrival_time(id1, id2, "23:30"))
