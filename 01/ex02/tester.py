# import os
# os.environ["OPENCV_LOG_LEVEL"] = "FATAL"
from load_image import ft_load


print(ft_load("../imgs/landscape.png"))

# added testcases
print(ft_load("../imgs/image.jpg"))  # jpg/jpeg
print(ft_load("../imgs"))  # folder
print(ft_load("asdfadsf"))  # ?
print(ft_load(123))  # ???
