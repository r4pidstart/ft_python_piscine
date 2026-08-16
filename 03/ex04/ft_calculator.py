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

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """calculate dot product"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("V1 and V2 must be lists")
        if len(V1) != len(V2):
            raise ValueError("V1 and V2 must be of the same length")
        if not all(isinstance(x, numbers.Number) for x in V1) or \
           not all(isinstance(x, numbers.Number) for x in V2):
            raise TypeError("All elements in V1 and V2 must be numbers")
        result = sum(a * b for a, b in zip(V1, V2))
        print(f'Dot product is: {result}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add two vectors"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("V1 and V2 must be lists")
        if len(V1) != len(V2):
            raise ValueError("V1 and V2 must be of the same length")
        if not all(isinstance(x, numbers.Number) for x in V1) or \
           not all(isinstance(x, numbers.Number) for x in V2):
            raise TypeError("All elements in V1 and V2 must be numbers")
        result = [a + b for a, b in zip(V1, V2)]
        print(f'Add vector is: {result}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """subtract two vectors"""
        if not isinstance(V1, list) or not isinstance(V2, list):
            raise TypeError("V1 and V2 must be lists")
        if len(V1) != len(V2):
            raise ValueError("V1 and V2 must be of the same length")
        if not all(isinstance(x, numbers.Number) for x in V1) or \
           not all(isinstance(x, numbers.Number) for x in V2):
            raise TypeError("All elements in V1 and V2 must be numbers")
        result = [a - b for a, b in zip(V1, V2)]
        print(f'Sous Vector is {result}')
