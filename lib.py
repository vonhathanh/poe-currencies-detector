import cv2
import numpy as np
import matplotlib.pyplot as plt

IMG_MIN_WIDTH = 1000.0
IMG_MIN_HEIGHT = 1000.0

def resize_img(input_img: np.ndarray):
    if len(input_img.shape) == 2:
        height, width = input_img.shape
    elif len(input_img.shape) == 3:
        height, width, _ = input_img.shape
    else:
        raise ValueError(f'expect input image to has shape = 2 or 3, got: {len(input_img.shape)}')

    if width > IMG_MIN_WIDTH:
        ratio = IMG_MIN_WIDTH / width
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
    else: 
        plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()
