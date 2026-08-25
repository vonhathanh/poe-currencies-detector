import cv2
import time
import numpy as np
import mss


def main():
    with mss.MSS() as sct:
        # The monitor or screen part to capture
        monitor = sct.monitors[1]  # or a region
        for i in range(5):
            start = time.time()
            img = np.array(sct.grab(monitor))
            end = time.time()
            print(f"Time taken to read image: {end - start}")

if __name__ == "__main__":
    main()