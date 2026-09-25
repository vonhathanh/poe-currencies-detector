import cv2
import numpy as np
import matplotlib.pyplot as plt
import re

from paddleocr import TextDetection, TextRecognition


IMG_MAX_WIDTH = 1024


CURRENCY_PATTERN = re.compile('^\d+x ')

MINIMUM_CURRENCY_BOX_WIDTH = 100
MAXIMUM_CURRENCY_BOX_WIDTH = 530
MINIMUM_CURRENCY_BOX_HEIGHT = 25
MAXIMUM_CURRENCY_BOX_HEIGHT = 55

text_detection_model = TextDetection(engine='transformers')
text_recognition_model = TextRecognition(engine='transformers')


def resize_img(input_img: np.ndarray):
    if len(input_img.shape) == 2:
        height, width = input_img.shape
    elif len(input_img.shape) == 3:
        height, width, _ = input_img.shape
    else:
        raise ValueError(f'expect input image to has shape = 2 or 3, got: {len(input_img.shape)}')

    if width > IMG_MAX_WIDTH:
        ratio = IMG_MAX_WIDTH / width
        width = int(ratio * width)
        height = int(ratio * height)
    else:
        ratio = 1.0
    return cv2.resize(input_img, (width, height), interpolation=cv2.INTER_LINEAR), ratio


def notebook_imshow(img):
    plt.figure(figsize=(16, 8))
    # RGB img
    if len(img.shape) == 3:
        plt.imshow(img)
    # gray img
    elif len(img.shape) == 2: 
        plt.imshow(img, cmap='gray')
    # god's img
    else:
        raise ValueError(f"input img has malformed shape, expected input are 2d array & 3d array, got: {len(img.shape)}d array")
    plt.axis('off')
    plt.show()

def load_currencies_set():
    currencies = set()
    with open('./data/currencies.txt', 'r') as f:
        data = f.readlines()
        for name in data:
            currencies.add(name.strip().lower())
    return currencies

def find_currency_coords(img, currencies_set):
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
    txts = text_recognition_model.predict(valid_boxes, batch_size=32)
    
    coords = []
    # enumerate over all bounding boxes
    for txt_obj in txts:
        text = txt_obj["rec_text"].lower()
        print('text ', text)
        # check text has prefix like: 1x, 2x,... nx + currency name
        match = CURRENCY_PATTERN.match(text)
        if match:
            # remove the prefix to get the original currency name only
            end_pos = match.end()
            text = text[end_pos:]    
        if text not in currencies_set:
            continue
        x = int(top_left[0]) + width // 2
        y = int(top_left[1]) + height // 2
        coords.append((x, y, text))
    return coords
