# import os
# os.environ["OPENCV_LOG_LEVEL"] = "FATAL"
from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red
import numpy


loaded_img: numpy.ndarray = ft_load("../imgs/landscape.png")
print(loaded_img)

ft_invert(loaded_img)
ft_red(loaded_img)
ft_green(loaded_img)
ft_blue(loaded_img)
ft_grey(loaded_img)

print(ft_invert.__doc__)

# added testcases
ft_invert("what is this")
