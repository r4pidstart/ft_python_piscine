from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """class for king"""
    def __init__(self, first_name, is_alive=True):
        """constructor for king"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, eyes):
        """set eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """set hairs"""
        self.hairs = hairs

    def get_eyes(self):
        """set eyes"""
        return self.eyes

    def get_hairs(self):
        """set hairs"""
        return self.hairs
