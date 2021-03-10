from tkinter import *
from tkinter.colorchooser import askcolor
import sys
sys.setrecursionlimit(2450)

coords = {"x1":0,"y1":0,"x2":0,"y2":0}
lines = []
DEFAULT_COLOR = 'black'
x = 0
y = 0
stack = []

class Filling():
    def __init__(self, main):
        self.main = main
        self.main.title('Filling')
        self.main.geometry("800x620")
        self.color = DEFAULT_COLOR
        menubar = Menu(main)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Clear", command=self.clear)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=main.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        main.config(menu=menubar)

        self.btnsel=Button(main, text="SELECT", fg='black', width=8, command=self.select)
        self.btnsel.place(x=10, y=100)
        self.btnline=Button(main, text="LINE", fg='black', width=8, command=self.line)
        self.btnline.place(x=10, y=150)
        self.btncir=Button(main, text="CIRCLE", fg='black', width=8, command=self.circle)
        self.btncir.place(x=10, y=200)
        self.btnfill=Button(main, text="FILL", fg='black', width=8, command=self.clickfillrec)
        self.btnfill.place(x=10, y=250)
        self.btnclear=Button(main, text="COLOR", fg='black', width=8, command=self.color_choice)
        self.btnclear.place(x=10, y=300)
        self.btnboundfill=Button(main, text="Bound Fill", fg='black', width=8, command=self.bound_fill_click)
        self.btnboundfill.place(x=10, y=350)
        self.btn8wayfill=Button(main, text="8 Fill", fg='black', width=8, command=self.eightway_fill_click)
        self.btn8wayfill.place(x=10, y=400)
        self.btnscanfillflo=Button(main, text="Scanfill Flood", fg='black', width=8, command=self.scan_fillflo_click)
        self.btnscanfillflo.place(x=10, y=450)
        self.canvas = Canvas(self.main, bg='white', bd=5, relief=RIDGE, height=600, width=700)
        self.canvas.place(x=80, y=0)
        self.canvas.create_rectangle(0, 0, 750, 600, fill='white', outline='white')

    def locate_xy(self, event):
        global current_x, current_y, close, current_color
        
        current_x, current_y = event.x, event.y
        current_x = x
        current_y = y

    def select(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=SUNKEN)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.unbind("<Button 1>")
        self.canvas.bind("<B1-Motion>") 
        
    def line(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=SUNKEN)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<ButtonPress-1>", self.line_click)
        self.canvas.bind("<B1-Motion>", self.drag) 
        
    def line_click(self, e):
        coords["x1"] = e.x
        coords["y1"] = e.y
        lines.append(self.canvas.create_line(coords["x1"],coords["y1"],coords["x1"],coords["y1"],fill=self.color))
        
    def circle(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=SUNKEN)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<ButtonPress-1>", self.circle_click)
        self.canvas.bind("<B1-Motion>", self.drag) 
        
    def circle_click(self, e):
        coords["x1"] = e.x
        coords["y1"] = e.y
        lines.append(self.canvas.create_oval(coords["x1"],coords["y1"],coords["x1"],coords["y1"],outline=self.color))    
        
    def drag(self, e):
        coords["x2"] = e.x
        coords["y2"] = e.y
        self.canvas.coords(lines[-1], coords["x1"],coords["y1"],coords["x2"],coords["y2"])
        
    def clear(self):
        self.canvas.delete("all")
        self.rect = None
        self.tick = 0
        
    def color_choice(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=SUNKEN)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.DEFAULT_COLOR = self.color
        self.color = askcolor(color=self.color)[1]

    def clickfillrec(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=SUNKEN)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.position)
        self.canvas.bind("<B1-Motion>", self.nothing)

    def position(self,event):
        x = event.x
        y = event.y
        #item = self.canvas.find_closest(event.x, event.y)
        self.ffillrec(x,y)

    def nothing(self, event):
        pass
        
    def ffillrec(self, x, y):
        item = self.canvas.find_closest(x, y)
        item2 = self.canvas.find_closest(x-1, y)
        item3 = self.canvas.find_closest(x, y-1)
        item4 = self.canvas.find_closest(x+1, y)
        item5 = self.canvas.find_closest(x, y+1)
        current_color = self.canvas.itemcget(item, "fill")
        self.canvas.create_rectangle(x, y, x, y, outline=self.color)
        #print(x)
        #print(y)
        #hihi = self.canvas.itemcget(item2, 'fill')
        #print(hihi)
        #print(self.color)
        #print(current_color)
        if (self.canvas.itemcget(item2, 'fill')) == current_color:
            if (x > 0):
                self.ffillrec((x-1), y)
        if (self.canvas.itemcget(item3, 'fill')) == current_color:
            if (y > 0): 
                self.ffillrec(x, (y-1))
        if (self.canvas.itemcget(item4, 'fill')) == current_color:
            if (x < 800): 
                self.ffillrec((x+1), y)
        if (self.canvas.itemcget(item5, 'fill')) == current_color:
            if (y < 620):
                self.ffillrec(x, (y+1))
        #item = self.canvas.find_closest(event.x, event.y)
        #x = event.x
        #y = event.y
        #self.canvas.itemconfig(item, fill=self.color)
        #current_color = self.canvas.itemcget(item, 'fill')
        #if(x < 0 or x >= self.canvas.winfo_screenwidth() or y < 0 or y >= self.canvas.winfo_screenheight()):
        #    return
        #if(x < 0 or x >= self.canvas.winfo_screenwidth() or y < 0 or y >= self.canvas.winfo_screenheight())!=current_color:
        #    return
        #if(x < 0 or x >= self.canvas.winfo_screenwidth() or y < 0 or y >= self.canvas.winfo_screenheight())== current_color:
        #    return
        
                
    def bound_fill_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=SUNKEN)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.position2)
        self.canvas.bind("<B1-Motion>", self.nothing)

    def position2(self,event):
        x = event.x
        y = event.y
        #item = self.canvas.find_closest(event.x, event.y)
        self.boundfill(x,y)
        
    def boundfill(self, x, y):#Blom jalan
        item2 = self.canvas.find_closest(x-1, y)
        item3 = self.canvas.find_closest(x, y-1)
        item4 = self.canvas.find_closest(x+1, y)
        item5 = self.canvas.find_closest(x, y+1)
        bordercol = "black"
        self.canvas.create_rectangle(x, y, x, y, outline=self.color)
        hihihi = self.canvas.itemcget(item4, 'fill')
        print(hihihi)
        if (self.canvas.itemcget(item2, 'fill')) != (bordercol):
            if (self.canvas.itemcget(item2, 'fill')) != (self.color):
                if (x > 0): 
                    self.boundfill((x-1), y)
                #self.canvas.itemconfig((event.x-1, event.y), fill = self.color)
                
        if (self.canvas.itemcget(item4, 'fill')) != (bordercol) : 
            if (self.canvas.itemcget(item4, 'fill')) != (self.color):
                if (y > 0): 
                    self.boundfill((x+1), y)
                #self.canvas.itemconfig((event.x+1, event.y), fill = self.color)
                
        if (self.canvas.itemcget(item3, 'fill')) != (bordercol) :
            if (self.canvas.itemcget(item3, 'fill')) != (self.color):
                if (x < 800): 
                    self.boundfill(x, (y-1))
                #self.canvas.itemconfig((event.x, event.y-1), fill = self.color)
                
        if (self.canvas.itemcget(item5, 'fill')) != (bordercol) :
            if (self.canvas.itemcget(item5, 'fill')) != (self.color):
                if (y < 620): 
                    self.boundfill(x, (y+1))
                #self.canvas.itemconfig((event.x, event.y+1), fill = self.color)
                
    def eightway_fill_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=SUNKEN)
        self.canvas.bind("<Button-1>", self.eightwayfill)
        self.canvas.bind("<B1-Motion>", self.nothing)
    
    def scan_fillflo_click(self):
        self.btnscanfillflo.configure(relief=SUNKEN)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.scanfillflo)
        self.canvas.bind("<B1-Motion>", self.nothing)
main = Tk()
p = Filling(main)
main.mainloop()
