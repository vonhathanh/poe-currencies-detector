import cv2
import numpy as np

IMG_MIN_WIDTH = 1000.0
IMG_MIN_HEIGHT = 1000.0

def resize_img(input_img: np.ndarray):
    height, width = input_img.shape
    if width > IMG_MIN_WIDTH:
        ratio = IMG_MIN_WIDTH / width
        width = int(ratio * width)
        height = int(ratio * height)
    return cv2.resize(input_img, (width, height), interpolation=cv2.INTER_LINEAR)

