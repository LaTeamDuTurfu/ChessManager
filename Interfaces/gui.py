
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../Interfaces/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x768")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    375.0,
    768.0,
    fill="#415A77",
    outline="")

canvas.create_rectangle(
    375.0,
    0.0,
    1024.0,
    768.0,
    fill="#778DA9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=435.0,
    y=673.0,
    width=220.0,
    height=58.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=676.923095703125,
    y=673.0,
    width=218.076904296875,
    height=58.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=934.0,
    y=673.0,
    width=54.0,
    height=58.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=36.0,
    y=673.0,
    width=303.0,
    height=58.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    187.0,
    334.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    659.0,
    44.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    682.0,
    149.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    664.0,
    239.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    604.0,
    329.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    579.0,
    419.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    653.0,
    509.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    640.0,
    599.0,
    image=image_image_8
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    842.0,
    44.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=754.0,
    y=26.0,
    width=176.0,
    height=34.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    842.0,
    83.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=754.0,
    y=65.0,
    width=176.0,
    height=34.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    965.5,
    149.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=934.0,
    y=131.0,
    width=63.0,
    height=34.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    785.5,
    149.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=754.0,
    y=131.0,
    width=63.0,
    height=34.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    875.5,
    149.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=844.0,
    y=131.0,
    width=63.0,
    height=34.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    875.5,
    329.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=754.0,
    y=311.0,
    width=243.0,
    height=34.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    819.0,
    419.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=754.0,
    y=401.0,
    width=130.0,
    height=34.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    794.0,
    509.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=754.0,
    y=491.0,
    width=80.0,
    height=34.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    875.5,
    599.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=754.0,
    y=581.0,
    width=243.0,
    height=34.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    814.0,
    239.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=754.0,
    y=221.0,
    width=120.0,
    height=34.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    937.0,
    239.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#415A77",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=877.0,
    y=221.0,
    width=120.0,
    height=34.0
)

canvas.create_rectangle(
    818.0,
    149.0,
    840.0,
    152.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    908.0,
    149.0,
    930.0,
    152.0,
    fill="#FFFFFF",
    outline="")

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    785.0,
    180.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    875.0,
    180.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    965.0,
    180.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    941.0,
    419.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    921.0,
    518.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    814.0,
    270.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    968.0,
    44.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    937.0,
    270.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    969.0,
    83.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    187.0,
    319.0,
    image=image_image_18
)
window.resizable(False, False)
window.mainloop()
