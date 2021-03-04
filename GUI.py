from tkinter import *


class Filling():
    def __init__(self, main):
        self.main = main
        self.main.title('Filling')
        self.main.geometry("800x620")
        menubar = Menu(main)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Clear", command=self.clear)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=main.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        main.config(menu=menubar)

        btnsel=Button(main, text="SELECT", fg='black', width=8)
        btnsel.place(x=10, y=100)
        btnline=Button(main, text="LINE", fg='black', width=8)
        btnline.place(x=10, y=150)
        btncir=Button(main, text="CIRCLE", fg='black', width=8)
        btncir.place(x=10, y=200)
        btnfill=Button(main, text="FILL", fg='black', width=8)
        btnfill.place(x=10, y=250)
        btnclear=Button(main, text="CLEAR", fg='black', width=8)
        btnclear.place(x=10, y=300)
        self.canvas = Canvas(self.main, bg='white', bd=5, relief=RIDGE, height=600, width=700)
        self.canvas.place(x=80, y=0)
    
    def clear(self):
        self.canvas.delete("all")
        self.rect = None
        self.tick = 0
    

main = Tk()
p = Filling(main)
main.mainloop()