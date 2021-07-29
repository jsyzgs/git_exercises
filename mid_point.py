import os
import numpy as np
import math
from PIL import Image

midpoint = (0,0)
pil_image = Image.open('1.jpg')


if __name__=='__main__':
    x = 2
    y = 2
    print(math.degrees(math.atan2(y, x)))
