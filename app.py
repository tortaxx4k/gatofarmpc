from tkinter import *
import threading
from PIL import Image, ImageTk
import time

app = Tk()
app.title("GatoFarm")
app.geometry("500x500")
app.config(bg="gray")
app.iconbitmap("logo.ico")
app.resizable(False, False)
app.protocol("WM_DELETE_WINDOW", app.destroy)

gatoparclick = 1
gato = 0 
running = False
loop_thread = None

# actions
def addclick(): 
    global gato  
    gato += gatoparclick
    clickprinnt.config(text=gato)

def upgradeclick():
    global gatoparclick
    gatoparclick *= 2
    upgradelevelprint.config(text=str(gatoparclick))

def loop_increment():
    global gato, running
    while running:
        gato += gatoparclick
        clickprinnt.config(text=gato)
        app.update()
        time.sleep(1)

def toggle_loop():
    global running, loop_thread
    if running:
        running = False
        loop_button.config(text="autoclick", bg="red")
    else:
        running = True
        loop_thread = threading.Thread(target=loop_increment)
        loop_thread.start()
        loop_button.config(text="autoclick", bg="green")


cookie_image = Image.open("cookie.png")
cookie_image = ImageTk.PhotoImage(cookie_image)

clickbutton = Button(app, image=cookie_image, command=addclick, height=100, width=100)
clickbutton.place(x=200, y=200)
clickprinnt = Label(app, text=gato, bg="gray")
clickprinnt.place(x=250, y=310)

updradebutton = Button(app, text='améliorer le cookie', command=upgradeclick, bg="darkgray")
updradebutton.place(x=200, y=400)
upgradelevelprint = Label(app, text=str(gatoparclick), bg="gray")
upgradelevelprint.place(x=250, y=430)

loop_button = Button(app, text="autoclick", command=toggle_loop, height=5, width=14, bg="red")
loop_button.place(x=200, y=100)


clickbutton.image = cookie_image

app.mainloop()
