Main processing flow:

1. Read image

2. Detect text boxes by paddleocr

3. Filter invalid text boxes by width & height

4. Run text recognition by paddleocr

5. Check if text match the predefined dictionary -> collect coordinates then send click events
