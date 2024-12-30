from tkinter import Button, Label
class ZRVBtn(Button):
 def __init__(self, master=None, **kwargs):
     # Задаємо параметри за замовчуванням
        default_properties = {
            "bg": "#333",
            "fg": "#fff",
            "font": ("Arial", 12, "bold"),
            "activebackground": "red",
            "cursor": "hand2"
        }
        # Поєднуємо параметри за замовчуванням із переданими
        default_properties.update(kwargs)
        # Викликаємо ініціалізацію базового класу
        super().__init__(master, **default_properties)
class ZRVLBL(Label):
 def __init__(self, master=None, **kwargs):
     # Задаємо параметри за замовчуванням
        default_properties = {
            "fg": "Black",
            "font": ("Tahoma", 10, "bold"),
            "justify":"center"
        }
        # Поєднуємо параметри за замовчуванням із переданими
        default_properties.update(kwargs)
        # Викликаємо ініціалізацію базового класу
        super().__init__(master, **default_properties)
class ZRVH1(ZRVLBL):
 def __init__(self, master=None, **kwargs):
     # Задаємо параметри за замовчуванням
        default_properties = {
            "font": ("Tahoma", 28, "bold")
        }
        # Поєднуємо параметри за замовчуванням із переданими
        default_properties.update(kwargs)
        # Викликаємо ініціалізацію базового класу
        super().__init__(master, **default_properties)
  
if __name__=="__main__":
    from tkinter import Tk
    main = Tk()
    b = ZRVBtn(main,command = lambda:print(1), text = "click")
    b.pack()
    b = ZRVH1(main, text = "Hello")
    b.pack()
    main.mainloop()
    
'''
Щоб створити власну кнопку на основі віджета Button з tkinter,
ти можеш створити клас, який успадковує функціонал базового класу Button.
Це дозволить тобі зберегти всі функції основного віджета,
додавши при цьому свої власні параметри за замовчуванням.

Ось приклад створення такої кастомної кнопки:

Пояснення:
Успадкування: Клас ZRVButton успадковує всі методи та властивості класу Button.
Параметри за замовчуванням: У словнику default_properties визначені базові параметри, які можна перевизначити під час створення кнопки.
Поєднання параметрів: Передані параметри kwargs оновлюють значення параметрів за замовчуванням.
Гнучкість: Ти можеш додати будь-яку власну логіку чи додаткові властивості в цей клас.
Тепер ти можеш створювати кнопки з передвстановленими стилями або поведінкою, залишаючи можливість повністю налаштовувати їх.
'''