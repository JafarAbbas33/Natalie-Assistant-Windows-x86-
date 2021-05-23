import sys
import tkinter as tk
import os, time

import mss, textwrap
from PIL import ImageTk
from PIL import Image
from PIL import ImageFont, ImageDraw



root = tk.Tk()

icon = ImageTk.PhotoImage(master=root, file='utils/favicon.ico')
root.wm_iconphoto(True, icon)

root.title("Assistant")



root.attributes("-fullscreen", True)

def killing_func():
    root.destroy()
    print("App destroyed")
    destroyed = True

mic = Image.open("utils/Google_mic.png")
mic = mic.resize((58, 80), Image.ANTIALIAS)
w,h=mic.size
monitor = {'left': 0, 'top': 0, 'width': root.winfo_screenwidth(), 'height': root.winfo_screenheight()}
font = ImageFont.truetype("utils/Montserrat-Medium.ttf", size=70)
spacing_bw_text = 10
o_w = 0

class TextUtil:
    pass
 
def update_text(text):
    canvas.itemconfigure(text_label, text=text)
    return

    global o_w                
    im = TextUtil.im
    current_h = TextUtil.current_h
    para=textwrap.wrap(text,width=27)
    draw = ImageDraw.Draw(im)
    width, height = im.siz
    
    tw,th=draw.textsize(text, font=font)
    n_w = (width-tw)/2
    o_w = n_w - o_w
    canvas.move(text_label, o_w, 0)
    return
    
    for line in para:
        tw,th=draw.textsize(line, font=font)
        draw.text(((width-tw)/2, current_h), line, font=font)
        current_h+=th + spacing_bw_text
        
    oo = ImageTk.PhotoImage(im)
    image_label.image = oo
    image_label.config(image=oo)


def bring_to_front():
    update_text("")
    global image, mic, w, h, im, oo, monitor
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        #sct_img = sct.shot(output = "xoxo" + x + ".jpg")
        im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
    im = Image.blend(im,image,0.65)
    width, height = image.size
    past_w = round((width-w)/2)
    past_h = round((height-h)/2)
    im.paste(mic, (past_w, past_h), mic)
    oo = ImageTk.PhotoImage(im)
    root.state('normal')
    root.focus_force()
    root.focus_force()
    root.focus_force()
    
    canvas.itemconfigure(image_label, image=oo)
    
    TextUtil.im = im
    TextUtil.current_h = past_h + 250

        

destroyed = False
ww = root.winfo_screenwidth()
hh = root.winfo_screenheight()
image = Image.new("RGB", (ww, hh), "black")
oo = ImageTk.PhotoImage(image)


canvas = tk.Canvas(root, width=ww, height=hh)
canvas.pack()
image_label = canvas.create_image(monitor['width'], 0, image=oo, anchor="ne")
text_label = canvas.create_text(monitor['width']/2, hh/2+200, text="", font=("Ubuntu", 26), fill="white")

bring_to_front()
update_text("Initializing")

