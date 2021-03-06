from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image as gambar

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
        self.canvas = Canvas(self.main, bg='white', bd=5, relief=RIDGE, height=600, width=700)
        self.canvas.place(x=80, y=0)
        
    def select(self):
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
        lines.append(self.canvas.create_line(coords["x1"],coords["y1"],coords["x1"],coords["y1"]))
        
    def circle(self):
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
        lines.append(self.canvas.create_oval(coords["x1"],coords["y1"],coords["x1"],coords["y1"]))    
        
    def drag(self, e):
        coords["x2"] = e.x
        coords["y2"] = e.y
        self.canvas.coords(lines[-1], coords["x1"],coords["y1"],coords["x2"],coords["y2"])
        
    def clear(self):
        self.canvas.delete("all")
        self.rect = None
        self.tick = 0
        
    def color_choice(self):
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
        self.btnfill.configure(relief=SUNKEN)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.ffillrec(x, y))
        self.canvas.bind("<B1-Motion>", self.nothing)
    
    def nothing(self, event):
        pass
    def carixy(self,event):
        global x, y, item
        x = event.x
        y = event.y
        self.item = self.canvas.find_closest(event.x, event.y)
    def ffillrec(self, x, y):
        #self.canvas.itemconfig(self.item, fill=self.color)
        current_color = self.canvas.itemcget(item, 'fill')
        if(x < 0 or x >= self.canvas.winfo_screenwidth() or y < 0 or y >= self.canvas.winfo_screenheight()):
            return
        if(x < 0 or x >= self.canvas.winfo_screenwidth() or y < 0 or y >= self.canvas.winfo_screenheight())!=current_color:
            return
        if(x < 0 or x >= self.canvas.winfo_screenwidth() or y < 0 or y >= self.canvas.winfo_screenheight())== current_color:
            return
        gambar.putpixel((x,y), self.color)
        print(x, y) #ngetes isinya apa, tapi functionnya aja error gimana mau ngeprint wkwkwk
        ffillrec(self, x+1, y)
        ffillrec(self, x-1, y)
        ffillrec(self, x, y+1)
        ffillrec(self, x, y-1)
        #item = self.canvas.find_closest(event.x, event.y)
        #x = event.x
        #y = event.y
        #self.canvas.itemconfig(item, fill=self.color)
        #current_color = self.canvas.itemcget(item, 'fill')
        #if (x > 0):
            #if (self.canvas.itemcget((event.x-1, event.y), 'fill')) == current_color:
                #self.ffillrec()
        #if (y > 0):
            #if (self.canvas.itemcget((event.x, event.y-1), 'fill')) == current_color : 
                #self.ffillrec()
        #if (x < self.canvas.winfo_screenwidth()-1):
            #if (self.canvas.itemcget((event.x+1, event.y), 'fill')) == current_color : 
                #self.ffillrec()
        #if (y < self.canvas.winfo_screenheight()-1):
            #if (self.canvas.itemcget((event.x, event.y+1), 'fill')) == current_color : 
                #self.ffillrec()
                
    def bound_fill_click(self):
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=SUNKEN)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.boundfill)
        self.canvas.bind("<B1-Motion>", self.nothing)
        
    def boundfill(self, event):#Blom jalan
        item = self.canvas.find_closest(event.x, event.y)
        x = event.x
        y = event.y
        current_color = "black"
        if (self.canvas.itemcget((event.x-1, event.y), 'fill')) != (current_color and self.color):
                self.canvas.itemconfig((event.x-1, event.y), fill = self.color)
                
        if (self.canvas.itemcget((event.x+1, event.y), 'fill')) != (current_color and self.color) : 
                self.canvas.itemconfig((event.x+1, event.y), fill = self.color)
                
        if (self.canvas.itemcget((event.x, event.y-1), 'fill')) != (current_color and self.color) : 
                self.canvas.itemconfig((event.x, event.y-1), fill = self.color)
                
        if (self.canvas.itemcget((event.x, event.y+1), 'fill')) != (current_color and self.color) : 
                self.canvas.itemconfig((event.x, event.y+1), fill = self.color)
                
    def eightway_fill_click(self):
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=SUNKEN)
        self.canvas.bind("<Button-1>", self.eightwayfillrec)
        self.canvas.bind("<B1-Motion>", self.nothing)
        
    def eightwayfillrec(self, event, x, y, DEFAULT_COLOR):
        if (self.canvas.itemcget((event.x, event.y))) != boundary_color) and (self.canvas.itemcget((event.x, event.y))) != self.color):
            gambar.putpixel((x,y), self.color)
            eightwayfill(x + 1, y, boundary_color); 
            eightwayfill(x, y + 1, boundary_color); 
            eightwayfill(x - 1, y, boundary_color); 
            eightwayfill(x, y - 1, boundary_color); 
            eightwayfill(x - 1, y - 1, boundary_color); 
            eightwayfill(x - 1, y + 1, boundary_color); 
            eightwayfill(x + 1, y - 1, boundary_color); 
            eightwayfill(x + 1, y + 1, boundary_color); 
        
        
main = Tk()
p = Filling(main)
main.mainloop()
