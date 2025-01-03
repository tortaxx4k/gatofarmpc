from tkinter import *

app = Tk()
app.title("GatoFarm")
app.geometry("500x500")
app.config(bg="gray")
app.iconbitmap("logo.ico")
app.resizable(False, False)

gatoparclick = 1
gato = 0 

# actions
def addclick(): 
    global gato  
    gato += gatoparclick
    clickprinnt.config(text=gato)
def upgradeclick():
    global gatoparclick
    gatoparclick *= 2
    upgradelevelprint.config(text=str(gatoparclick))

clickbutton = Button(app, text="click", command=addclick, height=5, width=10, bg="darkgray")
clickbutton.place(x=220, y=200)
clickprinnt = Label(app, text=gato, bg="gray")
clickprinnt.place(x=250, y=300)



updradebutton = Button(app, text='améliorer le nombre de gatos par click', command=upgradeclick, bg="darkgray")
updradebutton.place(x=145, y=400)
upgradelevelprint = Label(app, text=str(gatoparclick), bg="gray")
upgradelevelprint.place(x=250, y=430)

app.mainloop()
