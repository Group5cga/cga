from tkinter import *

coords = {"x1":0,"y1":0,"x2":0,"y2":0}
lines = []

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
        btnline=Button(main, text="LINE", fg='black', width=8, command=self.line)
        btnline.place(x=10, y=150)
        btncir=Button(main, text="CIRCLE", fg='black', width=8, command=self.circle)
        btncir.place(x=10, y=200)
        btnfill=Button(main, text="FILL", fg='black', width=8)
        btnfill.place(x=10, y=250)
        btnclear=Button(main, text="CLEAR", fg='black', width=8)
        btnclear.place(x=10, y=300)
        self.canvas = Canvas(self.main, bg='white', bd=5, relief=RIDGE, height=600, width=700)
        self.canvas.place(x=80, y=0)

    def line(self):
        self.canvas.bind("<ButtonPress-1>", self.line_click)
        self.canvas.bind("<B1-Motion>", self.drag) 
    def line_click(self, e):
        coords["x1"] = e.x
        coords["y1"] = e.y
        lines.append(self.canvas.create_line(coords["x1"],coords["y1"],coords["x1"],coords["y1"]))
    def circle(self):
        self.canvas.bind("<ButtonPress-1>", self.circle_click)
        self.canvas.bind("<B1-Motion>", self.drag) 
    def circle_click(self, e):
        coords["x1"] = e.x
        coords["y1"] = e.y
        lines.append(self.canvas.create_oval(coords["x1"],coords["y1"],coords["x1"],coords["y1"]))    
    def drag(self, e):
        coords["x2"] = e.x
        coords["y2"] = e.y
        self.canvas.coords(lines[-1], coords["x1"],coords["y1"],coords["x2"],coords["y2"])
    def clear(self):
        self.canvas.delete("all")
        self.rect = None
        self.tick = 0
    
main = Tk()
p = Filling(main)
main.mainloop()