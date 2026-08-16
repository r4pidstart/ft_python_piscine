from abc import ABC, abstractmethod


class Character(ABC):
    """docstring for character"""
    def __init__(self, first_name, is_alive=True):
        """constrctor for character class, init first_name and is_alive"""
        super().__init__()
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """abstract method to set is_alive of this character to False"""
        pass


class Stark(Character):
    """docstring for stark"""
    def die(self):
        """set is_alive of this character to False"""
        self.is_alive = False
