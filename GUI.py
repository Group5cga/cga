from tkinter import *


class Filling():
    def __init__(self, main):
        self.main = main
        self.main.title('Filling')
        self.main.geometry("800x620")

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
        canvas = Canvas(self.main, bg='white', bd=5, relief=RIDGE, height=600, width=700)
        canvas.place(x=80, y=0)

main = Tk()
p = Filling(main)
main.mainloop()