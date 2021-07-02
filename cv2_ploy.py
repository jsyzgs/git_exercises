import cv2
import numpy as np
line_thickness = 3

box = []
for i in range(3):
    box.extend([[1,2]])


bgr_3d_array = cv2.imread(r'C:\Users\GS\Downloads\black_screen.jpg')
areas = [[[0, 0], [896, 0], [896, 544], [0, 544]],[[100,100],[200,100],[200,300],[100,300]]]
for area in areas:
    pts = np.array(area, np.int32)
    cv2.polylines(bgr_3d_array, [pts], True, (168, 0, 225), thickness=line_thickness)

cv2.imshow('asd',bgr_3d_array)
cv2.waitKey(0)
