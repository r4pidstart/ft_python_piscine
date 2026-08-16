import numbers


class calculator:
    """this is a calculator class"""
    def __init__(self, init_value: list[int | float]):
        """constructor for calculator, gets list of numbers"""
        self.value = init_value

    def __add__(self, object: int | float) -> None:
        """add object to each value of value"""
        if not isinstance(object, numbers.Number):
            raise TypeError("object must be a number")
        self.value = [x + object for x in self.value]
        print(self.value)

    def __sub__(self, object: int | float) -> None:
        """subtract object from each value of value"""
        if not isinstance(object, numbers.Number):
            raise TypeError("object must be a number")
        self.value = [x - object for x in self.value]
        print(self.value)

    def __mul__(self, object: int | float) -> None:
        """multiply each value of value by object"""
        if not isinstance(object, numbers.Number):
            raise TypeError("object must be a number")
        self.value = [x * object for x in self.value]
        print(self.value)

    def __truediv__(self, object: int | float) -> None:
        """divide each value of value by object"""
        if not isinstance(object, numbers.Number):
            raise TypeError("object must be a number")
        if object == 0:
            raise ZeroDivisionError("division by zero")
        self.value = [x / object for x in self.value]
        print(self.value)
