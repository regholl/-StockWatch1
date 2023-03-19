from PySide6.QtWidgets import QListWidget
import webbrowser


class NewsFeedListWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.itemDoubleClicked.connect(self.item_double_clicked)

    def item_double_clicked(self, item):
        text = item.text()
        # Get the URL from the text
        url = self.get_website_from_text(text)
        if url is None:
            return
        print(f"Opening news story in default browser: {item.text()}")
        webbrowser.open_new_tab(url)

    def get_website_from_text(self, text):
        split_text = text.split(", ")
        for item in split_text:
            if item.startswith("http"):
                return item
        return None

    def filter_news(self, filter_text):
        for i in range(self.count()):
            item = self.item(i)
            if filter_text in item.text():
                item.setHidden(False)
            else:
                item.setHidden(True)
