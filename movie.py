from abc import ABC, abstractmethod

class Movie(ABC):
    def __init__(self, title, released_year, director, genre):
        self.title = title
        self.released_year = released_year
        self.director = director
        self.genre = genre

    @abstractmethod
    def display_info(self):
        pass