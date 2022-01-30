from argparse import FileType
from gettext import install
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

app = tk.Tk()

canvas = tk.Canvas(app, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


# logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


# instructions
instruction = tk.Label(
    app, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instruction.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=app, mode="rb", title="Choose a file", filetype=[
                       {"Pdf file", "*.pdf"}])
    if file:
        print("file was sucessfully loaded")


# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(app, textvariable=browse_text, command=lambda: open_file(),
                       font="Ralway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(app, width=600, height=250)
canvas.grid(columnspan=3)

app.mainloop()
