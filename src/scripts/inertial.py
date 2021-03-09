from Tkinter import *
import math

class Inertial:
    
    def __init__(self):
        self.root=Tk()
        self.root.title('Inertia-Calculator')
        self.root.geometry('600x400')
        Button(self.root,text='Box',command=self.box).grid(row=0,column=0)
        Button(self.root,text='Sphere',command=self.sphere).grid(row=0,column=1)
        Button(self.root,text='Cylinder',command=self.cylinder).grid(row=0,column=2)
        Button(self.root,text='CE',command=self.redo).grid(row=0,column=3)
        self.inputtxt = Text(self.root, height = 10, width = 25, bg = "white") 
        self.m=[]
        for i in range(4):
            x=StringVar()
            self.m.append(x)
        self.root.mainloop()
    
    def redo(self):
        self.root.destroy()
        Inertial()
    
    def output(self,n):
        if n==0:
            m=float(self.m[0].get())
            x=float(self.m[1].get())
            y=float(self.m[2].get())
            z=float(self.m[3].get())
            Ix=round(((y**2+z**2)*m)/12,3)
            Iy=round(((x**2+z**2)*m)/12,3)
            Iz=round(((y**2+x**2)*m)/12,3)
        
        elif n==1:
            m=float(self.m[0].get())
            radius=float(self.m[1].get())
            Ix=Iy=Iz=round(0.4*m*(radius**2),3)
        
        elif n==2:
            m=float(self.m[0].get())
            radius=float(self.m[1].get())
            height=float(self.m[2].get())
            Ix=Iy=round(m*((3*(radius**2))+(height**2))*1/12,3)
            Iz=round(m*(radius**2)*0.5,3)
        
        self.inputtxt.insert(END,"Ixx=\""+str(Ix)+"\"\n"+"Iyy=\""+str(Iy)+"\"\n"+"Izz=\""+str(Iz)+"\"")
        self.inputtxt.grid(row=6,column=5)
    
    def box(self):
        
        Label(self.root, text="mass").grid(row=1,column=0)
        Entry(self.root,width=5,textvariable=self.m[0]).grid(row=1,column=1)
        Label(self.root, text="X").grid(row=2,column=0)
        Entry(self.root,width=5,textvariable=self.m[1]).grid(row=2,column=1)
        Label(self.root, text="Y").grid(row=3,column=0)
        Entry(self.root,width=5,textvariable=self.m[2]).grid(row=3,column=1)
        Label(self.root, text="z").grid(row=4,column=0)
        Entry(self.root,width=5,textvariable=self.m[3]).grid(row=4,column=1)
        Button(self.root,text='Calculate',command=lambda:self.output(0)).grid(row=5,column=1)
    
    def sphere(self):
        
        Label(self.root, text="mass").grid(row=1,column=0)
        Entry(self.root,width=5,textvariable=self.m[0]).grid(row=1,column=1)
        Label(self.root, text="radius").grid(row=2,column=0)
        Entry(self.root,width=5,textvariable=self.m[1]).grid(row=2,column=1)
        Button(self.root,text='Calculate',command=lambda:self.output(1)).grid(row=5,column=1)
    
    def cylinder(self):
        
        Label(self.root, text="mass").grid(row=1,column=0)
        Entry(self.root,width=5,textvariable=self.m[0]).grid(row=1,column=1)
        Label(self.root, text="radius").grid(row=2,column=0)
        Entry(self.root,width=5,textvariable=self.m[1]).grid(row=2,column=1)
        Label(self.root, text="height").grid(row=3,column=0)
        Entry(self.root,width=5,textvariable=self.m[2]).grid(row=3,column=1)        
        Button(self.root,text='Calculate',command=lambda:self.output(2)).grid(row=5,column=1)

if __name__=='__main__':
    
    Inertial()