from tkinter import *
# this file demonstrates the movement of a single canvas item under mouse control

class Bezier(Tk):
    ################### ################################################
    ###### Event callbacks for THE CANVAS (not the stuff drawn on it)
    ###################################################################

    
    def mouseclick(self, event):
        #click event
        self.lastx = event.x
        self.lasty = event.y
        self.click = self.click + 1
        if(self.click == 1):
            self.initial_point = self.draw.create_rectangle(self.lastx, self.lasty, self.lastx+10, self.lasty+10,
                                        fill="white", tags="selected")
            self.draw.tag_bind(self.initial_point, "<Any-Enter>", self.mouseEnter)
            self.draw.tag_bind(self.initial_point, "<Any-Leave>", self.mouseLeave)
        
        
        if(self.click == 2):
            self.control_point_1 = self.draw.create_rectangle(self.lastx, self.lasty, self.lastx+10, self.lasty+10,
                                        fill="white", tags="selected")
            self.draw.tag_bind(self.control_point_1, "<Any-Enter>", self.mouseEnter)
            self.draw.tag_bind(self.control_point_1, "<Any-Leave>", self.mouseLeave)
        
        if(self.click == 3):
            self.control_point_2 = self.draw.create_rectangle(self.lastx, self.lasty, self.lastx+10, self.lasty+10,
                                        fill="white", tags="selected")
            self.draw.tag_bind(self.control_point_2, "<Any-Enter>", self.mouseEnter)
            self.draw.tag_bind(self.control_point_2, "<Any-Leave>", self.mouseLeave)
        
        if(self.click == 4):
            self.end_point = self.draw.create_rectangle(self.lastx, self.lasty, self.lastx+10, self.lasty+10,
                                        fill="white", tags="selected")
            self.draw.tag_bind(self.end_point, "<Any-Enter>", self.mouseEnter)
            self.draw.tag_bind(self.end_point, "<Any-Leave>", self.mouseLeave)
          
        
    
        

    def mouseMove(self, event):
        # whatever the mouse is over gets tagged as CURRENT for free by tk.
        self.draw.move(CURRENT, event.x - self.lastx, event.y - self.lasty)
        self.lastx = event.x
        self.lasty = event.y
        
        #Draw a bezier curve given the initial point, control point 1, control point 2, and end point
        self.draw.coords(self.initial_point)[0]
        
        point_list = [ ( (self.draw.coords(self.initial_point)[0] +  self.draw.coords(self.initial_point)[2])/2,  
        (self.draw.coords(self.initial_point)[1] +  self.draw.coords(self.initial_point)[3])/2), 
        ((self.draw.coords(self.end_point)[0] +  self.draw.coords(self.end_point)[2])/2,
        (self.draw.coords(self.end_point)[1] +  self.draw.coords(self.end_point)[3])/2),
        ((self.draw.coords(self.control_point_2)[0] +  self.draw.coords(self.control_point_2)[2])/2,
        (self.draw.coords(self.control_point_2)[1] +  self.draw.coords(self.control_point_2)[3])/2),
        ((self.draw.coords(self.control_point_1)[0] +  self.draw.coords(self.control_point_1)[2])/2,
        (self.draw.coords(self.control_point_1)[1] +  self.draw.coords(self.control_point_1)[3])/2)]
        
        self.draw.delete("circles")
        t = 0.005
        # print(point_list)
        self.draw_Bezier(point_list, t)
        
        
    def mouseEnter(self, event):
        # the CURRENT tag is applied to the object the cursor is over.
        # this happens automatically.
        self.draw.itemconfig(CURRENT, fill="red")


    def draw_Bezier(self, point_list, t):
                
        if  t >= 1:
            return point_list[0]    
        else:
            nt = 1.0 - t
            #obtain x of the bezier curve
            px = (nt**3)*point_list[0][0] + (3*t*nt**2)*point_list[1][0] + (3*t**2*nt)*point_list[2][0] + (t**3)*point_list[3][0]
            py = (nt**3)*point_list[0][1] + (3*t*nt**2)*point_list[1][1] + (3*t**2*nt)*point_list[2][1] + (t**3)*point_list[3][1]
            
            #Find the next point of the bezier curve
            nt_var = 1.0 - t + 0.002
            next_px = (nt_var**3)*point_list[0][0] + (3*t*nt_var**2)*point_list[1][0] + (3*t**2*nt_var)*point_list[2][0] + (t**3)*point_list[3][0]
            next_py = (nt_var**3)*point_list[0][1] + (3*t*nt_var**2)*point_list[1][1] + (3*t**2*nt_var)*point_list[2][1] + (t**3)*point_list[3][1]
            # #the derivative of the bezier curve
            # dpx = (3*nt**2)*(point_list[1][0] - point_list[0][0]) + (6*t*nt)*(point_list[2][0] - point_list[1][0]) + (3*t**2)*(point_list[3][0] - point_list[2][0])
            # dpy = (3*nt**2)*(point_list[1][1] - point_list[0][1]) + (6*t*nt)*(point_list[2][1] - point_list[1][1]) + (3*t**2)*(point_list[3][1] - point_list[2][1])
            # #find the angle of the tangent
            # angle = math.atan2(dpy, dpx)
            
            # print(px, py)
            self.draw.create_oval(px, py, px + 3, py + 3, fill="black", tags="circles")
            # self.draw.create_line(px, py, next_px, next_py, fill="black", tags="circles")
            t = t + 0.002
            self.draw_Bezier(point_list, t)
            
            # print(point_list)
                
                
    def mouseLeave(self, event):
        # the CURRENT tag is applied to the object the cursor is over.
        # this happens automatically.
        self.draw.itemconfig(CURRENT, fill="white")
        
        
        

    def createWidgets(self):
        self.QUIT = Button(self, text='QUIT', foreground='red',
                           command=self.quit)
        self.QUIT.pack(side=LEFT, fill=BOTH)
        self.draw = Canvas(self, width="9i", height="9i")
        self.draw.pack(side=LEFT)

        Widget.bind(self.draw, "<1>", self.mouseclick)
        Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)


    
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.click = 0
        self.createWidgets()
        
        

Bezier = Bezier()
Bezier.mainloop()
