Main processing flow:
 Read image
 detect rectangles
    detect horizontal line first
    detect vertical line at the start of the line
    if at the end of the vertical line there is another vertical line -
 dilute text in the image so we dont have to deal with text first, only rectangle detection (optional)
 check width/height validity
 detect text inside the rect
 if text is in the currencies list -> output coordinate

List of possible object types:
- Textbox with/without icon
- Textbox with/without border
- Textbox with/without number of currencies