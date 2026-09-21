import time
import numpy as np
import mss
import pyautogui
from rapidocr import RapidOCR
from lib import *

engine = RapidOCR()


def main():
    currencies = load_currencies_set()
    with mss.MSS() as sct:
        # The monitor or screen part to capture
        monitor = sct.monitors[1]  # or a region
        start = time.time()
        img = np.array(sct.grab(monitor))
        end = time.time()
        print(f"Time taken to read image: {end - start}")
        result = engine(img)
        txts = result.txts
        # enumerate over all bounding boxes
        for i, box in enumerate(result.boxes):
            top_left, top_right, _, bottom_left = box
            width = int(top_right[0] - top_left[0])
            height = int(bottom_left[1] - top_left[1])
            # check if the box has valid width & height
            if MAXIMUM_CURRENCY_BOX_WIDTH > width > MINIMUM_CURRENCY_BOX_WIDTH and MAXIMUM_CURRENCY_BOX_HEIGHT > height > MINIMUM_CURRENCY_BOX_HEIGHT:
                text = txts[i].lower()
                # check text has prefix like: 1x, 2x,... nx + currency name
                match = CURRENCY_PATTERN.match(text)
                if match:
                    # remove the prefix to get the original currency name only
                    end_pos = match.end()
                    text = text[end_pos:]    
                if text not in currencies:
                    continue
                x = int(top_left[0]) + width // 2
                y = int(top_left[1]) + height // 2
                pyautogui.click(x, y)
                print(f"clicked at {x=}, {y=}")        


if __name__ == "__main__":
    main()