import cv2
import numpy as np
from lib import resize_img


if __name__ == "__main__":
    image = cv2.imread("imgs/Capture4.PNG")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    resized_image = resize_img(gray)

    # for every row, compare ith & ith+1 pixels
    diff = resized_image[:, :-1] == resized_image[:, 1:]

    changes = np.r_[True, resized_image[50][1:] != resized_image[50][:-1], True]


    starts = np.flatnonzero(changes[:-1])
    ends = np.flatnonzero(changes[1:])

    lengths = ends - starts

    print(starts)   # [0 1 2 5 6]
    print(lengths)  # [1 1 3 1 1]

    print(changes)

    print(resized_image[50])
    # print(diff[50])

    # find the length of subarrays that contains line: diff[i:i+n] = [0, 0,.., 0] where n > predefined threshold
    # approach 1: loop over the 'diff' array and check whether i * i+1 == 0, store the start index and continue to
    # loop until i != 0. If the length traveled > threshold then store the coordinate & len else continue the loop
    # this is not a bad approach, we just dont utilize the maximum power of np.array
    # approach 2: apply matrix operation over the entire 'diff' array to get the location & length of the subarrays
    # 

