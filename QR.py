from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()
root.title('QR CODE GENERATOR')


def qrcode():
    name = display.get()
    link = display1.get()
    file_name = name + '.png'
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 480, window=image_label)

    if link:
        return
    quit()


canvas = Canvas(root, width=400, height=650, background='cyan')
canvas.pack()

app_label = Label(root, text='QR CODE GENERATOR', font=('Arial', 25))
canvas.create_window(200, 50, window=app_label)
name_label = Label(root, text='Link Name', font="arial", fg='red')
canvas.create_window(200, 150, window=name_label)
display = Entry(root)
canvas.create_window(200, 190, window=display)
link_label = Label(root, text="Link", font='Arial', fg='red')
canvas.create_window(200, 240, window=link_label)
display1 = Entry(root)
canvas.create_window(200, 280, window=display1)
button = Button(root, text='Generate', command=qrcode)
canvas.create_window(200, 320, window=button)

root.mainloop()
