#Задача Код на виріб
'''
Є станок, що виробляє дуже дрібні запчастини. Для їх нумерації використовувати числа недоцільно
Вирішили використати символи ( у прикладі це український алфавіт)
Алгоритм працює так: коли пройдено всі знаки у наборі, наступний це комбінація першого і символу у розряді()
тобто 34 - aa, 67 - ба, 3333 - вая
19.01.2025

'''
#шифрує число у набір символів

from tkinter import Text, Toplevel, StringVar, Label, Entry, Button, END, INSERT
import pyperclip
class ZRVAlpha_generator(Toplevel):
    p = ['','','','','']
    aa = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    i1, i2, i3, i4,i5 = 0, 0, 0, 0, 0
    #s = 100
    rez_n = 0
    n = len(aa)
    def generator (self, s = 3333):        
        while True:
            if self.i1 // len(self.aa) == 1:
                #print(1)
                self.i1 = 0
                self.i2 += 1
                self.p[1] = self.aa[self.i2-1]
                if self.i2 // len(self.aa) == 1:
                    self.i2 = 0
                    self.i3 += 1
                    self.p[2] = self.aa[self.i3-1]
                    #rint(p)
                    if self.i3 // len(self.aa) == 1:
                        self.i3 = 0
                        self.i4 += 1
                        self.p[3] = self.aa[self.i4-1]
                        if self.i4 // len(self.aa) == 1:
                            self.i4 = 0
                            self.i5 += 1
                            self.p[4] = self.aa[self.i5-1]
            self.i1 += 1
            self.p[0] = self.aa[self.i1-1]
            s -=1
            self.rez_n += 1
            if s == 0: break
            
            #print(p, rez_n)
        self.p.reverse()
        return self.p, self.rez_n
    def work(self):
        r, n = self.generator(int(self.string_pass.get()))
        r2=''
        for el in r:
            r2 += el
        cod = f'{n} = {r2}'
        pyperclip.copy(cod)
        print('Результат', f'Ваш код {cod} \nКод зкопійований у буфер обміну')
        self.passw.delete('1.0', END)
        self.passw.insert(INSERT, pyperclip.paste())
        self.p = ['','','','','']
        self.i1, self.i2, self.i3, self.i4, self.i5 = 0, 0, 0, 0, 0
        self.rez_n = 0
    def __init__(self):
        super().__init__()
        self.title('Генератор коду')
        self.geometry("250x200+100+100")
        self.resizable(0,0)
        self.string_pass = StringVar(value=100)
        self.label = Label(master = self,text="Число для перетворення", font=['Arial',14]).pack(pady=10)
        self.txt = Entry(master = self,textvariable=self.string_pass, font=['Arial',14], width = 7).pack()
        self.btn = Button(master = self,text="Згенерувати", command=self.work, font=['Arial',14]).pack(pady=10)
        self.passw = Text(master = self, height = 5,width = 20,bg = "white", font=['Arial',14])
        self.passw.pack(pady=10)
        

if __name__== "__main__":
    print ("ZRVAlpha_generator")
    g = ZRVAlpha_generator()    
    g.mainloop()