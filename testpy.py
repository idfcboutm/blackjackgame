import pyfirmate
from pyfirmata import util
import Tkinter
from time import sleep


def press():
    it = util.Iterator(board)
    it.start()
    while True:
        if flag.get():
            analoglabel.config(text=str(pin.read()))
            analoglabel.update_idletasks()
            root.update()
        else:
            break
        board.exit()
        root.destroy()


def exit_command():
    flag.set(False)


port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)
sleep(5)
pin = board.get_pin('a:0:i')

root = Tkinter.Tk()
root.title("Analog read by hamzawi")
root.minsize(300, 50)

startbutton = Tkinter.Button(root,
                             text="START",
                             command=press)
startbutton.grid(column=1, row=2)

exitbutton = Tkinter.Button(root,
                            text="EXIT",
                            command=exit_command)
exitbutton.grid(column=2, row=2)

label = Tkinter.Label(root,
                      text="The value is: ")
label.grid(column=1, row=1)

analoglabel = Tkinter.Label(root, text=" ")
analoglabel.grid(column=2, row=1)

flag = Tkinter.BooleanVar()
flag.set(True)

root.mainloop()
