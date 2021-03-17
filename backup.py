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
        self.btnsel.place(x=10, y=60)
        self.btnline=Button(main, text="LINE", fg='black', width=8, command=self.line)
        self.btnline.place(x=10, y=110)
        self.btncir=Button(main, text="CIRCLE", fg='black', width=8, command=self.circle)
        self.btncir.place(x=10, y=160)
        self.btnfill=Button(main, text="FILL", fg='black', width=8, command=self.clickfillrec)
        self.btnfill.place(x=10, y=210)
        self.btnfillstack=Button(main, text="FILL STACK", fg='black', width=8, command=self.clickfillstack)
        self.btnfillstack.place(x=10, y=260)
        self.btnclear=Button(main, text="COLOR", fg='black', width=8, command=self.color_choice)
        self.btnclear.place(x=10, y=310)
        self.btnboundfill=Button(main, text="Bound Fill", fg='black', width=8, command=self.bound_fill_click)
        self.btnboundfill.place(x=10, y=360)
        self.btnboundstack=Button(main, text="Bound Stack", fg='black', width=8, command=self.bound_stack_click)
        self.btnboundstack.place(x=10, y=410)
        self.btn8wayfill=Button(main, text="8 Fill", fg='black', width=8, command=self.eightway_fill_click)
        self.btn8wayfill.place(x=10, y=460)
        self.btn8wayboundary=Button(main, text="8 Fill Bound", fg='black', width=8, command=self.eightway_bound_click)
        self.btn8wayboundary.place(x=10, y=510)
        self.btnscanfillflo=Button(main, text="Scanfill Flood", fg='black', width=8, command=self.scan_fillflo_click)
        self.btnscanfillflo.place(x=10, y=550)
        self.canvas = Canvas(self.main, bg='white', bd=5, relief=RIDGE, height=600, width=700)
        self.canvas.place(x=80, y=0)
        self.canvas.create_rectangle(0, 0, 750, 600, fill='white', outline='white')

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
        if(x > 0 and self.canvas.itemcget(item2, 'fill') == current_color):
                self.ffillrec((x-1), y)
        if (y > 0 and self.canvas.itemcget(item3, 'fill') == current_color): 
                self.ffillrec(x, (y-1))
        if (x < 800 and self.canvas.itemcget(item4, 'fill') == current_color): 
                self.ffillrec((x+1), y)
        if (y < 620 and self.canvas.itemcget(item5, 'fill') == current_color):
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
        
    def clickfillstack(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfillstack.configure(relief=SUNKEN)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.floodstackpos)
        self.canvas.bind("<B1-Motion>", self.nothing)      

    def floodstackpos(self, event):
        global current_color
        x = event.x
        y = event.y
        item = self.canvas.find_closest(x, y)
        current_color = self.canvas.itemcget(item, "fill")
        self.floodstack(x,y) 

    def floodstack(self, x, y):
        item2 = self.canvas.find_closest(x-1, y)
        item3 = self.canvas.find_closest(x, y-1)
        item4 = self.canvas.find_closest(x+1, y)
        item5 = self.canvas.find_closest(x, y+1)
        #print((self.canvas.itemcget(item2, 'fill')))
        #print(current_color)
        if current_color != self.color:
            stack.append((x,y))
            #print(stack)
            while stack != []:
                x,y = stack.pop()
                self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                #print("stack while", stack)
                if(x > 0 and self.canvas.itemcget(item2, 'fill') == current_color):
                    stack.append(((x-1), y))
                    #print("stack 1", stack)
                if (y > 0 and self.canvas.itemcget(item3, 'fill') == current_color): 
                    stack.append((x, (y-1)))
                    #print("stack 2", stack)
                if (x < 800 and self.canvas.itemcget(item4, 'fill') == current_color): 
                    stack.append(((x+1), y))
                    #print("stack 3", stack)
                if (y < 620 and self.canvas.itemcget(item5, 'fill') == current_color):
                    stack.append((x, (y+1)))
                    #print("stack 4", stack)

    
    def bound_fill_click(self):
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=SUNKEN)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.boufindobj)
        self.canvas.bind("<B1-Motion>", self.nothing)

    def boufindobj(self, event):
        global get_coords
        get_coords = self.canvas.coords(lines[0])
        get_coords = tuple(map(int, get_coords))
        x = event.x
        y = event.y
        self.boundfill(x,y)   

    def boundfill(self,x,y):#Blom jalan
        item = self.canvas.find_closest(x, y)
        item2 = self.canvas.find_closest(x-1, y)
        item3 = self.canvas.find_closest(x, y-1)
        item4 = self.canvas.find_closest(x+1, y)
        item5 = self.canvas.find_closest(x, y+1)
        borderlimit = self.canvas.create_oval(get_coords, outline='black')
        border = self.canvas.itemcget(borderlimit, 'outline')
        self.canvas.create_rectangle(x, y, x, y, fill=self.color, outline=self.color)
        if (x >= get_coords[0] and x <= get_coords[2]):
            if ((self.canvas.itemcget(item2, 'fill'))) != self.color and ((self.canvas.itemcget(item2, 'fill'))) != border:
                self.boundfill((x-1), y)
            if ((self.canvas.itemcget(item4, 'fill'))) != self.color and (self.canvas.itemcget(item4, 'fill')) != border:    
                self.boundfill((x+1), y)     
        if (y >= get_coords[1] and y <= get_coords[3]):
            if ((self.canvas.itemcget(item3, 'fill'))) != self.color and (self.canvas.itemcget(item3, 'fill')) != border: 
                self.boundfill(x, (y-1))
            if ((self.canvas.itemcget(item5, 'fill'))) != border and (self.canvas.itemcget(item5, 'fill')) != self.color:    
                self.boundfill(x, (y+1))

    def bound_stack_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnboundstack.configure(relief=SUNKEN)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.boundstackpos)
        self.canvas.bind("<B1-Motion>", self.nothing)   
    
    def boundstackpos(self,event):
        global current_color
        x = event.x
        y = event.y
        item = self.canvas.find_closest(x, y)
        current_color = self.canvas.itemcget(item, "fill")
        self.boundstack(x,y) 

    def boundstack(self,x,y):
        item = self.canvas.find_closest(x, y)
        item2 = self.canvas.find_closest(x-1, y)
        item3 = self.canvas.find_closest(x, y-1)
        item4 = self.canvas.find_closest(x+1, y)
        item5 = self.canvas.find_closest(x, y+1)
        borderlimit = self.canvas.create_oval(get_coords, outline='black')
        border = self.canvas.itemcget(borderlimit, 'outline')
        self.canvas.create_rectangle(x, y, x, y, fill=self.color, outline=self.color)

        if current_color != self.color:
            stack.append((x,y))
            #print(stack)
            while stack != []:
                x,y = stack.pop()
                self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                #print("stack while", stack)
                if ((self.canvas.itemcget(item2, 'fill'))) != self.color and ((self.canvas.itemcget(item2, 'fill'))) != border:
                    stack.append(((x-1), y))
                    #print("stack 1", stack)
                if ((self.canvas.itemcget(item4, 'fill'))) != self.color and (self.canvas.itemcget(item4, 'fill')) != border:
                    stack.append((x, (y-1)))
                    #print("stack 2", stack)
                if ((self.canvas.itemcget(item3, 'fill'))) != self.color and (self.canvas.itemcget(item3, 'fill')) != border: 
                    stack.append(((x+1), y))
                    #print("stack 3", stack)
                if ((self.canvas.itemcget(item5, 'fill'))) != border and (self.canvas.itemcget(item5, 'fill')) != self.color:
                    stack.append((x, (y+1)))
                    #print("stack 4", stack)
                    
    def eightway_fill_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=SUNKEN)
        self.canvas.bind("<Button-1>", self.eightwaypos)
        self.canvas.bind("<B1-Motion>", self.nothing)

    def eightwaypos(self, event):
        global get_coords
        get_coords = self.canvas.coords(lines[0])
        get_coords = tuple(map(int, get_coords))
        x = event.x
        y = event.y
        self.eightwayfill(x,y)
        
    def eightwayfill(self, x, y):
        item = self.canvas.find_closest(x, y)
        item2 = self.canvas.find_closest(x-1, y)
        item3 = self.canvas.find_closest(x, y-1)
        item4 = self.canvas.find_closest(x+1, y)
        item5 = self.canvas.find_closest(x, y+1)
        item6 = self.canvas.find_closest(x+1, y+1)
        item7 = self.canvas.find_closest(x-1, y-1)
        item8 = self.canvas.find_closest(x-1, y+1)
        item9 = self.canvas.find_closest(x+1, y-1)
        current_color = self.canvas.itemcget(item, "fill")
        self.canvas.create_rectangle(x, y, x, y, outline=self.color)
        if(x >= 0 and self.canvas.itemcget(item2, 'fill') == current_color):
            self.eightwayfill((x-1), y)
        if (x < 800 and self.canvas.itemcget(item4, 'fill') == current_color): 
            self.eightwayfill((x+1), y)
        if (y >= 0 and self.canvas.itemcget(item3, 'fill') == current_color): 
            self.eightwayfill(x, y - 1)
        if (y < 620 and self.canvas.itemcget(item5, 'fill') == current_color):
            self.eightwayfill(x,(y + 1))
        if (x >= 0 and x <800 and y> 0 and y < 620 and self.canvas.itemcget(item6, 'fill') == current_color):
            self.eightwayfill(x+1,(y + 1))
        if (x >= 0 and x <800 and y> 0 and y < 620 and self.canvas.itemcget(item9, 'fill') == current_color):
            self.eightwayfill(x + 1, y - 1)
        if (x >= 0 and x <800 and y> 0 and y < 620 and self.canvas.itemcget(item7, 'fill') == current_color):
            self.eightwayfill(x - 1, y - 1)
        if (x >= 0 and x <800 and y> 0 and y < 620 and self.canvas.itemcget(item8, 'fill') == current_color):
            self.eightwayfill(x - 1, y + 1)

    def eightway_bound_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.btn8wayboundary.configure(relief=SUNKEN)
        self.canvas.bind("<Button-1>", self.eightwayboundpos)
        self.canvas.bind("<B1-Motion>", self.nothing)

    def eightwayboundpos(self, event):
        global get_coords
        get_coords = self.canvas.coords(lines[0])
        get_coords = tuple(map(int, get_coords))
        x = event.x
        y = event.y
        self.eightwaybound(x,y)
        
    def eightwaybound(self, x, y):
        item = self.canvas.find_closest(x, y)
        item2 = self.canvas.find_closest(x-1, y)
        item3 = self.canvas.find_closest(x, y-1)
        item4 = self.canvas.find_closest(x+1, y)
        item5 = self.canvas.find_closest(x, y+1)
        item6 = self.canvas.find_closest(x+1, y+1)
        item7 = self.canvas.find_closest(x-1, y-1)
        item8 = self.canvas.find_closest(x-1, y+1)
        item9 = self.canvas.find_closest(x+1, y-1)
        current_color = self.canvas.itemcget(item, "fill")
        self.canvas.create_rectangle(x, y, x, y, outline=self.color)
        borderlimit = self.canvas.create_oval(get_coords, outline='black')
        border = self.canvas.itemcget(borderlimit, 'outline')
        if (x >= 0 and (self.canvas.itemcget(item2, 'fill')) != self.color and (self.canvas.itemcget(item2, 'fill')) != border):
            self.eightwaybound((x-1), y)
        if (x < 800 and (self.canvas.itemcget(item4, 'fill')) != self.color and (self.canvas.itemcget(item4, 'fill')) != border): 
            self.eightwaybound((x+1), y)
        if (y >= 0 and (self.canvas.itemcget(item3, 'fill')) != self.color and (self.canvas.itemcget(item3, 'fill')) != border): 
            self.eightwaybound(x, y - 1)
        if (y < 620 and (self.canvas.itemcget(item5, 'fill')) != self.color and (self.canvas.itemcget(item5, 'fill')) != border):
            self.eightwaybound(x,(y + 1))
        if (x >= 0 and x <800 and y >= 0 and y < 620 and (self.canvas.itemcget(item6, 'fill')) != self.color and (self.canvas.itemcget(item6, 'fill')) != border):
            self.eightwaybound(x+1,(y + 1))
        if (x >= 0 and x <800 and y >= 0 and y < 620 and (self.canvas.itemcget(item9, 'fill')) != self.color and (self.canvas.itemcget(item9, 'fill')) != border):
            self.eightwaybound(x + 1, y - 1)
        if (x >= 0 and x <800 and y >= 0 and y < 620 and (self.canvas.itemcget(item7, 'fill')) != self.color and (self.canvas.itemcget(item7, 'fill')) != border):
            self.eightwaybound(x - 1, y - 1)
        if (x >= 0 and x <800 and y >= 0 and y < 620 and (self.canvas.itemcget(item8, 'fill')) != self.color and (self.canvas.itemcget(item8, 'fill')) != border):
            self.eightwaybound(x - 1, y + 1)

    def scan_fillflo_click(self):
        self.btnscanfillflo.configure(relief=SUNKEN)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btn8wayfill.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.scanflopos)
        self.canvas.bind("<B1-Motion>", self.nothing)
    
    def scanflopos(self,event):
        global get_coords
        get_coords = self.canvas.coords(lines[0])
        get_coords = tuple(map(int, get_coords))
        x = event.x
        y = event.y
        self.scanfillflo(x,y)

    def scanfillflo(self, x, y): #result = not responding wkwkwk
        i = x
        item = self.canvas.find_closest(x, y)
        item2 = self.canvas.find_closest(i, y)
        current_color = self.canvas.itemcget(item, "fill")
        if current_color != self.color:
            while i >= 0:
                if self.canvas.itemcget(item2, "fill") != current_color:
                    self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                    i -= 1
            L = i + 1
            i = x + 1
            while i <= 700:
                if self.canvas.itemcget(item2, "fill") != current_color:
                    self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                    i += 1
            R = i - 1
            item3 = self.canvas.find_closest(i, y+1)
            item4 = self.canvas.find_closest(i, y-1)
            for i in range (L, R):
                if self.canvas.itemcget(item3, "fill") != current_color:
                    self.canvas.create_rectangle(i, y+1, i, y+1, outline=self.color)
                if self.canvas.itemcget(item4, "fill") != current_color:
                    self.canvas.create_rectangle(i, y-1, i, y-1, outline=self.color)
main = Tk()
p = Filling(main)
main.mainloop()
