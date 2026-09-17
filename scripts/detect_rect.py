import os
import sys 
import cv2
import glob
sys.path.append(os.path.abspath('..'))
from rapidocr import RapidOCR

img_filenames = glob.glob('imgs/*.PNG')

engine = RapidOCR()
for filename in img_filenames:
    img = cv2.imread(filename)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    result = engine(gray_img)

    for box in result.boxes:
        top_left, top_right, bottom_right, bottom_left = box
        cv2.rectangle(img, (int(top_left[0]), int(top_left[1])), (int(bottom_right[0]), int(bottom_right[1])), (0, 255, 0), 1)
    cv2.imshow("output", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

# class Rect:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.height = 1
#         self.width = 1

#     def set_height(self, value):
#         self.height = value

#     def set_width(self, value):
#         self.width = value

#     def __str__(self):
#         return f"x={self.x}, y={self.y}, height={self.height}, width={self.width}"

# MINIMUM_CURRENCY_BOX_WIDTH = 120
# MAXIMUM_CURRENCY_BOX_WIDTH = 500
# MINIMUM_CURRENCY_BOX_HEIGHT = 30
# MAXIMUM_CURRENCY_BOX_HEIGHT = 60
