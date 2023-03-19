from PySide6.QtCore import QTimer
from src.stock_watch import database

class NewsData:
    def __init__(self):
        self.changed_callbacks = []
        self.timer = None
        self.db_connection = None
        self.posted_news = []
        self.started = False

    def start(self):
        if not self.started:
            self.started = True

            # Move to models
            self.db_connection = database.connect()

            # Populate with initial data
            self.check_database()

            # Check database
            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.check_database)
            self.timer.start()

    def check_database(self, initial_many: int = 100, many: int = 10):
        cursor = self.db_connection.cursor()

        if len(self.posted_news) == 0:
            cursor.execute("SELECT * FROM reddit_submissions ORDER BY created_utc DESC")
            reddit_submissions = cursor.fetchmany(initial_many)
            if len(reddit_submissions) > 0:
                for submission in reddit_submissions:
                    if submission not in self.posted_news:
                        self.posted_news.append(submission)
                        self._changed()
        else:
            cursor.execute("SELECT * FROM reddit_submissions ORDER BY created_utc DESC")
            reddit_submissions = cursor.fetchmany(many)
            if len(reddit_submissions) > 0:
                for submission in reddit_submissions:
                    if submission not in self.posted_news:
                        self.posted_news.append(submission)
                        self._changed()


    def changed(self, callback):
        self.changed_callbacks.append(callback)

    def _changed(self):
        for callback in self.changed_callbacks:
            # -1 meaning the last element of the list
            callback(self.posted_news[-1])