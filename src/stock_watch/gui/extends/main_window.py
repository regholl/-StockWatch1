from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from screeninfo import get_monitors

from src.stock_watch.gui.extends.menu_bar import MenuBar
from src.stock_watch.gui.threader import Worker
from src.stock_watch.gui.views.news_feed_view import NewsFeedView
from src.stock_watch.gui.views.frequently_used_words_view import FrequentlyUsedWordsView
from src.stock_watch.gui.views.search_bar_widget import SearchBarWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.search_bar_widget = None
        self.news_feed_widget = None
        self.frequently_used_words_widget = None

        self.setup_window_geometry()
        self.setWindowTitle("Stock Watch")
        self.setMenuBar(MenuBar(self))

        self.add_widgets()

        self.show()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def add_widgets(self):
        # Add search bar widget
        self.search_bar_widget = SearchBarWidget(self)
        self.search_bar_widget.on_text_changed(self.search_bar_on_text_changed_callback)
        search_container_layout = QVBoxLayout()
        search_container_layout.addWidget(self.search_bar_widget)
        search_container = QWidget()
        search_container.setLayout(search_container_layout)

        self.frequently_used_words_widget = FrequentlyUsedWordsView(self)
        self.news_feed_widget = NewsFeedView(self)
        news_container_layout = QHBoxLayout()
        news_container_layout.addWidget(self.frequently_used_words_widget)
        news_container_layout.addWidget(self.news_feed_widget)
        news_container = QWidget()
        news_container.setLayout(news_container_layout)

        combined_container = QWidget()
        combined_container_layout = QVBoxLayout()
        combined_container_layout.addWidget(search_container)
        combined_container_layout.addWidget(news_container)
        combined_container.setLayout(combined_container_layout)

        self.setCentralWidget(combined_container)

    def setup_window_geometry(self):
        # Get the primary monitor
        monitor = get_monitors()[0]
        # Set the geometry of the window to the monitor's center
        self.setGeometry(int(monitor.width/4), int(monitor.height/4), int(monitor.width/2), int(monitor.height/2))

    def check_database(self):
        worker = Worker(self.check_for_research)
        self.threadpool.start(worker)

    def search_bar_on_text_changed_callback(self, text):
        # Ask the news feed widget to filter the news feed
        self.news_feed_widget.filter_news(text)
