from src.stock_watch.gui.extends.main_window import MainWindow
from ..extends.application import Application
import qdarktheme


class MainWindowController(object):
    def __init__(self):
        self.app = None
        self.main_window = None
        self.widget = None

    def show(self):
        self.app = Application([])
        qdarktheme.setup_theme("auto")
        self.main_window = MainWindow()
        self.app.exec()
