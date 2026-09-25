import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

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

image = cv2.imread("data/imgs/Capture7.PNG")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

notebook_imshow(image)