# import os
# os.environ["OPENCV_LOG_LEVEL"] = "FATAL"
from load_image import ft_load
from rotate import ft_rotate
import numpy


loaded_img: numpy.ndarray = ft_load("../imgs/animal.png")
ft_rotate(loaded_img, 100, 400, 400, False)

# added testcases
ft_rotate(loaded_img, 100000, 400, 400, True)
ft_rotate(loaded_img, 768, 1024, 400, True)
ft_rotate(loaded_img, -13, 400, 400, True)
ft_rotate("what is this", 400, 400, 400, True)
