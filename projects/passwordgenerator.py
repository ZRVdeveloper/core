import random
from tkinter import Text, Toplevel, StringVar, Label, Entry, Button, END, INSERT
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import pyperclip


class ZRVPassword_generator(Toplevel):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['@', '#', '$', '%', '&', '*']
    def process(self):
        length = int(self.string_pass.get())        
        self.all = self.lower + self.upper + self.num + self.special
        '''
        sample() — це вбудована функція випадкового модуля в Python, яка повертає певну довжину списку елементів, вибраних із послідовності, тобто списку, кортежу, рядка або набору. Використовується для випадкової вибірки без заміни.

        Синтаксис: random.sample(sequence, k)   
        Параметри: 
        sequence : може бути списком, кортежем, рядком або набором. 
        k : ціле число, воно визначає довжину вибірки.   
        Повертає: новий список елементів, вибраних із послідовності, довжиною k.'''
        ran = random.sample(self.all,length)
        password = "".join(ran)
        messagebox.showinfo('Результат', f'Ваш пароль {password} \nПароль зкопійований у буфер обміну')
        pyperclip.copy(password)
        print('Результат', f'Ваш пароль {password} \nПароль зкопійований у буфер обміну')
        self.passw.delete('1.0', END)
        self.passw.insert(INSERT, pyperclip.paste())
    def __init__(self):
        super().__init__()
        self.title('Генератор паролів')
        self.geometry("250x200+100+100")
        self.resizable(0,0)
        self.string_pass = StringVar(value=8)
        self.label = Label(master = self,text="Довжина пароля", font=['Arial',14]).pack(pady=10)
        self.txt = Entry(master = self,textvariable=self.string_pass, font=['Arial',14]).pack()
        self.btn = Button(master = self,text="Згенерувати", command=self.process, font=['Arial',14]).pack(pady=10)
        self.passw = Text(master = self, height = 5,width = 20,bg = "white", font=['Arial',14])
        self.passw.pack(pady=10)



if __name__== "__main__":
    print ("ZRVPassword_generator")
    g = ZRVPassword_generator()    
    g.mainloop()


