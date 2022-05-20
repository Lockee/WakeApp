from wakeapp.utils.bvg_api import bvg_api

class AppController:
    def __init__(self) -> None:
        self.bvg = bvg_api('https://v5.bvg.transport.rest')
