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
        self.outline = "black"
        menubar = Menu(main)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Clear", command=self.clear)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=main.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        main.config(menu=menubar)
        general = Label(main, text = "Object").place(x = 10, y = 35) 
        self.btnsel=Button(main, text="SELECT", fg='black', width=8, command=self.select)
        self.btnsel.place(x=10, y=60)
        self.btnline=Button(main, text="LINE", fg='black', width=8, command=self.line)
        self.btnline.place(x=10, y=100)
        self.btncir=Button(main, text="CIRCLE", fg='black', width=8, command=self.circle)
        self.btncir.place(x=100, y=60)

        color = Label(main, text = "Color").place(x = 10, y = 140) 
        self.btnclear=Button(main, text="Fill", fg='black', width=8, command=self.color_choice)
        self.btnclear.place(x=10, y=170)
        self.btnoutline=Button(main, text="Outline", fg='black', width=8, command=self.color_outline)
        self.btnoutline.place(x=100, y=170)
        
        floodfill = Label(main, text = "Flood Fill Basic").place(x = 10, y = 210) 
        self.btnfill=Button(main, text="FILL", fg='black', width=8, command=self.clickfillrec)
        self.btnfill.place(x=10, y=240)
        self.btnfillstack=Button(main, text="FILL STACK", fg='black', width=8, command=self.clickfillstack)
        self.btnfillstack.place(x=100, y=240)

        Boundfill = Label(main, text = "Boundary Fill Basic").place(x = 10, y = 280) 
        self.btnboundfill=Button(main, text="Bound Fill", fg='black', width=8, command=self.bound_fill_click)
        self.btnboundfill.place(x=10, y=310)
        self.btnboundstack=Button(main, text="Bound Stack", fg='black', width=8, command=self.bound_stack_click)
        self.btnboundstack.place(x=100, y=310)

        scanfloodfill = Label(main, text = "Scanline").place(x = 10, y = 460) 
        self.btnscanfillflo=Button(main, text="ScanFlood Recursive", fg='black', width=8, command=self.scan_fillflo_click)
        self.btnscanfillflo.place(x=10, y=490)
        self.btnscanflostack=Button(main, text="ScanFlood Stack", fg='black', width=8, command=self.scanflostack_click)
        self.btnscanflostack.place(x=100, y=490)
        self.btnscanflostack=Button(main, text="ScanBound Recursive", fg='black', width=8, command=self.scanboundrec_click)
        self.btnscanflostack.place(x=10, y=530)
        self.btnscanflostack=Button(main, text="ScanBound Stack", fg='black', width=8, command=self.scanboundstack_click)
        self.btnscanflostack.place(x=100, y=530)

        self.canvas = Canvas(self.main, bg='white', bd=5, relief=RIDGE, height=600, width=600)
        self.canvas.place(x=180, y=0)
        self.canvas.create_rectangle(0, 0, 650, 600, fill='white', outline='white')

    def select(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=SUNKEN)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.unbind("<Button 1>")
        self.canvas.bind("<B1-Motion>") 
        
    def line(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=SUNKEN)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.bind("<ButtonPress-1>", self.line_click)
        self.canvas.bind("<B1-Motion>", self.drag) 
        
    def line_click(self, e):
        coords["x1"] = e.x
        coords["y1"] = e.y
        lines.append(self.canvas.create_line(coords["x1"],coords["y1"],coords["x1"],coords["y1"],fill=self.color))
        
    def circle(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=SUNKEN)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.bind("<ButtonPress-1>", self.circle_click)
        self.canvas.bind("<B1-Motion>", self.drag) 
        
    def circle_click(self, e):
        coords["x1"] = e.x
        coords["y1"] = e.y
        lines.append(self.canvas.create_oval(coords["x1"],coords["y1"],coords["x1"],coords["y1"],outline=self.outline, width=2))    
        
    def drag(self, e):
        coords["x2"] = e.x
        coords["y2"] = e.y
        self.canvas.coords(lines[-1], coords["x1"],coords["y1"],coords["x2"],coords["y2"])
        
    def clear(self):
        self.canvas.delete("all")
        coords = {"x1":0,"y1":0,"x2":0,"y2":0}
        lines = []
        DEFAULT_COLOR = 'black'
        x = 0
        y = 0
        stack = []
        
    def color_choice(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=SUNKEN)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.DEFAULT_COLOR = self.color
        self.color = askcolor(color=self.color)[1]

    def color_outline(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=SUNKEN)
        self.outline = askcolor(color=self.color)[1]

    def clickfillrec(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=SUNKEN)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.position)
        self.canvas.bind("<B1-Motion>", self.nothing)

    def position(self,event):
        global get_coords
        get_coords = self.canvas.coords(lines[0])
        get_coords = tuple(map(int, get_coords))
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
        if(x >= 0 and self.canvas.itemcget(item2, 'fill') == current_color):
                self.ffillrec((x-1), y)
        if (y >= 0 and self.canvas.itemcget(item3, 'fill') == current_color): 
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
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=SUNKEN)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
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
        #print((self.canvas.itemcget(item2, 'fill')))
        #print(current_color)
        if current_color != self.color:
            stack.append((x,y))
            #print(stack)
            while stack != []:
                x,y = stack.pop()
                item2 = self.canvas.find_closest(x-1, y)
                item3 = self.canvas.find_closest(x, y-1)
                item4 = self.canvas.find_closest(x+1, y)
                item5 = self.canvas.find_closest(x, y+1)
                self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                print("stack while", stack)
                if(x >= 0 and self.canvas.itemcget(item2, 'fill') == current_color):
                    stack.append(((x-1), y))
                    #print("stack 1", stack)
                if (y >= 0 and self.canvas.itemcget(item3, 'fill') == current_color): 
                    stack.append((x, (y-1)))
                    #print("stack 2")
                if (x < 800 and self.canvas.itemcget(item4, 'fill') == current_color): 
                    stack.append(((x+1), y))
                    #print("stack 3")
                if (y < 620 and self.canvas.itemcget(item5, 'fill') == current_color):
                    stack.append((x, (y+1)))
                    #print("stack 4")
    
    def bound_fill_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=SUNKEN)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.boufindobj)
        self.canvas.bind("<B1-Motion>", self.nothing)

    def boufindobj(self, event):
        global get_coords, borderlimit, border
        get_coords = self.canvas.coords(lines[0])
        get_coords = tuple(map(int, get_coords))
        x = event.x
        y = event.y
        self.boundfill(x,y)   

    def boundfill(self, x, y):
        item2 = self.canvas.find_closest(x-1, y)
        item3 = self.canvas.find_closest(x, y-1)
        item4 = self.canvas.find_closest(x+1, y)
        item5 = self.canvas.find_closest(x, y+1)
        self.canvas.create_rectangle(x, y, x, y,outline=self.color)
        if x >= 0 and ((self.canvas.itemcget(item2, 'fill') != self.color) and (self.canvas.itemcget(item2, 'outline') != self.outline)):
                self.boundfill((x-1), y)
                #print(x,y,"if 2")
        if y >= 0 and ((self.canvas.itemcget(item3, 'fill') != self.color) and (self.canvas.itemcget(item3, 'outline') != self.outline)): 
                self.boundfill(x, (y-1))
                #print(x,y,"if 3")
        if x < 800 and ((self.canvas.itemcget(item4, 'fill')  != self.color) and (self.canvas.itemcget(item4, 'outline') != self.outline)):
                self.boundfill((x+1), y)
                #print(x,y,"if 1")
        if y < 620 and ((self.canvas.itemcget(item5, 'fill') != self.color) and (self.canvas.itemcget(item5, 'outline') != self.outline)):    
                self.boundfill(x, (y+1))
                #print(x,y,"if 4")

    def bound_stack_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=SUNKEN)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
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
        stack.append((x,y))
        #print(stack)
        if self.outline != self.color:
            while stack != []:
                x,y = stack.pop()
                self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                item2 = self.canvas.find_closest(x-1, y)
                item3 = self.canvas.find_closest(x, y-1)
                item4 = self.canvas.find_closest(x+1, y)
                item5 = self.canvas.find_closest(x, y+1)
                print("stack while", stack)
                if (x >= 0 and (self.canvas.itemcget(item2, 'outline')) != self.outline and (self.canvas.itemcget(item2, 'fill')) != self.color):
                    stack.append(((x-1), y))
                    #print("stack 1", stack)
                if (y >= 0 and (self.canvas.itemcget(item4, 'outline')) != self.outline and (self.canvas.itemcget(item4, 'fill')) != self.color):
                    stack.append((x, (y-1)))
                    #print("stack 2", stack)
                if (x < 800 and (self.canvas.itemcget(item3, 'outline')) != self.outline and (self.canvas.itemcget(item3, 'fill')) != self.color): 
                    stack.append(((x+1), y))
                    #print("stack 3", stack)
                if (y < 620 and (self.canvas.itemcget(item5, 'outline')) != self.outline and (self.canvas.itemcget(item5, 'fill')) != self.color):
                    stack.append((x, (y+1)))
                    #print("stack 4", stack)

    def scan_fillflo_click(self):
        self.btnscanfillflo.configure(relief=SUNKEN)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=RAISED)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.scanflopos)
        self.canvas.bind("<B1-Motion>", self.nothing)
    
    def scanflopos(self,event):
        global current_color
        x = event.x
        y = event.y
        item = self.canvas.find_closest(x, y)
        current_color = self.canvas.itemcget(item, "fill")
        self.scanfillflo(x,y)

    def scanfillflo(self, x, y):
        i = x
        if current_color != self.color:
            while i >= 0:
                item2 = self.canvas.find_closest(i, y)
                if self.canvas.itemcget(item2, "fill") == current_color:
                    self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                    i -= 1
                else:
                    break
                print("while1", i)
            L = i + 1
            #print("while2R", L)
            i = x + 1
            while i <= 700:
                item2 = self.canvas.find_closest(i, y)
                if self.canvas.itemcget(item2, "fill") == current_color:
                    self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                    i += 1
                else:
                    break
                print("while2", i)
            R = i - 1
            #print("while2R", R)
            for i in range (L, R):
                item3 = self.canvas.find_closest(i, y+1)
                item4 = self.canvas.find_closest(i, y-1)
                if self.canvas.itemcget(item3, "fill") == current_color:
                    self.scanfillflo(i,(y+1))
                if self.canvas.itemcget(item4, "fill") == current_color:
                    self.scanfillflo(i,(y-1))
    
    def scanflostack_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=SUNKEN)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.scanflostackpos)
        self.canvas.bind("<B1-Motion>", self.nothing)

    def scanflostackpos(self,event):
        x = event.x
        y = event.y
        self.scanflostack(x,y)
    
    def scanflostack(self,x,y):
        item = self.canvas.find_closest(x, y)
        current_color = self.canvas.itemcget(item, "fill")
        if current_color != self.color:
            stack.append((x,y))
            while stack != []:
                x,y = stack.pop()
                i = x
                while i >= 0:
                    item2 = self.canvas.find_closest(i-1, y)
                    if self.canvas.itemcget(item2, "fill") == current_color:
                        i -= 1
                    else:
                        break
                spanabove = False
                spanbelow = False
                while i < 600:
                    print(i)
                    item = self.canvas.find_closest(i, y)
                    if self.canvas.itemcget(item, "fill") == current_color:
                        self.canvas.create_rectangle(i, y, i, y, outline=self.color)
                        if y < 600 :
                            item3 = self.canvas.find_closest(i, y+1)
                            if not spanabove and self.canvas.itemcget(item3, "fill") == current_color:
                                stack.append((i,(y+1)))
                                spanabove = True
                            elif spanabove and self.canvas.itemcget(item3, "fill") != current_color:
                                spanabove = False
                        if y > 0 :
                            item4 = self.canvas.find_closest(i, y-1)
                            if not spanbelow and self.canvas.itemcget(item4, "fill") == current_color:
                                stack.append((i,(y-1)))
                                spanbelow = True
                            elif spanbelow and self.canvas.itemcget(item4, "fill") != current_color:
                                spanbelow = False
                    else :
                        break
                    i += 1

    def scanboundrec_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=SUNKEN)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.scanboundpos)
        self.canvas.bind("<B1-Motion>", self.nothing)                   

    def scanboundpos(self,event):
        x = event.x
        y = event.y
        self.scanboundrec(x,y)
    
    def scanboundrec(self,x,y):
        i = x
        if self.outline != self.color:
            while i >= 0:
                item2 = self.canvas.find_closest(i, y)
                if self.canvas.itemcget(item2, "outline") != self.outline:
                    self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                    i -= 1
                else:
                    break
                print("while1", i)
            L = i + 1
            #print("while2R", L)
            i = x + 1
            while i <= 700:
                item2 = self.canvas.find_closest(i, y)
                if self.canvas.itemcget(item2, "outline") != self.outline:
                    self.canvas.create_rectangle(x, y, x, y, outline=self.color)
                    i += 1
                else:
                    break
                print("while2", i)
            R = i - 1
            #print("while2R", R)
            for i in range (L, R):
                item3 = self.canvas.find_closest(i, y+1)
                item4 = self.canvas.find_closest(i, y-1)
                if self.canvas.itemcget(item3, "outline") != self.outline:
                    self.scanboundrec(i,(y+1))
                if self.canvas.itemcget(item4, "outline") != self.outline:
                    self.scanboundrec(i,(y-1))

    def scanboundstack_click(self):
        self.btnscanfillflo.configure(relief=RAISED)
        self.btnboundstack.configure(relief=RAISED)
        self.btnfillstack.configure(relief=RAISED)
        self.btnscanflostack.configure(relief=SUNKEN)
        self.btnfill.configure(relief=RAISED)
        self.btncir.configure(relief=RAISED)
        self.btnsel.configure(relief=RAISED)
        self.btnline.configure(relief=RAISED)
        self.btnclear.configure(relief=RAISED)
        self.btnboundfill.configure(relief=RAISED)
        self.btnoutline.configure(relief=RAISED)
        self.canvas.bind("<Button-1>", self.scanboundstackpos)
        self.canvas.bind("<B1-Motion>", self.nothing)    

    def scanboundstackpos(self,event):
        x = event.x
        y = event.y
        self.scanboundstack(x,y)

    def scanboundstack(self,x,y):
        item = self.canvas.find_closest(x, y)
        current_color = self.canvas.itemcget(item, "fill")
        if self.outline != self.color:
            stack.append((x,y))
            while stack != []:
                x,y = stack.pop()
                i = x
                while i >= 0:
                    item2 = self.canvas.find_closest(i-1, y)
                    if self.canvas.itemcget(item2, "outline") != self.outline:
                        i -= 1
                    else:
                        break
                spanabove = False
                spanbelow = False
                while i < 600:
                    print(i)
                    item = self.canvas.find_closest(i, y)
                    if self.canvas.itemcget(item, "outline") == self.outline:
                        self.canvas.create_rectangle(i, y, i, y, outline=self.color)
                        if y < 600 :
                            item3 = self.canvas.find_closest(i, y+1)
                            if not spanabove and self.canvas.itemcget(item3, "outline") != self.outline:
                                stack.append((i,(y+1)))
                                spanabove = True
                            elif spanabove and self.canvas.itemcget(item3, "outline") == self.outline:
                                spanabove = False
                        if y > 0 :
                            item4 = self.canvas.find_closest(i, y-1)
                            if not spanbelow and self.canvas.itemcget(item4, "outline") != self.outline:
                                stack.append((i,(y-1)))
                                spanbelow = True
                            elif spanbelow and self.canvas.itemcget(item4, "outline") == self.outline:
                                spanbelow = False
                    else :
                        break
                    i += 1

main = Tk()
p = Filling(main)
main.mainloop()