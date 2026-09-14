import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib import resize_img

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

image = cv2.imread("imgs/Capture4.PNG")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image, scale_ratio = resize_img(gray[0:194, 0:319])
resized_color_img, _ = resize_img(image[0:194, 0:319, :])
notebook_imshow(image)