from Models import Post
import datetime

class API:
    def __init__(self, config=None):
        self.config = config

    def add_post(self, post: Post):
        # Simulate a POST request to backend
        return True

    def get_posts(self, start_date: datetime.datetime, end_date: datetime.datetime):
        # Simulate fetching posts from a backend
        return [
            Post("Adam", "Python is a snake", datetime.datetime(2021, 5, 1)),
            Post("Sara", "Python is a programming language", datetime.datetime(2021, 5, 3))
        ]
