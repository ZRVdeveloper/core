
import requests
import json
from tkinter import *
from tkinter import messagebox, ttk

class Kurs_Valiut(Toplevel):
    w = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    w2 = 'img/exchange.json'
    options_list = []  
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.Title = Label(self, text="Курс валют",
                           font = ["Comic Sans MS",18])
        self.Title.grid(column=0,
                        row = 0,
                        columnspan = 2,
                        padx=10,
                        pady=10,sticky="W")
        self.btn_i = Button(self, text='Завантажити з інтернету',
                          command = lambda: self.show("i"),
                          font = ["Comic Sans MS",12])
        self.btn_i.grid(column=0,
                        row = 1,
                        padx=10,
                        pady=10, sticky="W")
        self.btn_f = Button(self, text='Завантажити з файлу',
                          command = lambda: self.show("f"),
                          font = ["Comic Sans MS",12])
        self.btn_f.grid(column=1,
                        row = 1,
                        padx=10,
                        pady=10, sticky="W")
        self.Kurs_r_name = Label(self, text = '',font = ["Comic Sans MS",16],fg="blue", justify="left")
        self.Kurs_r_name.grid(column=1, row = 3, )
        
    def show(self,t=None):        
        if t == 'i':
            self.data = self.download_json()
        elif t == 'f':
            self.data = self.open_json()
        else:
            self.data = 'error'
        for el in self.data:
            self.options_list.append(el["txt"])
        self.value_inside = StringVar() 
  
        # Set the default value of the variable 
        self.value_inside.set("Оберіть валюту")
        # Create the optionmenu widget and passing  
        # the options_list and value_inside to it. 
        #self.Kurs_question_menu = OptionMenu(self, self.value_inside, *self.options_list)
        self.Kurs_question_menu = ttk.Combobox(self, values = self.options_list)
        
        self.Kurs_question_menu.grid(column=0, row = 2)
        self.btn = Button(self, text='Переглянути курс',
                          command = self.kurs,
                          font = ["Comic Sans MS",12])
        self.btn.grid(column=1, row = 2, sticky ="W")
        self.btn_d = Button(self, text="Долар США", command = lambda:self.kurs("Долар США"))
        self.btn_d.grid(column=0, row= 4)
        self.btn_e = Button(self, text="Євро", command = lambda:self.kurs("Євро"))
        self.btn_e.grid(column=0, row= 5)
    def download_json(self):
        try:
            url = requests.get(self.w)
            u = url.text
        except:
            messagebox.showerror("showerror", "Error")
            u = {
                "0": 0,
                "txt": "Немає даних",
                "rate": 0,
                "cc": "Немає данних",
                "exchangedate": "00.00.2000"
                }
            
        finally:            
            self.y = json.loads(u)
        return self.y
    def open_json(self):
        with open ('img/exchange.json',mode="r", encoding="utf-8") as f:
            self.y = json.load(f)
        return self.y
    def kurs(self,s = 'Євро'):
        if s == None:  
        	self.select = self.Kurs_question_menu.get()
        else:
        	self.select = s
        for i in range(len(self.data)):
                if self.data[i]["txt"] == self.select:
                    r = self.data[i]
        t_rez = f"Назва: {r['txt']} \nКоротка назва: {r['cc']} \nКурс: {r['rate']} \nДата: {r['exchangedate']}"
        self.Kurs_r_name.config( text = t_rez)

if __name__ == "__main__":
    k = Kurs_Valiut()
    k.mainloop()