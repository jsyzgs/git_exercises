'''
@author: shuaigao
@file: open_use_numpy.py
@time: 2021/12/3 15:39
@desc:
'''

import numpy as np
import cv2
from PIL import Image


file_path = r'C:\Users\GS\Desktop\rmb_100_shu.jpg'
data_np = np.fromfile(file_path,dtype=np.byte)
img = cv2.imread(file_path)
ret,buf = cv2.imencode(".jpg",img)

img_bin = Image.fromarray(np.uint8(buf)).tobytes()
print('done')