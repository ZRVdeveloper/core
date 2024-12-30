from tkinter import Toplevel, Canvas #, Label
class CircleTimer(Toplevel):
 c = 359.999999
 def End(self):
  self.place.itemconfig(self.arc, extent=self.c)
  self.c -= 1
  #self.k.config(text = self.c)
  if self.c > -1:
   self.after(5, self.End)
   #self.update()
  else:
   self.place.itemconfig(self.arc, extent=359.99)
  
  
 def New(self):
  if self.t // 60 != 0 :
      self.place.itemconfig(self.tx, text = self.t // 60)
  else:
      self.place.itemconfig(self.tx, text = self.t)
      
  self.place.itemconfig(self.arc, extent=self.c)
  self.t -=1
  self.c -= self.step
  if self.t != -1:
   self.after(1000,self.New)
  else:
   self.c =359
   #self.place.itemconfig(self.tx, text = 360)
   self.place.itemconfig(self.arc, extent=self.c, outline='red')
   self.End()
 def __init__(self, t = 5, ttype='second'):
  super().__init__()
  self.geometry("400x400")
  self.t = t
  #self.k = Label(text="1")
  #self.k.pack()
  self.step = self.c/self.t
  self.place = Canvas(self, width=400, height=400)
  self.arc = self.place.create_arc(100, 100, 300, 300, start=90, extent=0, style='arc',outline='darkgreen', width=20) # малювання синього сектора
  self.tx = self.place.create_text(200, 200, # координати центрування тексту
              text="_", # текст, що відображатиметься на полотні
              justify='center', # вирівнювання тексту по центру
              font="Tahoma 45")
  self.place.pack()
  #for i in range(self.t, 0, -1):
  self.New
  self.after(1000, self.New)
if __name__=="__main__": 
    t = CircleTimer(59)
    t.mainloop()