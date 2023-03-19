from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget, QWidget
from src.stock_watch.gui.models.news_data import NewsData
from src.stock_watch.gui.views.new_feed_list_widget import NewsFeedListWidget


class NewsFeedView(QDockWidget):
    def __init__(self, parent):
        super().__init__("News Feed", parent)
        self.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.setWidget(QWidget(self))
        self.news_data = NewsData()
        self.news_data.changed(self.news_data_changed)

        self.visibilityChanged.connect(self.visibility_changed)

        self.list_widget = NewsFeedListWidget(self)
        self.setWidget(self.list_widget)

    def visibility_changed(self, visible):
        if visible:
            self.news_data.start()

    def news_data_changed(self, data):
        # Create a new widget with the data
        string_rep = f"{data[18]}, {data[20]}"
        self.list_widget.addItem(string_rep)
        self.list_widget.scrollToBottom()

    def filter_news(self, filter_text):
        self.list_widget.filter_news(filter_text)
