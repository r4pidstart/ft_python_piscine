import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ex04"))

from ft_calculator import calculator
a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)
