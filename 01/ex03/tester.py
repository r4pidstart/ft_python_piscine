# import os
# os.environ["OPENCV_LOG_LEVEL"] = "FATAL"
from load_image import ft_load
from zoom import ft_zoom
import numpy


loaded_img: numpy.ndarray = ft_load("../imgs/animal.png")
print(ft_zoom(loaded_img, 100, 400, 400, 400, True))
print(ft_zoom(loaded_img, 100, 400, 400, 400, False))

# added testcases
print(ft_zoom(loaded_img, 100000, 400, 400, 400, True))
print(ft_zoom(loaded_img, 768, 1024, 400, 400, True))
print(ft_zoom(loaded_img, -13, 400, 400, 400, True))
print(ft_zoom("what is this", 400, 400, 400, 400, True))
