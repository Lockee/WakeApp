


from wakeapp.gui.app import app
from wakeapp.utils.bvg_api import bvg_api


def main() -> None:
    bvg = bvg_api('https://v5.bvg.transport.rest')
    app(bvg).run()

if __name__=='__main__':
    main()