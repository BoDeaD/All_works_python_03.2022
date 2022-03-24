from tkinter import *
window = Tk() 
window.title("Main window")
window.iconbitmap('f:/Games/icon.jpg')
'''
window.iconbitmap - window переменная в которой храняться методы.
iconbitmap - Метод позволяющий поменять иконку окна(в скобках указываем путь и формат файла)
'''
SIZE = '400x300'
window.geometry(SIZE)

label = Label(text = 'Hello', bg = 'black', fg = 'white') #fg - Цвет текста
label.pack() #Label - Виджет,label - переменная в которой записан виджет, pack - метод, с помощью него можно вывести заданые в переменной атрибуты
label = Label(text = 'hello 1', bg = 'black', fg = 'white', font = ('Arial',20,'bold'))
# font(шрифт(порядок)) - ("название шрифта", "размер","начертание" ) Выше пример!
label.pack()
# Порядок зависит от "что выше, то первое и выводиться"
entry = Entry(width = 30) #entry - переменая в которую мы записали МЕТОД Entry
#Entry - Виджет. Создаёт (с помощью команды entry.pack) текстовое поле(в него можно записать текст(пользователю))
entry.pack()

def insert():
    entry.insert(0,'Hello  ')
#insert - функцыя insert принимает первую позицыю(куда вставить текст). Индекс (в данном случаи это "0")где начинать

def delete():
    entry.delete(0, END)
#END - От начала до конца чистить наше поле

button = Button(text = "Click me", bg = '#fff', fg = '#000', width = 10, height = 10)
#Button - Виджет. Создаёт кнопку в скобках прописываем атрибуты
button.config(command = insert) #С помощью этой команды мы говорим что-бы кнопка добовляла текст с созданой функцыи insert
button.pack(side = LEFT, padx = 10, pady = 15) #МЫ хотим упаковать нашу кнопку "Слево","Отсупить по x 10","По y 15"
#command - Метод. реагирует на действие пользователя, активацию виджета(нажатие кнопки)
del_button = Button(text = "Delete", bg = '#fff', fg = '#000', width = 10, height = 10)
del_button.config(command = delete)
del_button.pack(side = RIGHT, padx = 10, pady = 15)

window.mainloop()
