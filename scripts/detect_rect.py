import os
import sys 
import cv2
import glob
from rapidocr import RapidOCR

sys.path.append(os.path.abspath('..'))


MINIMUM_CURRENCY_BOX_WIDTH = 100
MAXIMUM_CURRENCY_BOX_WIDTH = 480
MINIMUM_CURRENCY_BOX_HEIGHT = 25
MAXIMUM_CURRENCY_BOX_HEIGHT = 55


img_filenames = glob.glob('imgs/*.PNG')

engine = RapidOCR()

for filename in img_filenames:
    img = cv2.imread(filename)

    result = engine(img)

    for box in result.boxes:
        top_left, top_right, bottom_right, bottom_left = box
        width = int(top_right[0] - top_left[0])
        height = int(bottom_left[1] - top_left[1])
        if MAXIMUM_CURRENCY_BOX_WIDTH > width > MINIMUM_CURRENCY_BOX_WIDTH and MAXIMUM_CURRENCY_BOX_HEIGHT > height > MINIMUM_CURRENCY_BOX_HEIGHT:
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