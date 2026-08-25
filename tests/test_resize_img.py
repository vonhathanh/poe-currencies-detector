import cv2
from lib import resize_img


if __name__ == "__main__":
    image = cv2.imread("imgs/Capture4.PNG")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    print('original img shape: ', gray.shape)

    resized_image = resize_img(gray)

    print('resized img shape: ', resized_image.shape)