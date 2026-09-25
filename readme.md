Main processing flow:
 Read image
 detect text boxes by paddleocr
 filter invalid text boxes by width & height
 run text recognition by paddleocr
 check if text match the predefined dictionary -> collect coordinates then send click events