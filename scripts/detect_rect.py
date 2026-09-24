import os
import sys 
import cv2
import time
import glob
from paddleocr import TextDetection, TextRecognition

sys.path.append(os.path.abspath('..'))

from lib import *

currencies = load_currencies_set()

img_filenames = glob.glob('imgs/*.PNG')

text_detection_model = TextDetection(engine='transformers')
text_recognition_model = TextRecognition(engine='transformers')

for filename in img_filenames:

    print('processing ', filename)

    img = cv2.imread(filename)

    boxes = text_detection_model.predict(img)[0]["dt_polys"]

    valid_boxes = []

    for box in boxes:
        top_left, top_right, _, bottom_left = box
        width = int(top_right[0] - top_left[0])
        height = int(bottom_left[1] - top_left[1])
        # check if the box has valid width & height
        if MAXIMUM_CURRENCY_BOX_WIDTH > width > MINIMUM_CURRENCY_BOX_WIDTH and MAXIMUM_CURRENCY_BOX_HEIGHT > height > MINIMUM_CURRENCY_BOX_HEIGHT:
            cropped_region = img[top_left[1]:bottom_left[1], top_left[0]:top_right[0], :]
            valid_boxes.append(cropped_region)
    start = time.time()
    txts = text_recognition_model.predict(valid_boxes, batch_size=32)
    end = time.time()
    print('cost ', end - start)
