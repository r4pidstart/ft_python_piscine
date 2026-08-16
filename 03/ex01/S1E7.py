from S1E9 import Character


class Baratheon(Character):
    """class for barateon family"""
    def __init__(self, first_name, is_alive=True):
        """constructor for barateon class, init first_name and is_alive
        and set color of eyes and hair"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """return string representation of this character"""
        return f"""__str__ Vector: (
            '{self.family_name}', '{self.eyes}', '{self.hairs}'
        )"""

    def __repr__(self):
        """return string representation of this character"""
        return f"""__repr__ Vector: (
            '{self.family_name}', '{self.eyes}', '{self.hairs}'
        )"""

    def die(self):
        """set is_alive of this character to False"""
        self.is_alive = False


class Lannister(Character):
    """class for lannister family"""
    def __init__(self, first_name, is_alive=True):
        """constructor for lannister class, init first_name and is_alive
       and set color of eyes and hair"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """return string representation of this character"""
        return f"""__str__ Vector: (
            '{self.family_name}', '{self.eyes}', '{self.hairs}'
        )"""

    def __repr__(self):
        """return string representation of this character"""
        return f"""__repr__ Vector: (
            '{self.family_name}', '{self.eyes}', '{self.hairs}'
        )"""

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        """make a new lannister character with first_name and is_alive"""
        return Lannister(first_name, is_alive)

    def die(self):
        """set is_alive of this character to False"""
        self.is_alive = False
