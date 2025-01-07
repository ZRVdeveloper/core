import sys
#Додаємо шлях до папки з проєктами
sys.path.insert(0, f'{sys.path[0]}\\gamesgameplace\\')
from tkinter import Toplevel, Label
import ZRVStyle, AnimalEat




class Games(Toplevel): 
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.H1 = ZRVStyle.ZRVH1(self, text='Обери гру')
        self.H1.place(y=0)
        self.B1 = ZRVStyle.ZRVBtn(self,command=AnimalEat.AnimalEat, text = "Нагодуй тваринку")
        self.B1.grid(pady = 50, padx = 20, column=1, row=1)
  
if __name__=="__main__": 
    g = Games()
    g.mainloop()