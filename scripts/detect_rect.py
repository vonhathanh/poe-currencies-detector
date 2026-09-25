import os
import sys 
import cv2
import time
import glob

sys.path.append(os.path.abspath('..'))

from lib import *

currencies = load_currencies_set()

img_filenames = glob.glob('./data/imgs/*.PNG')

for filename in img_filenames:

    print('processing ', filename)

    img = cv2.imread(filename)

    coords = find_currency_coords(img, currencies)
    print(f"{coords=}")
