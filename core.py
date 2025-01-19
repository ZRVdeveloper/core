#надпрограма "Core"
import sys
#Додаємо шлях до папки з проєктами
sys.path.insert(0, f'{sys.path[0]}\\projects\\')

from tkinter import Tk, Label, Button, PhotoImage
import fontawesome as fa
import CircleTimer, ZRVStyle, Gameplace, Kurs, passwordgenerator, alphacodegenerator

print(fa.icons['check-square'])

class Core(Tk):
    def CloseMain(self):
        self.after_cancel(self)
        self.destroy()
    def __init__(self):
        super().__init__()
        #self.overrideredirect(True)#Ховає верх
        self.geometry("800x500+20+20")
        self.title(f"Надпрограма 'Core' {fa.icons['check']}")
        #self.exitImage = PhotoImage(file=fa.icons['check-square']).subsample(7)
        self.CloseB = Button(self,command=self.CloseMain,text = 'X')#, image=self.exitImage)
        self.CloseB.place(x=750)
        self.H1 = ZRVStyle.ZRVH1(self, text='Надпрограма "CORE"')
        self.H1.place(y=0)
        #project1
        
        self.B1 = ZRVStyle.ZRVBtn(self,command=lambda:CircleTimer.CircleTimer(59), text = "Круговий таймер")
        self.B1.grid(pady = 50, padx = 20, column=1, row=1)
        self.B2 = ZRVStyle.ZRVBtn(self,command=lambda:print(1), text = "Круговий таймер")
        self.B2.grid(pady = 50, padx = 20, column=2, row=1)
        self.B3 = ZRVStyle.ZRVBtn(self,command=Gameplace.Games, text = "Ігрова зона")
        self.B3.grid(pady = 50, padx = 20, column=3, row=1)
        self.B4 = ZRVStyle.ZRVBtn(self,command=Kurs.Kurs_Valiut, text = "Курс валют")
        self.B4.grid(pady = 50, padx = 20, column=4, row=1)
        self.B5 = ZRVStyle.ZRVBtn(self,command=passwordgenerator.ZRVPassword_generator, text = "Генератор паролів")
        self.B5.grid(pady = 50, padx = 20, column=4, row=1)
        self.B6 = ZRVStyle.ZRVBtn(self,command=alphacodegenerator.ZRVAlpha_generator, text = "Генератор коду з числа")
        self.B6.grid(pady = 0, padx = 20, column=1, row=2)
        
if __name__=="__main__":      

    window = Core()    
    window.mainloop()
    

