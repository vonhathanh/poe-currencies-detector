import time
import numpy as np
import mss
import pyautogui
from pynput import keyboard
from rapidocr import RapidOCR
from lib import *
import flet as ft

engine = RapidOCR()
currencies = load_currencies_set()
screen_capture = mss.MSS()
monitor = screen_capture.monitors[1]  # or a region

def on_press(key):
    if key == keyboard.Key.space:
        pickup_currencies()

def pickup_currencies():
    start = time.time()
    screenshot = screen_capture.grab(monitor)
    img = np.array(screenshot)
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


def main(page: ft.Page):

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    page.title = "PoE Detector"
    page.window_width = 400
    page.window_height = 300
    page.padding = 30

    currencies = ft.Checkbox(label="Currencies")
    base_items = ft.Checkbox(label="Base Items")
    maps = ft.Checkbox(label="Maps")
    fragments = ft.Checkbox(label="Fragments")

    def on_change(e):
        selected = [
            checkbox.label
            for checkbox in [currencies, base_items, maps, fragments]
            if checkbox.value
        ]

        print("Selected:", selected)

    for checkbox in [currencies, base_items, maps, fragments]:
        checkbox.on_change = on_change

    page.add(
        ft.Column(
            [
                ft.Text(
                    "PoE Currency Detector",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Divider(),
                currencies,
                base_items,
                maps,
                fragments,
            ],
            spacing=10,
        )
    )

    def on_window_event(e):
        if e.type == ft.WindowEventType.CLOSE:
            print("App is exiting!")
            listener.stop()
            listener.join()
            print('App exited')

    page.window.on_event = on_window_event

ft.run(main)