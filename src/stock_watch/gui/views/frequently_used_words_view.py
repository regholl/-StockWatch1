from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget, QWidget, QListWidget

from src.stock_watch.gui.models.news_data import NewsData
from src.stock_watch.gui.models.word_frequency import WordFrequency


class FrequentlyUsedWordsView(QDockWidget):
    def __init__(self, parent):
        super().__init__("Word Frequency", parent)
        self.news_data = NewsData()
        self.word_frequency = WordFrequency()

        self.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        self.setWidget(QWidget(self))

        self.visibilityChanged.connect(self.visibility_changed)
        self.news_data.changed(self.news_data_changed)

        self.list_widget = QListWidget()
        self.setWidget(self.list_widget)

    def visibility_changed(self, visible):
        if visible:
            # Start news_data update loop
            self.news_data.start()
            # Set width of widget to 1/4 of the window
            self.setFixedWidth(int(self.parent().width() / 6))

    def news_data_changed(self, data):
        # Create a new widget with the data
        string_rep = f"{data[18]}"
        list_of_words = string_rep.split()
        self.word_frequency.add_words(list_of_words)
        frequent_words = self.word_frequency.get_most_frequent(20)
        # print(frequent_words)
        self.list_widget.clear()
        for word in frequent_words:
            self.list_widget.addItem(f"{word} - {self.word_frequency.get_frequency(word)}")
        self.update()