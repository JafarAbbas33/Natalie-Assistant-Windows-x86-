if __name__ == "__main__":
    print("Bro not main")
    sys.exit()

import tkinter as tk
import os, sys, threading, time

import mss, textwrap
from PIL import ImageTk
from PIL import Image
from PIL import ImageFont, ImageDraw




root = tk.Tk()

##image = Image.open('favicon.ico')
##photo = ImageTk.PhotoImage(image)

icon = ImageTk.PhotoImage(master=root, file='favicon.ico')
root.wm_iconphoto(True, icon)

##root.wm_iconbitmap('favicon.ico')

root.title("Assistant")
root.state('iconic')

##root.attributes('-fullscreen', True)
##root.state('iconic')
##root.state('withdrawn')
##root.resizable(0,0)
##root.state('normal')
##pad=0
####root.attributes('-type', 'dock')
##
##
####root.attributes('-zoomed', True)
##try:                                   # Automatic zoom if possible
##    root.wm_state("zoomed")
##    print("Using automatic zoom")
##except tk.TclError:  
##    root.geometry("{0}x{1}+0+0".format(
##                root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))





##root.overrideredirect(True)
##root.overrideredirect(False)

root.attributes("-fullscreen", True)
##root.wm_attributes("-topmost", 1)
##root.focus_set()

def killing_func():
    root.destroy()
    print("App destroyed")
    destroyed = True

##root.bind('<Escape>', d)

##root.wait_visibility(root)
##root.attributes('-type', 'normal')
##root.wm_attributes("-alpha", 0.5)

##def ss():
mic = Image.open("1200px-Google_mic.svg.png")
mic = mic.resize((58, 80), Image.ANTIALIAS)
w,h=mic.size
monitor = {'left': 0, 'top': 0, 'width': 1366, 'height': 768}
##monitor = {'left': 20, 'top': 20, 'width': 1000, 'height': 500}
font = ImageFont.truetype("Montserrat-Medium.ttf", size=70)
##font = ImageFont.load_default()
spacing_bw_text = 10

class TextUtil:
    pass
 
##def update_text(text):
##    im = TextUtil.im.copy()
##    current_h = TextUtil.current_h
##    para=textwrap.wrap(text,width=27)
##    draw = ImageDraw.Draw(im)
##    width, height = im.size
##    
##    for line in para:
##        tw,th=draw.textsize(line, font=font)
##        draw.text(((width-tw)/2, current_h), line, font=font)
##        current_h+=th + spacing_bw_text
##        
##    oo = ImageTk.PhotoImage(im)
##    image_label.image = oo
##    image_label.config(image=oo)


def bring_to_front():
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
    image_label.config(image=oo)
    TextUtil.im = im
    TextUtil.current_h = past_h + 250


def s():
    global btf
    if btf:
        pass
    
    print("Inner")
    bring_to_front()
    btf = False
        

destroyed = False
##root.after(50, s)
##root.after(1000, lambda: root.state('normal'))
##root.after(3000, root.destroy)
##threading.Thread(target=s, daemon=True).start()
ww = root.winfo_screenwidth()
hh = root.winfo_screenheight()
image = Image.new("RGB", (ww, hh), "black")
oo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=oo)
image_label.place(x=0, y=0, relwidth=1, relheight=1)
text_label = tk.Label(root, text="")
text_label.place(anchor="center", relx=0.5, rely=0.75)
##image_label.pack()
##tk.Label(root, image=ph).place(anchor="center", relx=0.5, rely=1)
##root.geometry('200x200')
##root.focus_force()
