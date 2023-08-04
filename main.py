from tkinter import *
# from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter

window = Tk()
window.title("Create Watermark")
window.minsize(width=1000, height=800)

watermark = Image.open('./abstract.jpg')
bg = ImageTk.PhotoImage(watermark)
background = Label(window, image=bg, width=1000, height=800)
background.place(x=0, y=0)

label = Label(text="Upload Image file to Watermark", font=("Times", 24, "bold"))
label.pack(pady=20)

button2 = Button()
button3 = Button()
photo = Button()
download_button = Button()


def download(image, filename):
    image.save(f'{filename}watermark.jpg')


def add_logo(image, filename):
    global download_button

    if download_button:
        download_button.destroy()
    logo = Image.open('./logo.png')
    # logo = logo.filter(ImageFilter.BLUR)
    size = (500, 400)
    logo.thumbnail(size)
    image.paste(logo, (100, 100))
    image.show()
    download_button = Button(text='Download Now', font=('Times', 20, 'bold'), command=lambda: download(image, filename))
    download_button.pack()


def add_text(image, filename):
    global download_button

    if download_button:
        download_button.destroy()

    text = 'Vijay Kumar M R'
    width, height = image.width, image.height
    draw = ImageDraw.Draw(image)

    # Method to fit the font according to the image
    x, y = int(width / 2), int(height / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x
    font = ImageFont.truetype('arial.ttf', font_size//6)
    margin_from_top = 10

    # black Color Text as Watermark
    draw.text((margin_from_top, margin_from_top), text=text, fill=(0, 0, 0), font=font)
    image.show()

    download_button = Button(text='Download Now', font=('Times', 20, 'bold'), command=lambda: download(image, filename))
    download_button.pack()


def upload_file():
    global button2
    global button3
    global photo
    global img
    if button2:
        button2.destroy()
        button3.destroy()
        photo.destroy()
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
    filename = askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img_resized = img.resize((300, 400))
    img = ImageTk.PhotoImage(img_resized)
    photo = Button(image=img)
    photo.pack(pady=20)
    button2 = Button(text='Add Your Logo as WaterMark', font=("Times", 20, "bold"), command=lambda: add_logo(Image.open(filename), filename))
    button2.pack(pady=20)
    button3 = Button(text='Add Text as WaterMark', font=('Times', 20, 'bold'), command=lambda: add_text(Image.open(filename), filename))
    button3.pack(pady=20)


button1 = Button(text='Upload File', width=20, command=upload_file)
button1.pack()

window.mainloop()
